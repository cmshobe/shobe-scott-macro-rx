#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 9 Jan 2025

@author: charlesshobe

VERSION 9!! PARALLEL
-this is version 5 but with dynamic depth (= version 7)
-but then modified to get hydraulics right!

0-D morphodynamic model for wood-influenced rivers
refactored for easier use in studying parameter sensitivity
"""
import sys
import numpy as np
import copy as cp
import numba as nb

@nb.jit(nb.types.Tuple((nb.float64, nb.float64))(nb.float64, nb.float64,
                                                 nb.float64, nb.float64,
                                                 nb.float64, nb.float64,
                                                 nb.float64, nb.float64,
                                                 nb.float64, nb.int8),nopython=True)
def base_flow_resistance(Q, d, wb, theta, a1, sigma_z, g, S, chan_depth,
                         use_fp):
    calc_Q = 0
    while np.isclose(calc_Q, Q, rtol=1e-3) == False: 
        
        #while we haven't converged on a no-roughness depth that yields the correct discharge value...
        if calc_Q < Q:
            d += 1e-5
        elif calc_Q > Q:
            d -= 1e-5
        
        #break up numerical solution into component terms so it isn't so crazy
        width_area_term = wb + d / np.tan(theta) #this is hard to explain: it's the term that gets multiplied by depth to give XS area. It's wb + d/tan(theta)
        
        #cross-sectional area term
        xs_area = width_area_term * d #xs area of flow incl. wood roughness
        
        #wetted perimeter
        wp = wb + 2 * (d / np.sin(theta))
        
        #hydraulic radius
        R = xs_area / wp
        
        #Manning-strickler baselevel roughness term
        manning_strickler_term = a1 * np.power(R / sigma_z, 1 / 6)
          
        #square root term
        sqrt_term = np.power(g * R * S, 1/2)
        
        #finally, calculate discharge as product of the three terms
        calc_Q = xs_area * manning_strickler_term * sqrt_term

    if (d > chan_depth) and (use_fp == 1): #if flow is going overbank...
        calc_Q = Q #trip the flag to stop accruing depth
        d = chan_depth
        
        #break up numerical solution into component terms so it isn't so crazy
        width_area_term = wb + d / np.tan(theta) #this is hard to explain: it's the term that gets multiplied by depth to give XS area. It's wb + d/tan(theta)
        
        #cross-sectional area term
        xs_area = width_area_term * d #xs area of flow incl. wood roughness
        
        #wetted perimeter
        wp = wb + 2 * (d / np.sin(theta))
        
        #hydraulic radius
        R = xs_area / wp
        
        #Manning-strickler baselevel roughness term
        manning_strickler_term = a1 * np.power(R / sigma_z, 1 / 6)
          
        #square root term
        sqrt_term = np.power(g * R * S, 1/2)
            
    return manning_strickler_term, d


@nb.jit(nb.types.Tuple((nb.float64, nb.float64, nb.float64, nb.float64))(nb.float64, nb.float64,
                                                 nb.float64, nb.float64,
                                                 nb.float64, nb.float64,
                                                 nb.float64, nb.float64,
                                                 nb.float64, nb.float64,
                                                 nb.float64, nb.float64,
                                                 nb.int8),nopython=True)
def total_flow_resistance(Q, d_r, wb, theta, a1, a2, sigma_z, g, S, chan_depth,
                         manning_strickler_term, e, use_fp):
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
        sqrt_f_over_f_r = VPE_term / manning_strickler_term
        
        
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
        sqrt_f_over_f_r = VPE_term / manning_strickler_term
        
        
        #calculate f_r / f for comparison with field studies (Follett and Wohl, etc)
        f_r_over_f = 1 / np.power(sqrt_f_over_f_r, 2)
        
        S_r = S * np.power(sqrt_f_over_f_r, e) #* np.power(d / d_r, e / 6)
        
    return R_r, S_r, d_r, f_r_over_f


def channel_evolution(time_to_run,
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
    
    
    
    #constants that are not model parameters
    tolerance_over_timestep = 2e-11
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
    #iter = 0
    
    d = 0.01 #guess for depth w/o roughness; loop will adjust
    d_r = 0.01 #guess for depth incl. roughness; loop will adjust
    
    #save_widths = np.zeros(int(time_to_run / timestep) + 1)
    #save_slopes = cp.deepcopy(save_widths)
    #save_depths = cp.deepcopy(save_widths)
    #save_depths_r = cp.deepcopy(save_widths)
    #save_qs_out = cp.deepcopy(save_widths)
    #save_tau_bed = cp.deepcopy(save_widths)
    #save_tau_bank = cp.deepcopy(save_widths)
    #save_S_r = cp.deepcopy(save_widths)
    #save_fr_over_f0 = cp.deepcopy(save_widths)


    #save_widths[0] = wb
    #save_slopes[0] = S
    #save_depths[0] = 0
    #save_depths_r[0] = 0
    #save_qs_out[0] = 0
    #save_tau_bed[0] = 0
    #save_tau_bank[0] = 0
    #save_S_r[0] = 0
    #save_fr_over_f0[0] = 0
    
    
    
    
    
    prior_w = 0
    prior_S = 0
    
    kill_flag = 0
    while kill_flag == 0 and time < time_to_run:
        
        #PART 1: HYDRAULICS
        #base-level flow resistance
        manning_strickler_term, d = base_flow_resistance(Q, d, wb, theta, a1, 
                                                         sigma_z, g, S, chan_depth,
                                                         use_fp)
        
        if np.isnan(manning_strickler_term) == True:
            print(time)
            print(chan_depth)
            print(d)
            sys.exit('MANNING term is nan')
        
        #total flow resistance
        R_r, S_r, d_r, f_r_over_f = total_flow_resistance(Q, d_r, 
                                                                      wb, theta, 
                                                          a1, a2, sigma_z, 
                                                          g, S, chan_depth, 
                                                          manning_strickler_term, 
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
        
        #instead of distinguishing net erosion and net deposition...
        if fc_bed == 1:
            E_bed = 0
        else:
            E_bed = (Qs_out / reach_length) * (1 / (((1 / k_ero) * (np.power(tau_bank, 3/2) / np.power(tau_bed, 3/2)) * ((1 - fc_bank) / (1 - fc_bed))) * l_bank + wb))
        
        if fc_bank == 1:
            E_bank = 0
        else:
            E_bank = (Qs_out / reach_length) * (1 / (((k_ero) * (np.power(tau_bed, 3/2) / np.power(tau_bank, 3/2)) * ((1 - fc_bed) / (1 - fc_bank))) * wb + l_bank))
        
        if fc_bank == 1:
            D_bed = 0
        else:
            D_bed = ((Qs_in) / reach_length) * (1 / (((1 / (k_dep)) * (np.power(tau_bed, 3/2) / np.power(tau_bank, 3/2)) * ((1 - fc_bed) / (1 - fc_bank))) * l_bank + wb))
        
        if fc_bed == 1:
            D_bank = 0
        else:
            D_bank = ((Qs_in) / reach_length) * (1 / (((k_dep) * (np.power(tau_bank, 3/2) / np.power(tau_bed, 3/2)) * ((1 - fc_bank) / (1 - fc_bed))) * wb + l_bank))
        
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
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        if (chan_depth <= 0) or np.isclose(chan_depth, 0, atol = 0.001, rtol = 0):
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
        #else model should keep running
        else:
            prior_w = cp.deepcopy(wb)
            prior_S = cp.deepcopy(S)

    if kill_flag == 0:
        print('max time reached before SS')
        print(str(sigma_z) + ' // ' + str(l_bed_obstacle) + ' // ' + str(l_bank_obstacle))
        teq = -9999
    return (wb, d_r, S, S_r, tau_bed, tau_bank, f_r_over_f, teq)
