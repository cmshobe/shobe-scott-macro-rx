#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 20 10:45:29 2026

@author: charlesshobe
"""

import sys
import numpy as np
import copy as cp
import numba as nb
import time as timer
import csv

start_time = timer.time()

@nb.jit(nb.types.Tuple((nb.float64, nb.float64, nb.float64, nb.float64))(nb.float64, nb.float64,
                                                 nb.float64, nb.float64,
                                                 nb.float64, nb.float64,
                                                 nb.float64, nb.float64,
                                                 nb.float64, nb.float64,
                                                 nb.float64,
                                                 nb.int8),nopython=True)
def total_flow_resistance(Q, d_r, wb, theta, a1, a2, sigma_z, g, S, chan_depth,
                         e, use_fp):
    
    calc_Q_r = 0
    while np.isclose(calc_Q_r, Q, rtol=1e-3) == False: 
        #while we haven't converged on a roughened depth that yields the correct discharge value...

        if calc_Q_r < Q:
            d_r += 1e-5
        elif calc_Q_r > Q:
            d_r -= 1e-5
        
        #break up numerical solution into component terms so it isn't so crazy
        width_area_term_r = wb + d_r / np.tan(theta) #this is hard to explain: it's the term that gets multiplied by depth to give XS area. It's wb + d/tan(theta)
        
        #cross-sectional area term
        xs_area_r = width_area_term_r * d_r #xs area of flow incl. wood roughness
        
        #wetted perimeter
        wp_r = wb + 2 * (d_r / np.sin(theta))
        
        #wood-roughened hydraulic radius
        R_r = xs_area_r / wp_r
        
        #VPE sqrt(8/f) term
        VPE_term_numerator = a1 * a2 * (R_r/ sigma_z)
        VPE_term_denomenator = np.power(np.power(a1, 2) + np.power(a2, 2) * np.power(R_r / sigma_z, 5/3), 1/2)
        VPE_term = VPE_term_numerator / VPE_term_denomenator
        
        #reduced energy slope
        sqrt_f_over_f_r_numerator = a2 * np.power(R_r / sigma_z, 5/6)
        sqrt_f_over_f_r_denomenator = np.power(np.power(a1, 2) + np.power(a2, 2) * np.power(R_r / sigma_z, 5/3), 1/2)
        sqrt_f_over_f_r = sqrt_f_over_f_r_numerator / sqrt_f_over_f_r_denomenator
        
        #calculate f_r / f for comparison with field studies (Follett and Wohl, etc)
        f_r_over_f = 1 / np.power(sqrt_f_over_f_r, 2)
        
        S_r = S * np.power(sqrt_f_over_f_r, e) #* np.power(d / d_r, e / 6)
        
        #square root term
        sqrt_term_r = np.power(g * R_r * S_r, 1/2)
        
        #finally, calculate discharge as product of the three terms
        calc_Q_r = xs_area_r * VPE_term * sqrt_term_r
        
        
        
    if (d_r > chan_depth) and (use_fp == 1): #if flow is going overbank...
        calc_Q_r = Q #trip the flag to stop accruing depth
    
        d_r = chan_depth
        
        #break up numerical solution into component terms so it isn't so crazy
        width_area_term_r = wb + d_r / np.tan(theta) #this is hard to explain: it's the term that gets multiplied by depth to give XS area. It's wb + d/tan(theta)
        
        #cross-sectional area term
        xs_area_r = width_area_term_r * d_r #xs area of flow incl. wood roughness
        
        #wetted perimeter
        wp_r = wb + 2 * (d_r / np.sin(theta))
        
        #wood-roughened hydraulic radius
        R_r = xs_area_r / wp_r
        
        #VPE sqrt(8/f) term
        VPE_term_numerator = a1 * a2 * (R_r/ sigma_z)
        VPE_term_denomenator = np.power(np.power(a1, 2) + np.power(a2, 2) * np.power(R_r / sigma_z, 5/3), 1/2)
        VPE_term = VPE_term_numerator / VPE_term_denomenator
        
        #reduced energy slope
        sqrt_f_over_f_r_numerator = a2 * np.power(R_r / sigma_z, 5/6)
        sqrt_f_over_f_r_denomenator = np.power(np.power(a1, 2) + np.power(a2, 2) * np.power(R_r / sigma_z, 5/3), 1/2)
        sqrt_f_over_f_r = sqrt_f_over_f_r_numerator / sqrt_f_over_f_r_denomenator
        
        
        #calculate f_r / f for comparison with field studies (Follett and Wohl, etc)
        f_r_over_f = 1 / np.power(sqrt_f_over_f_r, 2)
        
        S_r = S * np.power(sqrt_f_over_f_r, e) #* np.power(d / d_r, e / 6)
        
    return R_r, S_r, d_r, f_r_over_f

def channel_evolution_equilibrium(time_to_run,
         timestep,
         reach_length,
         Q,
         Qs_in,
         wb,
         theta,
         sigma_z,
         l_bed_obstacle,
         l_bank_obstacle,
         k_ero,
         k_dep,
         S,
         d50,
         h_floodplain,
         use_fp):
    
    #constants
    tolerance_over_timestep = 1e-13
    a1 = 6.5 #VPE constant
    a2 = 2.5 #VPE constant
    rho_w = 1000 #kg/m^3; water density
    rho_s = 2650 #kg/m^3, sed density
    g = 9.81 #m/s^2 accel due to gravity
    e = 1.5 #range of 1.33-2; Rickenmann, 2011
    tau_star_crit = 0.0495 #critical Shields stress, Wong and Parker (2005)
    phi = 0.3 #porosity

    h_baselevel = 0
    h_node = S * reach_length + h_baselevel
    chan_depth = h_floodplain - h_node #m; just some initial value
    
    ####RUN#####################################################################
    #set up time loop
    time = 0
    
    d_r = 0.01 #guess for depth incl. roughness; loop will adjust
    
    prior_w = 0
    prior_S = 0
    
    kill_flag = 0
    while kill_flag == 0 and time < time_to_run:
        
        #PART 1: HYDRAULICS
        
        #total flow resistance
        R_r, S_r, d_r, f_r_over_f = total_flow_resistance(Q, d_r, 
                                                                      wb, theta, 
                                                          a1, a2, sigma_z, 
                                                          g, S, chan_depth, 
                                                          e,
                                                          use_fp)
            
        #PART 2: BEDLOAD TRANSPORT
        shear_stress_r = rho_w * g * R_r * S_r
        shields_stress = shear_stress_r / ((rho_s - rho_w) * g * d50)
        
        #calc water surface width with roughness
        w_r = wb + 2 * (d_r / np.tan(theta))
        
        #calculate fc_bed and fc_bank
        if use_fp == 1:
            l_bank = 2 * (chan_depth / np.sin(theta))
        elif use_fp == 0:
            l_bank = 2 * (np.maximum(chan_depth, d_r) / np.sin(theta))
        
        fc_bed = np.minimum(l_bed_obstacle / wb, 1)
        fc_bank = np.minimum((2 * l_bank_obstacle) / l_bank, 1)
        fc_tot = (fc_bed * wb + fc_bank * l_bank) / (l_bank + wb)
        
        
        Qs_out = 3.97 * np.power((rho_s - rho_w) / rho_w, 1/2) * np.power(g, 1/2) * np.power(np.maximum(shields_stress - tau_star_crit, 0), 3/2) * np.power(d50, 3/2) * w_r * (1 - fc_tot)
        
        #PART 3: CALCULATION OF BANK AND BED SHEAR STRESSES
        
        #calc Fw
        Fw_tot = 1.766 * ((wb / (2 * d_r)) * np.sin(theta) + 1.5)**(-1.4026)
            
        #calc tau bank and bed
        tau_bank = shear_stress_r * (Fw_tot / 2) * ((wb / d_r) * np.sin(theta) + np.cos(theta))
        tau_bed = shear_stress_r * (1 - Fw_tot) * (1 + (d_r / (wb * np.tan(theta))))
        
        if (np.isnan(tau_bank) == True) or (np.isnan(tau_bed) == True):
            sys.exit('nan shear stress')
        if (tau_bed <=0) or (tau_bank <= 0):
            sys.exit('ERROR <=zero shear stress')
        

        #PART 4: CALCULATION OF BED AND BANK EROSION
        
        if fc_bed == 1:
            E_bed = 0
            D_bank = 0
        else:
            E_bed = (Qs_out / reach_length) * (1 / (((1 / k_ero) * (np.power(tau_bank, 3/2) / np.power(tau_bed, 3/2)) * ((1 - fc_bank) / (1 - fc_bed))) * l_bank + wb))
            D_bank = ((Qs_in) / reach_length) * (1 / (((k_dep) * (np.power(tau_bank, 3/2) / np.power(tau_bed, 3/2)) * ((1 - fc_bank) / (1 - fc_bed))) * wb + l_bank))

        if fc_bank == 1:
            E_bank = 0
            D_bed = 0
        else:
            E_bank = (Qs_out / reach_length) * (1 / (((k_ero) * (np.power(tau_bed, 3/2) / np.power(tau_bank, 3/2)) * ((1 - fc_bed) / (1 - fc_bank))) * wb + l_bank))
            D_bed = ((Qs_in) / reach_length) * (1 / (((1 / (k_dep)) * (np.power(tau_bed, 3/2) / np.power(tau_bank, 3/2)) * ((1 - fc_bed) / (1 - fc_bank))) * l_bank + wb))

        dh_bed = (D_bed - E_bed) / (1 - phi)
        dh_bank = (D_bank - E_bank) / (1 - phi)
        
        
        #PART 5: MORPHOLOGIC ADJUSTMENT TO BED AND BANK EROSION
        #update bed elevation
        h_node += (dh_bed * timestep)
        chan_depth = h_floodplain - h_node
        
        #update slope in response to new bed elevation assuming next node downstream maintains constant elevation
        S = (h_node - h_baselevel) / reach_length
        
        if S <= 0:
            sys.exit("failed: slope <= 0")
        
        #adjust basal width
        wb += (2 * ((-dh_bank / np.sin(theta)) - (-dh_bed / np.tan(theta))) * timestep)
        
        time += timestep
        
        if ((chan_depth <= 0) and use_fp == 1) or (np.isclose(chan_depth, 0, atol = 0.001, rtol = 0) and use_fp == 1):
            print('channel filled completely before max time')
            print(str(sigma_z) + ' // ' + str(l_bed_obstacle) + ' // ' + str(l_bank_obstacle))
            print(str(time) + '//' + str(time / 3.154e7))
            kill_flag = 1
            teq = time
        
        rtol = tolerance_over_timestep * timestep
        atol = 0
        if np.isclose(prior_w, wb, rtol = rtol, atol = atol) and np.isclose(prior_S, S, rtol = rtol, atol = atol):#check to see if width and slope are at steady state
            print('reached SS before max time')
            print(str(sigma_z) + ' // ' + str(l_bed_obstacle) + ' // ' + str(l_bank_obstacle))
            print(str(time) + '//' + str(time / 3.154e7))
            kill_flag = 1
            teq = time
            end_time = timer.time()
            print('Runtime: ' + str(end_time - start_time) + 'seconds')
        #else model should keep running
        else:
            prior_w = cp.deepcopy(wb)
            prior_S = cp.deepcopy(S)

    if kill_flag == 0:
        print('max time reached before SS')
        print(str(sigma_z) + ' // ' + str(l_bed_obstacle) + ' // ' + str(l_bank_obstacle))
        teq = -9999
        end_time = timer.time()
        print('Runtime: ' + str(end_time - start_time) + 'seconds')

    return (wb, d_r, S, S_r, tau_bed, tau_bank, f_r_over_f, teq)


def channel_evolution_trajectory(time_to_run,
         timestep,
         reach_length,
         Q,
         Qs_in,
         wb,
         theta,
         sigma_z,
         l_bed_obstacle,
         l_bank_obstacle,
         k_ero,
         k_dep,
         S,
         d50,
         h_floodplain,
         use_fp,
         print_interval,
         save_interval):
    
    #constants
    tolerance_over_timestep = 1e-13
    a1 = 6.5 #VPE constant
    a2 = 2.5 #VPE constant
    rho_w = 1000 #kg/m^3; water density
    rho_s = 2650 #kg/m^3, sed density
    g = 9.81 #m/s^2 accel due to gravity
    e = 1.5 #range of 1.33-2; Rickenmann, 2011
    tau_star_crit = 0.0495 #critical Shields stress, Wong and Parker (2005)
    phi = 0.3 #porosity

    h_baselevel = 0
    h_node = S * reach_length + h_baselevel
    chan_depth = h_floodplain - h_node #m; just some initial value
    ####RUN#####################################################################
    #set up time loop
    time = 0
    iter = 0
    
    d_r = 0.01 #guess for depth incl. roughness; loop will adjust

    save_widths = np.repeat(-99., int(time_to_run / save_interval) + 1)
    save_slopes = cp.deepcopy(save_widths)
    save_depths_r = cp.deepcopy(save_widths)
    save_qs_out = cp.deepcopy(save_widths)
    save_fw = cp.deepcopy(save_widths)
    save_tau_total = cp.deepcopy(save_widths)
    save_tau_bed = cp.deepcopy(save_widths)
    save_tau_bank = cp.deepcopy(save_widths)
    save_S_r = cp.deepcopy(save_widths)
    save_fr_over_f0 = cp.deepcopy(save_widths)
    save_chan_depths = cp.deepcopy(save_widths)


    save_widths[0] = wb
    save_slopes[0] = S
    save_depths_r[0] = 0
    save_qs_out[0] = 0
    save_fw[0] = 0
    save_tau_total[0] = 0
    save_tau_bed[0] = 0
    save_tau_bank[0] = 0
    save_S_r[0] = 0
    save_fr_over_f0[0] = 0
    save_chan_depths[0] = chan_depth

    prior_w = 0
    prior_S = 0
    
    kill_flag = 0
    while kill_flag == 0 and time < time_to_run:

        #PART 1: HYDRAULICS
        
        #total flow resistance
        R_r, S_r, d_r, f_r_over_f = total_flow_resistance(Q, d_r, 
                                                                      wb, theta, 
                                                          a1, a2, sigma_z, 
                                                          g, S, chan_depth, 
                                                          e,
                                                          use_fp)
        
        #PART 2: BEDLOAD TRANSPORT
        shear_stress_r = rho_w * g * R_r * S_r
        shields_stress = shear_stress_r / ((rho_s - rho_w) * g * d50)

        #calc water surface width with roughness
        w_r = wb + 2 * (d_r / np.tan(theta))
        
        #calculate fc_bed and fc_bank
        if use_fp == 1:
            l_bank = 2 * (chan_depth / np.sin(theta))
        elif use_fp == 0:
            l_bank = 2 * (np.maximum(chan_depth, d_r) / np.sin(theta))
        
        fc_bed = np.minimum(l_bed_obstacle / wb, 1)
        fc_bank = np.minimum((2 * l_bank_obstacle) / l_bank, 1)
        fc_tot = (fc_bed * wb + fc_bank * l_bank) / (l_bank + wb)
        
        
        Qs_out = 3.97 * np.power((rho_s - rho_w) / rho_w, 1/2) * np.power(g, 1/2) * np.power(np.maximum(shields_stress - tau_star_crit, 0), 3/2) * np.power(d50, 3/2) * w_r * (1 - fc_tot)

        #PART 3: CALCULATION OF BANK AND BED SHEAR STRESSES
        
        #calc Fw
        Fw_tot = 1.766 * ((wb / (2 * d_r)) * np.sin(theta) + 1.5)**(-1.4026)
        
        #calc tau bank and bed
        tau_bank = shear_stress_r * (Fw_tot / 2) * ((wb / d_r) * np.sin(theta) + np.cos(theta))
        tau_bed = shear_stress_r * (1 - Fw_tot) * (1 + (d_r / (wb * np.tan(theta))))
        
        if (np.isnan(tau_bank) == True) or (np.isnan(tau_bed) == True):
            sys.exit('nan shear stress')
        if (tau_bed <=0) or (tau_bank <= 0):
            sys.exit('ERROR <=zero shear stress')

        
        #PART 4: CALCULATION OF BED AND BANK EROSION
        
        if fc_bed == 1:
            E_bed = 0
            D_bank = 0
        else:
            E_bed = (Qs_out / reach_length) * (1 / (((1 / k_ero) * (np.power(tau_bank, 3/2) / np.power(tau_bed, 3/2)) * ((1 - fc_bank) / (1 - fc_bed))) * l_bank + wb))
            D_bank = ((Qs_in) / reach_length) * (1 / (((k_dep) * (np.power(tau_bank, 3/2) / np.power(tau_bed, 3/2)) * ((1 - fc_bank) / (1 - fc_bed))) * wb + l_bank))

        if fc_bank == 1:
            E_bank = 0
            D_bed = 0
        else:
            E_bank = (Qs_out / reach_length) * (1 / (((k_ero) * (np.power(tau_bed, 3/2) / np.power(tau_bank, 3/2)) * ((1 - fc_bed) / (1 - fc_bank))) * wb + l_bank))
            D_bed = ((Qs_in) / reach_length) * (1 / (((1 / (k_dep)) * (np.power(tau_bed, 3/2) / np.power(tau_bank, 3/2)) * ((1 - fc_bed) / (1 - fc_bank))) * l_bank + wb))

        dh_bed = (D_bed - E_bed) / (1 - phi)
        dh_bank = (D_bank - E_bank) / (1 - phi)
        
        #PART 5: MORPHOLOGIC ADJUSTMENT TO BED AND BANK EROSION
        #update bed elevation
        h_node += (dh_bed * timestep)
        chan_depth = h_floodplain - h_node
        
        #update slope in response to new bed elevation assuming next node downstream maintains constant elevation
        S = (h_node - h_baselevel) / reach_length
            
        if S <= 0:
            sys.exit("failed: slope <= 0")
    
        #adjust basal width
        wb += (2 * ((-dh_bank / np.sin(theta)) - (-dh_bed / np.tan(theta))) * timestep)
        
        time += timestep
        
        if (time % print_interval == 0) or (time == timestep):
            print('time = ' + str(time))
            print('depth = ' + str(d_r))
            print('h_floodplain = ' + str(h_floodplain))
            print('h_node = ' + str(h_node))
            print('chan_depth = ' + str(chan_depth))
            print('wb = ' + str(wb))
            print('slope = ' + str(S))
            print('tau_total = ' + str(shear_stress_r))
            print('tau_bed = ' + str(tau_bed))
            print('tau_bank = ' + str(tau_bank))
            print('fc_bed = ' + str(fc_bed))
            print('fc_bank = ' + str(fc_bank))
            print('fc_tot = ' + str(fc_tot))
            print('Qs_out = ' + str(Qs_out))
            print('Qs_in = ' + str(Qs_in))
            print('dQs = ' + str(Qs_out - Qs_in))
            print('dh_bed = ' + str(dh_bed))
            print('dh_bank = ' + str(dh_bank))
            print('---------------------')
            mass_bal_check = -(dh_bed * wb * (1 - phi)) - (dh_bank * l_bank * (1 - phi)) + (Qs_in / reach_length) - (Qs_out / reach_length)
            print('mass balance check: ' + str(mass_bal_check))
            print('---------------------')

        if time % save_interval == 0:
            iter += 1
            save_widths[iter] = wb
            save_slopes[iter] = S
            #save_depths[iter] = d
            save_depths_r[iter] = d_r
            save_qs_out[iter] = Qs_out
            save_fw[iter] = Fw_tot
            save_tau_total[iter] = shear_stress_r
            save_tau_bed[iter] = tau_bed
            save_tau_bank[iter] = tau_bank
            save_S_r[iter] = S_r
            save_fr_over_f0[iter] = f_r_over_f
            save_chan_depths[iter] = chan_depth
        
        if ((chan_depth <= 0) and use_fp == 1) or (np.isclose(chan_depth, 0, atol = 0.001, rtol = 0) and use_fp == 1):
            print('channel filled completely before max time')
            print(str(sigma_z) + ' // ' + str(l_bed_obstacle) + ' // ' + str(l_bank_obstacle))
            print(time)
            kill_flag = 1
            teq = time
        
        rtol = tolerance_over_timestep * timestep
        atol = 0
        if np.isclose(prior_w, wb, rtol = rtol, atol = atol) and np.isclose(prior_S, S, rtol = rtol, atol = atol):#check to see if width and slope are at steady state
            print('reached SS before max time')
            print(str(sigma_z) + ' // ' + str(l_bed_obstacle) + ' // ' + str(l_bank_obstacle))
            print(time)
            kill_flag = 1
            teq = time
        #else model should keep running
        else:
            prior_w = cp.deepcopy(wb)
            prior_S = cp.deepcopy(S)

    if kill_flag == 0:
        print('max time reached before SS')
        print(str(sigma_z) + ' // ' + str(l_bed_obstacle) + ' // ' + str(l_bank_obstacle))
        teq = -9999
    return (save_widths, save_slopes, save_depths_r, save_qs_out, 
            save_fw, save_tau_total, save_tau_bed, save_tau_bank, save_S_r, save_fr_over_f0,
            save_chan_depths, teq)

def channel_evolution_inversion(variable_args, *fixed_args):
    print('------------')
    
    k_ero = 10 ** variable_args[0] #NOTE THIS HAS BEEN LOGGED 
    k_dep = variable_args[1]
    print('k_ero: ' + str(k_ero))
    print('k_dep: ' + str(k_dep))
    
    
    time_to_run = fixed_args[0]
    timestep  = fixed_args[1]
    reach_length  = fixed_args[2]
    Q_time_series  = fixed_args[3]
    wb  = fixed_args[4]
    theta =  fixed_args[5]
    S = fixed_args[6]
    d50 = fixed_args[7]
    h_floodplain = fixed_args[8]
    use_fp = fixed_args[9]
    print_interval = fixed_args[10]
    save_interval = fixed_args[11]
    w_obs = fixed_args[12] #np array of len(3)
    h_obs = fixed_args[13] #np array of len(3)
    run_name = fixed_args[14]
    sigma_z_vals = fixed_args[15]
    l_bed_obst_vals = fixed_args[16]
    l_bank_obst_vals = fixed_args[17]
    
    sigma_z = sigma_z_vals[0]
    l_bed_obstacle = l_bed_obst_vals[0]
    l_bank_obstacle = l_bank_obst_vals[0]
    
    
    #constants that are not model parameters
    a1 = 6.5 #VPE constant
    a2 = 2.5 #VPE constant
    rho_w = 1000 #kg/m^3; water density
    rho_s = 2650 #kg/m^3, sed density
    g = 9.81 #m/s^2 accel due to gravity
    e = 1.5 #range of 1.33-2; Rickenmann, 2011
    tau_star_crit = 0.0495 #critical Shields stress, Wong and Parker (2005)
    phi = 0.3 #porosity
    
    h_baselevel = 0
    h_node = S * reach_length + h_baselevel
    chan_depth = h_floodplain - h_node #m; just some initial value
    ####RUN#####################################################################
    #set up time loop
    time = 0
    timestep_iter = 0
    iter = 0
    
    d = 0.01 #guess for depth w/o roughness; loop will adjust
    d_r = 0.01 #guess for depth incl. roughness; loop will adjust
    
    w_sim = np.zeros(3)
    h_sim = np.zeros(3)
    
    survey_time_2020 = 33264000 #seconds
    survey_time_2022 = 96163200 #seconds

    save_widths = np.repeat(-99., int(time_to_run / save_interval) + 1)
    save_slopes = cp.deepcopy(save_widths)
    save_depths = cp.deepcopy(save_widths)#np.ones(int(time_to_run / save_interval) + 1)
    save_depths_r = cp.deepcopy(save_widths)
    save_qs_out = cp.deepcopy(save_widths)
    save_fw = cp.deepcopy(save_widths)
    save_tau_bed = cp.deepcopy(save_widths)
    save_tau_bank = cp.deepcopy(save_widths)
    save_S_r = cp.deepcopy(save_widths)
    save_fr_over_f0 = cp.deepcopy(save_widths)
    save_chan_depths = cp.deepcopy(save_widths)


    save_widths[0] = wb
    save_slopes[0] = S
    save_depths[0] = 0
    save_depths_r[0] = 0
    save_qs_out[0] = 0
    save_fw[0] = 0
    save_tau_bed[0] = 0
    save_tau_bank[0] = 0
    save_S_r[0] = 0
    save_fr_over_f0[0] = 0
    save_chan_depths[0] = chan_depth
    
    kill_flag = 0
    while kill_flag == 0 and time < time_to_run:
        
        #get discharge from Q time series; allow repeats of the series
        if timestep_iter >= 1874223:
            timestep_iter = 0
        Q = Q_time_series[timestep_iter]
        Qs_in = 0.3 * 2.4e-6 * Q**2

        #PART 1: HYDRAULICS
        
        #total flow resistance
        R_r, S_r, d_r, f_r_over_f = total_flow_resistance(Q, d_r, 
                                                                      wb, theta, 
                                                          a1, a2, sigma_z, 
                                                          g, S, chan_depth, 
                                                          e,
                                                          use_fp)
        
        #PART 2: BEDLOAD TRANSPORT
        shear_stress_r = rho_w * g * R_r * S_r
        shields_stress = shear_stress_r / ((rho_s - rho_w) * g * d50)

        #calc water surface width with roughness
        w_r = wb + 2 * (d_r / np.tan(theta))
        
        #calculate fc_bed and fc_bank
        if use_fp == 1:
            l_bank = 2 * (chan_depth / np.sin(theta))
        elif use_fp == 0:
            l_bank = 2 * (np.maximum(chan_depth, d_r) / np.sin(theta))
        
        fc_bed = np.minimum(l_bed_obstacle / wb, 1)
        fc_bank = np.minimum((2 * l_bank_obstacle) / l_bank, 1)
        fc_tot = (fc_bed * wb + fc_bank * l_bank) / (l_bank + wb)
        
        
        Qs_out = 3.97 * np.power((rho_s - rho_w) / rho_w, 1/2) * np.power(g, 1/2) * np.power(np.maximum(shields_stress - tau_star_crit, 0), 3/2) * np.power(d50, 3/2) * w_r * (1 - fc_tot)

        #PART 3: CALCULATION OF BANK AND BED SHEAR STRESSES
        
        #calc Fw
        Fw_tot = 1.766 * ((wb / (2 * d_r)) * np.sin(theta) + 1.5)**(-1.4026)
        
        #calc tau bank and bed
        tau_bank = shear_stress_r * (Fw_tot / 2) * ((wb / d_r) * np.sin(theta) + np.cos(theta))
        tau_bed = shear_stress_r * (1 - Fw_tot) * (1 + (d_r / (wb * np.tan(theta))))
        
        if (np.isnan(tau_bank) == True) or (np.isnan(tau_bed) == True):
            sys.exit('nan shear stress')
        if (tau_bed <=0) or (tau_bank <= 0):
            sys.exit('ERROR <=zero shear stress')

        
        #PART 4: CALCULATION OF BED AND BANK EROSION
        
        if fc_bed == 1:
            E_bed = 0
            D_bank = 0
        else:
            E_bed = (Qs_out / reach_length) * (1 / (((1 / k_ero) * (np.power(tau_bank, 3/2) / np.power(tau_bed, 3/2)) * ((1 - fc_bank) / (1 - fc_bed))) * l_bank + wb))
            D_bank = ((Qs_in) / reach_length) * (1 / (((k_dep) * (np.power(tau_bank, 3/2) / np.power(tau_bed, 3/2)) * ((1 - fc_bank) / (1 - fc_bed))) * wb + l_bank))

        if fc_bank == 1:
            E_bank = 0
            D_bed = 0
        else:
            E_bank = (Qs_out / reach_length) * (1 / (((k_ero) * (np.power(tau_bed, 3/2) / np.power(tau_bank, 3/2)) * ((1 - fc_bed) / (1 - fc_bank))) * wb + l_bank))
            D_bed = ((Qs_in) / reach_length) * (1 / (((1 / (k_dep)) * (np.power(tau_bed, 3/2) / np.power(tau_bank, 3/2)) * ((1 - fc_bed) / (1 - fc_bank))) * l_bank + wb))

        dh_bed = (D_bed - E_bed) / (1 - phi)
        dh_bank = (D_bank - E_bank) / (1 - phi)
        
        
        #PART 5: MORPHOLOGIC ADJUSTMENT TO BED AND BANK EROSION
        #update bed elevation
        h_node += (dh_bed * timestep)
        chan_depth = h_floodplain - h_node
        
        #update slope in response to new bed elevation assuming next node downstream maintains constant elevation
        S = (h_node - h_baselevel) / reach_length
            
        if S <= 0:
            sys.exit("failed: slope <= 0")
    
        #adjust basal width
        wb += (2 * ((-dh_bank / np.sin(theta)) - (-dh_bed / np.tan(theta))) * timestep)
        
        time += timestep
        timestep_iter += 1
        
        if time % print_interval == 0:
            #iter += 1
            print('time = ' + str(time))
            #print(time / 3.154e7)
            #print('discharge = ' + str(Q))
            
        if time == survey_time_2020:
            w_sim[0] = wb
            h_sim[0] = h_node
            sigma_z = sigma_z_vals[1]
            l_bed_obstacle = l_bed_obst_vals[1]
            l_bank_obstacle = l_bank_obst_vals[1]
            
        if time == survey_time_2022:
            w_sim[1] = wb
            h_sim[1] = h_node
            sigma_z = sigma_z_vals[2]
            l_bed_obstacle = l_bed_obst_vals[2]
            l_bank_obstacle = l_bank_obst_vals[2]


        if time % save_interval == 0:
            iter += 1
            save_widths[iter] = wb
            save_slopes[iter] = S
            save_depths[iter] = d
            save_depths_r[iter] = d_r
            save_qs_out[iter] = Qs_out
            save_fw[iter] = Fw_tot
            save_tau_bed[iter] = tau_bed
            save_tau_bank[iter] = tau_bank
            save_S_r[iter] = S_r
            save_fr_over_f0[iter] = f_r_over_f
            save_chan_depths[iter] = chan_depth
        
        if (chan_depth <= 0) or np.isclose(chan_depth, 0, atol = 0.001, rtol = 0):
            print('channel filled completely before max time')
            print(str(sigma_z) + ' // ' + str(l_bed_obstacle) + ' // ' + str(l_bank_obstacle))
            print(time)
            kill_flag = 1

    if kill_flag == 0:
        w_sim[2] = wb
        h_sim[2] = h_node
        print('max time reached before SS')
        print(str(sigma_z) + ' // ' + str(l_bed_obstacle) + ' // ' + str(l_bank_obstacle))
        
    #calculate misfit function
    
    width_uncertainty = 5 #m
    bed_elev_uncertainty = 0.1 #m
    
    weight_on_width = 1. #0 for all weight on slope, 1 for all on width
    
    misfit = (weight_on_width) * (1 / 3) * np.sqrt(np.power(np.sum(w_obs - w_sim), 2) / np.power(width_uncertainty, 2)) + (1 - weight_on_width) * (1 / 3) * np.sqrt(np.power(np.sum(h_obs - h_sim), 2) / np.power(bed_elev_uncertainty, 2))
    print('misfit: ' + str(misfit))
    end_time = timer.time()
    print ('runtime: ' + str((end_time - start_time) / 60) + 'minutes')
    
    data = [k_ero, k_dep, misfit]
    
    with open('results/' + str(run_name) + '_inversion_record.csv', 'a', newline = '\n') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(data)
    
    return misfit

def channel_evolution_bestfit(time_to_run,
         timestep,
         reach_length,
         Q_time_series,
         wb,
         theta,
         k_ero,
         k_dep,
         S,
         d50,
         h_floodplain,
         use_fp,
         print_interval,
         save_interval,
         sigma_z_vals,
         l_bed_obst_vals,
         l_bank_obst_vals):
    
    sigma_z = sigma_z_vals[0]
    l_bed_obstacle = l_bed_obst_vals[0]
    l_bank_obstacle = l_bank_obst_vals[0]
    
    #constants
    a1 = 6.5 #VPE constant
    a2 = 2.5 #VPE constant
    rho_w = 1000 #kg/m^3; water density
    rho_s = 2650 #kg/m^3, sed density
    g = 9.81 #m/s^2 accel due to gravity
    e = 1.5 #range of 1.33-2; Rickenmann, 2011
    tau_star_crit = 0.0495 #critical Shields stress, Wong and Parker (2005)
    phi = 0.3 #porosity
    
    h_baselevel = 0
    h_node = S * reach_length + h_baselevel
    chan_depth = h_floodplain - h_node #m; just some initial value
    ####RUN#####################################################################
    #set up time loop
    time = 0
    timestep_iter = 0
    iter = 0
    
    d_r = 0.01 #guess for depth incl. roughness; loop will adjust
    
    survey_time_2020 = 33264000 #seconds
    survey_time_2022 = 96163200 #seconds

    save_widths = np.repeat(-99., int(time_to_run / save_interval) + 1)
    save_slopes = cp.deepcopy(save_widths)
    save_depths_r = cp.deepcopy(save_widths)
    save_qs_out = cp.deepcopy(save_widths)
    save_fw = cp.deepcopy(save_widths)
    save_tau_bed = cp.deepcopy(save_widths)
    save_tau_bank = cp.deepcopy(save_widths)
    save_S_r = cp.deepcopy(save_widths)
    save_fr_over_f0 = cp.deepcopy(save_widths)
    save_chan_depths = cp.deepcopy(save_widths)

    save_widths[0] = wb
    save_slopes[0] = S
    save_depths_r[0] = 0
    save_qs_out[0] = 0
    save_fw[0] = 0
    save_tau_bed[0] = 0
    save_tau_bank[0] = 0
    save_S_r[0] = 0
    save_fr_over_f0[0] = 0
    save_chan_depths[0] = chan_depth
    
    kill_flag = 0
    while kill_flag == 0 and time < time_to_run:
        
        #get discharge from Q time series; allow repeats of the series
        if timestep_iter >= 1874223:
            timestep_iter = 0
        Q = Q_time_series[timestep_iter]
        Qs_in = 0.3 * 2.4e-6 * Q**2
            

        #PART 1: HYDRAULICS
        
        #total flow resistance
        R_r, S_r, d_r, f_r_over_f = total_flow_resistance(Q, d_r, 
                                                                      wb, theta, 
                                                          a1, a2, sigma_z, 
                                                          g, S, chan_depth, 
                                                          e,
                                                          use_fp)
        
        #PART 2: BEDLOAD TRANSPORT
        shear_stress_r = rho_w * g * R_r * S_r
        shields_stress = shear_stress_r / ((rho_s - rho_w) * g * d50)

        #calc water surface width with roughness
        w_r = wb + 2 * (d_r / np.tan(theta))
        
        #calculate fc_bed and fc_bank
        if use_fp == 1:
            l_bank = 2 * (chan_depth / np.sin(theta))
        elif use_fp == 0:
            l_bank = 2 * (np.maximum(chan_depth, d_r) / np.sin(theta))
        
        fc_bed = np.minimum(l_bed_obstacle / wb, 1)
        fc_bank = np.minimum((2 * l_bank_obstacle) / l_bank, 1)
        fc_tot = (fc_bed * wb + fc_bank * l_bank) / (l_bank + wb)
        
        
        Qs_out = 3.97 * np.power((rho_s - rho_w) / rho_w, 1/2) * np.power(g, 1/2) * np.power(np.maximum(shields_stress - tau_star_crit, 0), 3/2) * np.power(d50, 3/2) * w_r * (1 - fc_tot)

        #PART 3: CALCULATION OF BANK AND BED SHEAR STRESSES
        
        #calc Fw
        Fw_tot = 1.766 * ((wb / (2 * d_r)) * np.sin(theta) + 1.5)**(-1.4026)
        
        #calc tau bank and bed
        tau_bank = shear_stress_r * (Fw_tot / 2) * ((wb / d_r) * np.sin(theta) + np.cos(theta))
        tau_bed = shear_stress_r * (1 - Fw_tot) * (1 + (d_r / (wb * np.tan(theta))))
        
        if (np.isnan(tau_bank) == True) or (np.isnan(tau_bed) == True):
            sys.exit('nan shear stress')
        if (tau_bed <=0) or (tau_bank <= 0):
            sys.exit('ERROR <=zero shear stress')

        
        #PART 4: CALCULATION OF BED AND BANK EROSION
        
        if fc_bed == 1:
            E_bed = 0
            D_bank = 0
        else:
            E_bed = (Qs_out / reach_length) * (1 / (((1 / k_ero) * (np.power(tau_bank, 3/2) / np.power(tau_bed, 3/2)) * ((1 - fc_bank) / (1 - fc_bed))) * l_bank + wb))
            D_bank = ((Qs_in) / reach_length) * (1 / (((k_dep) * (np.power(tau_bank, 3/2) / np.power(tau_bed, 3/2)) * ((1 - fc_bank) / (1 - fc_bed))) * wb + l_bank))

        if fc_bank == 1:
            E_bank = 0
            D_bed = 0
        else:
            E_bank = (Qs_out / reach_length) * (1 / (((k_ero) * (np.power(tau_bed, 3/2) / np.power(tau_bank, 3/2)) * ((1 - fc_bed) / (1 - fc_bank))) * wb + l_bank))
            D_bed = ((Qs_in) / reach_length) * (1 / (((1 / (k_dep)) * (np.power(tau_bed, 3/2) / np.power(tau_bank, 3/2)) * ((1 - fc_bed) / (1 - fc_bank))) * l_bank + wb))

        dh_bed = (D_bed - E_bed) / (1 - phi)
        dh_bank = (D_bank - E_bank) / (1 - phi)
        
        #PART 5: MORPHOLOGIC ADJUSTMENT TO BED AND BANK EROSION
        #update bed elevation
        h_node += (dh_bed * timestep)
        chan_depth = h_floodplain - h_node
        
        #update slope in response to new bed elevation assuming next node downstream maintains constant elevation
        S = (h_node - h_baselevel) / reach_length
            
        if S <= 0:
            sys.exit("failed: slope <= 0")
    
        #adjust basal width
        wb += (2 * ((-dh_bank / np.sin(theta)) - (-dh_bed / np.tan(theta))) * timestep)
        
        time += timestep
        timestep_iter += 1
        
        if time % print_interval == 0:
            #iter += 1
            print('time = ' + str(time))
            #print(time / 3.154e7)
            #print(str(wb))
            #print(str(d_r))
            #print(str(chan_depth))
            #print(str(S))
            
        if time == survey_time_2020:
            sigma_z = sigma_z_vals[1]
            l_bed_obstacle = l_bed_obst_vals[1]
            l_bank_obstacle = l_bank_obst_vals[1]
            
        if time == survey_time_2022:
            sigma_z = sigma_z_vals[2]
            l_bed_obstacle = l_bed_obst_vals[2]
            l_bank_obstacle = l_bank_obst_vals[2]


        if time % save_interval == 0:
            iter += 1
            save_widths[iter] = wb
            save_slopes[iter] = S
            save_depths_r[iter] = d_r
            save_qs_out[iter] = Qs_out
            save_fw[iter] = Fw_tot
            save_tau_bed[iter] = tau_bed
            save_tau_bank[iter] = tau_bank
            save_S_r[iter] = S_r
            save_fr_over_f0[iter] = f_r_over_f
            save_chan_depths[iter] = chan_depth
        
        if (chan_depth <= 0) or np.isclose(chan_depth, 0, atol = 0.001, rtol = 0):
            print('channel filled completely before max time')
            print(str(sigma_z) + ' // ' + str(l_bed_obstacle) + ' // ' + str(l_bank_obstacle))
            print(time)
            kill_flag = 1
            teq = time

    if kill_flag == 0:
        print('max time reached before SS')
        print(str(sigma_z) + ' // ' + str(l_bed_obstacle) + ' // ' + str(l_bank_obstacle))
        teq = -9999
    return (save_widths, save_slopes, save_depths_r, save_qs_out, 
            save_fw,save_tau_bed, save_tau_bank, save_S_r, save_fr_over_f0,
            save_chan_depths, teq)

