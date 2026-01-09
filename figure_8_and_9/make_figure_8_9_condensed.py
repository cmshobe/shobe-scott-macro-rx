#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 21:44:08 2025

@author: charlesshobe

Create results figure: outputs w, d, S+Sr,  and f/fr as f(sigma_z)
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

#######IMPORT BASELINE DATA FOR NORMALIZATION
run_name = 'trajectory_z0_baseline_rev1'
baseline_widths = np.load('results/' + str(run_name) + '_widths.npy')
baseline_depths = np.load('results/' + str(run_name) + '_depths_r.npy')
baseline_slopes = np.load('results/' + str(run_name) + '_slopes.npy')
#baseline_e_slopes = np.load('results/' + str(run_name) + '_e_slopes.npy')
#baseline_tau_bed = np.load('results/' + str(run_name) + '_tau_bed.npy')
#baseline_tau_bank = np.load('results/' + str(run_name) + '_tau_bank.npy')
#baseline_fr_over_f0 = np.load('results/' + str(run_name) + '_fr_over_f0.npy')
#baseline_qs_out = np.load('results/' + str(run_name) + '_qs_out.npy')


#######IMPORT NON-DEPTH-CONSTRAINED DATA
run_name = 'trajectory_rev1_z0_0point1_L1000_tol1e-13_dt1000'
sigma_z_nofp_1_widths = np.load('results/' + str(run_name) + '_widths.npy')
sigma_z_nofp_1_depths = np.load('results/' + str(run_name) + '_depths_r.npy')
sigma_z_nofp_1_slopes = np.load('results/' + str(run_name) + '_slopes.npy')
#sigma_z_nofp_1_e_slopes = np.load('results/' + str(run_name) + '_e_slopes.npy')
#sigma_z_nofp_1_tau_bed = np.load('results/' + str(run_name) + '_tau_bed.npy')
#sigma_z_nofp_1_tau_bank = np.load('results/' + str(run_name) + '_tau_bank.npy')
#sigma_z_nofp_1_fr_over_f0 = np.load('results/' + str(run_name) + '_fr_over_f0.npy')
#sigma_z_nofp_1_qs_out = np.load('results/' + str(run_name) + '_qs_out.npy')

run_name = 'trajectory_rev1_z0_0point25_L1000_tol1e-13_dt1000'
sigma_z_nofp_2_widths = np.load('results/' + str(run_name) + '_widths.npy')
sigma_z_nofp_2_depths = np.load('results/' + str(run_name) + '_depths_r.npy')
sigma_z_nofp_2_slopes = np.load('results/' + str(run_name) + '_slopes.npy')
#sigma_z_nofp_2_e_slopes = np.load('results/' + str(run_name) + '_e_slopes.npy')
#sigma_z_nofp_2_tau_bed = np.load('results/' + str(run_name) + '_tau_bed.npy')
#sigma_z_nofp_2_tau_bank = np.load('results/' + str(run_name) + '_tau_bank.npy')
#sigma_z_nofp_2_fr_over_f0 = np.load('results/' + str(run_name) + '_fr_over_f0.npy')
#sigma_z_nofp_2_qs_out = np.load('results/' + str(run_name) + '_qs_out.npy')


run_name = 'trajectory_rev1_z0_0point5_L1000_tol1e-13_dt1000'
sigma_z_nofp_3_widths = np.load('results/' + str(run_name) + '_widths.npy')
sigma_z_nofp_3_depths = np.load('results/' + str(run_name) + '_depths_r.npy')
sigma_z_nofp_3_slopes = np.load('results/' + str(run_name) + '_slopes.npy')
#sigma_z_nofp_3_e_slopes = np.load('results/' + str(run_name) + '_e_slopes.npy')
#sigma_z_nofp_3_tau_bed = np.load('results/' + str(run_name) + '_tau_bed.npy')
#sigma_z_nofp_3_tau_bank = np.load('results/' + str(run_name) + '_tau_bank.npy')
#sigma_z_nofp_3_fr_over_f0 = np.load('results/' + str(run_name) + '_fr_over_f0.npy')
#sigma_z_nofp_3_qs_out = np.load('results/' + str(run_name) + '_qs_out.npy')

run_name = 'trajectory_rev1_z0_1_L1000_tol1e-13_dt1000'
sigma_z_nofp_4_widths = np.load('results/' + str(run_name) + '_widths.npy')
sigma_z_nofp_4_depths = np.load('results/' + str(run_name) + '_depths_r.npy')
sigma_z_nofp_4_slopes = np.load('results/' + str(run_name) + '_slopes.npy')
#sigma_z_nofp_4_e_slopes = np.load('results/' + str(run_name) + '_e_slopes.npy')
#sigma_z_nofp_4_tau_bed = np.load('results/' + str(run_name) + '_tau_bed.npy')
#sigma_z_nofp_4_tau_bank = np.load('results/' + str(run_name) + '_tau_bank.npy')
#sigma_z_nofp_4_fr_over_f0 = np.load('results/' + str(run_name) + '_fr_over_f0.npy')
#sigma_z_nofp_4_qs_out = np.load('results/' + str(run_name) + '_qs_out.npy')

run_name = 'trajectory_rev1_z0_2point5_L1000_tol1e-13_dt1000'
sigma_z_nofp_5_widths = np.load('results/' + str(run_name) + '_widths.npy')
sigma_z_nofp_5_depths = np.load('results/' + str(run_name) + '_depths_r.npy')
sigma_z_nofp_5_slopes = np.load('results/' + str(run_name) + '_slopes.npy')
#sigma_z_nofp_5_e_slopes = np.load('results/' + str(run_name) + '_e_slopes.npy')
#sigma_z_nofp_5_tau_bed = np.load('results/' + str(run_name) + '_tau_bed.npy')
#sigma_z_nofp_5_tau_bank = np.load('results/' + str(run_name) + '_tau_bank.npy')
#sigma_z_nofp_5_fr_over_f0 = np.load('results/' + str(run_name) + '_fr_over_f0.npy')
#sigma_z_nofp_5_qs_out = np.load('results/' + str(run_name) + '_qs_out.npy')

run_name = 'trajectory_rev1_z0_5_L1000_tol1e-13_dt1000'
sigma_z_nofp_6_widths = np.load('results/' + str(run_name) + '_widths.npy')
sigma_z_nofp_6_depths = np.load('results/' + str(run_name) + '_depths_r.npy')
sigma_z_nofp_6_slopes = np.load('results/' + str(run_name) + '_slopes.npy')
#sigma_z_nofp_6_e_slopes = np.load('results/' + str(run_name) + '_e_slopes.npy')
#sigma_z_nofp_6_tau_bed = np.load('results/' + str(run_name) + '_tau_bed.npy')
#sigma_z_nofp_6_tau_bank = np.load('results/' + str(run_name) + '_tau_bank.npy')
#sigma_z_nofp_6_fr_over_f0 = np.load('results/' + str(run_name) + '_fr_over_f0.npy')
#sigma_z_nofp_6_qs_out = np.load('results/' + str(run_name) + '_qs_out.npy')

run_name = 'trajectory_rev1_z0_10_L1000_tol1e-13_dt1000'
sigma_z_nofp_7_widths = np.load('results/' + str(run_name) + '_widths.npy')
sigma_z_nofp_7_depths = np.load('results/' + str(run_name) + '_depths_r.npy')
sigma_z_nofp_7_slopes = np.load('results/' + str(run_name) + '_slopes.npy')
#sigma_z_nofp_7_e_slopes = np.load('results/' + str(run_name) + '_e_slopes.npy')
#sigma_z_nofp_7_tau_bed = np.load('results/' + str(run_name) + '_tau_bed.npy')
#sigma_z_nofp_7_tau_bank = np.load('results/' + str(run_name) + '_tau_bank.npy')
#sigma_z_nofp_7_fr_over_f0 = np.load('results/' + str(run_name) + '_fr_over_f0.npy')
#sigma_z_nofp_7_qs_out = np.load('results/' + str(run_name) + '_qs_out.npy')

#######IMPORT DEPTH-CONSTRAINED DATA (HFP = 3 M)

run_name = 'trajectory_rev1_fp_z0_0point1_L1000_tol1e-13_dt1000'
sigma_z_1_widths = np.load('results/' + str(run_name) + '_widths.npy')
sigma_z_1_depths = np.load('results/' + str(run_name) + '_depths_r.npy')
sigma_z_1_slopes = np.load('results/' + str(run_name) + '_slopes.npy')
#sigma_z_1_e_slopes = np.load('results/' + str(run_name) + '_e_slopes.npy')
#sigma_z_1_tau_bed = np.load('results/' + str(run_name) + '_tau_bed.npy')
#sigma_z_1_tau_bank = np.load('results/' + str(run_name) + '_tau_bank.npy')
#sigma_z_1_fr_over_f0 = np.load('results/' + str(run_name) + '_fr_over_f0.npy')
#sigma_z_1_qs_out = np.load('results/' + str(run_name) + '_qs_out.npy')

run_name = 'trajectory_rev1_fp_z0_0point25_L1000_tol1e-13_dt1000'
sigma_z_2_widths = np.load('results/' + str(run_name) + '_widths.npy')
sigma_z_2_depths = np.load('results/' + str(run_name) + '_depths_r.npy')
sigma_z_2_slopes = np.load('results/' + str(run_name) + '_slopes.npy')
#sigma_z_2_e_slopes = np.load('results/' + str(run_name) + '_e_slopes.npy')
#sigma_z_2_tau_bed = np.load('results/' + str(run_name) + '_tau_bed.npy')
#sigma_z_2_tau_bank = np.load('results/' + str(run_name) + '_tau_bank.npy')
#sigma_z_2_fr_over_f0 = np.load('results/' + str(run_name) + '_fr_over_f0.npy')
#sigma_z_2_qs_out = np.load('results/' + str(run_name) + '_qs_out.npy')

run_name = 'trajectory_rev1_fp_z0_0point5_L1000_tol1e-13_dt1000'
sigma_z_3_widths = np.load('results/' + str(run_name) + '_widths.npy')
sigma_z_3_depths = np.load('results/' + str(run_name) + '_depths_r.npy')
sigma_z_3_slopes = np.load('results/' + str(run_name) + '_slopes.npy')
#sigma_z_3_e_slopes = np.load('results/' + str(run_name) + '_e_slopes.npy')
#sigma_z_3_tau_bed = np.load('results/' + str(run_name) + '_tau_bed.npy')
#sigma_z_3_tau_bank = np.load('results/' + str(run_name) + '_tau_bank.npy')
#sigma_z_3_fr_over_f0 = np.load('results/' + str(run_name) + '_fr_over_f0.npy')
#sigma_z_3_qs_out = np.load('results/' + str(run_name) + '_qs_out.npy')

run_name = 'trajectory_rev1_fp_z0_1_L1000_tol1e-13_dt1000'
sigma_z_4_widths = np.load('results/' + str(run_name) + '_widths.npy')
sigma_z_4_depths = np.load('results/' + str(run_name) + '_depths_r.npy')
sigma_z_4_slopes = np.load('results/' + str(run_name) + '_slopes.npy')
#sigma_z_4_e_slopes = np.load('results/' + str(run_name) + '_e_slopes.npy')
#sigma_z_4_tau_bed = np.load('results/' + str(run_name) + '_tau_bed.npy')
#sigma_z_4_tau_bank = np.load('results/' + str(run_name) + '_tau_bank.npy')
#sigma_z_4_fr_over_f0 = np.load('results/' + str(run_name) + '_fr_over_f0.npy')
#sigma_z_4_qs_out = np.load('results/' + str(run_name) + '_qs_out.npy')

run_name = 'trajectory_rev1_fp_z0_2point5_L1000_tol1e-13_dt1000'
sigma_z_5_widths = np.load('results/' + str(run_name) + '_widths.npy')
sigma_z_5_depths = np.load('results/' + str(run_name) + '_depths_r.npy')
sigma_z_5_slopes = np.load('results/' + str(run_name) + '_slopes.npy')
#sigma_z_5_e_slopes = np.load('results/' + str(run_name) + '_e_slopes.npy')
#sigma_z_5_tau_bed = np.load('results/' + str(run_name) + '_tau_bed.npy')
#sigma_z_5_tau_bank = np.load('results/' + str(run_name) + '_tau_bank.npy')
#sigma_z_5_fr_over_f0 = np.load('results/' + str(run_name) + '_fr_over_f0.npy')
#sigma_z_5_qs_out = np.load('results/' + str(run_name) + '_qs_out.npy')

run_name = 'trajectory_rev1_fp_z0_5_L1000_tol1e-13_dt1000'
sigma_z_6_widths = np.load('results/' + str(run_name) + '_widths.npy')
sigma_z_6_depths = np.load('results/' + str(run_name) + '_depths_r.npy')
sigma_z_6_slopes = np.load('results/' + str(run_name) + '_slopes.npy')
#sigma_z_6_e_slopes = np.load('results/' + str(run_name) + '_e_slopes.npy')
#sigma_z_6_tau_bed = np.load('results/' + str(run_name) + '_tau_bed.npy')
#sigma_z_6_tau_bank = np.load('results/' + str(run_name) + '_tau_bank.npy')
#sigma_z_6_fr_over_f0 = np.load('results/' + str(run_name) + '_fr_over_f0.npy')
#sigma_z_6_qs_out = np.load('results/' + str(run_name) + '_qs_out.npy')

run_name = 'trajectory_rev1_fp_z0_10_L1000_tol1e-13_dt1000'
sigma_z_7_widths = np.load('results/' + str(run_name) + '_widths.npy')
sigma_z_7_depths = np.load('results/' + str(run_name) + '_depths_r.npy')
sigma_z_7_slopes = np.load('results/' + str(run_name) + '_slopes.npy')
#sigma_z_7_e_slopes = np.load('results/' + str(run_name) + '_e_slopes.npy')
#sigma_z_7_tau_bed = np.load('results/' + str(run_name) + '_tau_bed.npy')
#sigma_z_7_tau_bank = np.load('results/' + str(run_name) + '_tau_bank.npy')
#sigma_z_7_fr_over_f0 = np.load('results/' + str(run_name) + '_fr_over_f0.npy')
#sigma_z_7_qs_out = np.load('results/' + str(run_name) + '_qs_out.npy')
##############################################################################

#get timenormalization info
baseline_final_index = np.where(baseline_widths > 0)[0][-1]

sigma_z_nofp_1_final_index = np.where(sigma_z_nofp_1_widths > 0)[0][-1]
sigma_z_nofp_2_final_index = np.where(sigma_z_nofp_2_widths > 0)[0][-1]
sigma_z_nofp_3_final_index = np.where(sigma_z_nofp_3_widths > 0)[0][-1]
sigma_z_nofp_4_final_index = np.where(sigma_z_nofp_4_widths > 0)[0][-1]
sigma_z_nofp_5_final_index = np.where(sigma_z_nofp_5_widths > 0)[0][-1]
sigma_z_nofp_6_final_index = np.where(sigma_z_nofp_6_widths > 0)[0][-1]
sigma_z_nofp_7_final_index = np.where(sigma_z_nofp_7_widths > 0)[0][-1]

sigma_z_1_final_index = np.where(sigma_z_1_widths > 0)[0][-1]
sigma_z_2_final_index = np.where(sigma_z_2_widths > 0)[0][-1]
sigma_z_3_final_index = np.where(sigma_z_3_widths > 0)[0][-1]
sigma_z_4_final_index = np.where(sigma_z_4_widths > 0)[0][-1]
sigma_z_5_final_index = np.where(sigma_z_5_widths > 0)[0][-1]
sigma_z_6_final_index = np.where(sigma_z_6_widths > 0)[0][-1]
sigma_z_7_final_index = np.where(sigma_z_7_widths > 0)[0][-1]


max_final_index = np.max(np.array([baseline_final_index, 
                             sigma_z_nofp_1_final_index,
                             sigma_z_nofp_2_final_index, 
                             sigma_z_nofp_3_final_index,
                             sigma_z_nofp_4_final_index,
                             sigma_z_nofp_5_final_index, 
                             sigma_z_nofp_6_final_index,
                             sigma_z_nofp_7_final_index,
                             sigma_z_1_final_index,
                             sigma_z_2_final_index, 
                             sigma_z_3_final_index,
                             sigma_z_4_final_index,
                             sigma_z_5_final_index, 
                             sigma_z_6_final_index,
                             sigma_z_7_final_index])) + 1
timestep = 1000
sec_in_year = 3.154e7
time_array_absolute = np.arange(0, max_final_index * timestep, timestep) / sec_in_year #years
time_array = time_array_absolute / np.max(time_array_absolute)

##############################################################################

#normalize outputs to baseline_equilibrium_value
#find value of last entry in dataset

sigma_z_nofp_1_widths_norm = sigma_z_nofp_1_widths / baseline_widths[baseline_final_index]
sigma_z_nofp_2_widths_norm = sigma_z_nofp_2_widths / baseline_widths[baseline_final_index]
sigma_z_nofp_3_widths_norm = sigma_z_nofp_3_widths / baseline_widths[baseline_final_index]
sigma_z_nofp_4_widths_norm = sigma_z_nofp_4_widths / baseline_widths[baseline_final_index]
sigma_z_nofp_5_widths_norm = sigma_z_nofp_5_widths / baseline_widths[baseline_final_index]
sigma_z_nofp_6_widths_norm = sigma_z_nofp_6_widths / baseline_widths[baseline_final_index]
sigma_z_nofp_7_widths_norm = sigma_z_nofp_7_widths / baseline_widths[baseline_final_index]

sigma_z_nofp_1_depths_norm = sigma_z_nofp_1_depths / baseline_depths[baseline_final_index]
sigma_z_nofp_2_depths_norm = sigma_z_nofp_2_depths / baseline_depths[baseline_final_index]
sigma_z_nofp_3_depths_norm = sigma_z_nofp_3_depths / baseline_depths[baseline_final_index]
sigma_z_nofp_4_depths_norm = sigma_z_nofp_4_depths / baseline_depths[baseline_final_index]
sigma_z_nofp_5_depths_norm = sigma_z_nofp_5_depths / baseline_depths[baseline_final_index]
sigma_z_nofp_6_depths_norm = sigma_z_nofp_6_depths / baseline_depths[baseline_final_index]
sigma_z_nofp_7_depths_norm = sigma_z_nofp_7_depths / baseline_depths[baseline_final_index]

sigma_z_nofp_1_slopes_norm = sigma_z_nofp_1_slopes / baseline_slopes[baseline_final_index]
sigma_z_nofp_2_slopes_norm = sigma_z_nofp_2_slopes / baseline_slopes[baseline_final_index]
sigma_z_nofp_3_slopes_norm = sigma_z_nofp_3_slopes / baseline_slopes[baseline_final_index]
sigma_z_nofp_4_slopes_norm = sigma_z_nofp_4_slopes / baseline_slopes[baseline_final_index]
sigma_z_nofp_5_slopes_norm = sigma_z_nofp_5_slopes / baseline_slopes[baseline_final_index]
sigma_z_nofp_6_slopes_norm = sigma_z_nofp_6_slopes / baseline_slopes[baseline_final_index]
sigma_z_nofp_7_slopes_norm = sigma_z_nofp_7_slopes / baseline_slopes[baseline_final_index]

sigma_z_1_widths_norm = sigma_z_1_widths / baseline_widths[baseline_final_index]
sigma_z_2_widths_norm = sigma_z_2_widths / baseline_widths[baseline_final_index]
sigma_z_3_widths_norm = sigma_z_3_widths / baseline_widths[baseline_final_index]
sigma_z_4_widths_norm = sigma_z_4_widths / baseline_widths[baseline_final_index]
sigma_z_5_widths_norm = sigma_z_5_widths / baseline_widths[baseline_final_index]
sigma_z_6_widths_norm = sigma_z_6_widths / baseline_widths[baseline_final_index]
sigma_z_7_widths_norm = sigma_z_7_widths / baseline_widths[baseline_final_index]

sigma_z_1_depths_norm = sigma_z_1_depths / baseline_depths[baseline_final_index]
sigma_z_2_depths_norm = sigma_z_2_depths / baseline_depths[baseline_final_index]
sigma_z_3_depths_norm = sigma_z_3_depths / baseline_depths[baseline_final_index]
sigma_z_4_depths_norm = sigma_z_4_depths / baseline_depths[baseline_final_index]
sigma_z_5_depths_norm = sigma_z_5_depths / baseline_depths[baseline_final_index]
sigma_z_6_depths_norm = sigma_z_6_depths / baseline_depths[baseline_final_index]
sigma_z_7_depths_norm = sigma_z_7_depths / baseline_depths[baseline_final_index]

sigma_z_1_slopes_norm = sigma_z_1_slopes / baseline_slopes[baseline_final_index]
sigma_z_2_slopes_norm = sigma_z_2_slopes / baseline_slopes[baseline_final_index]
sigma_z_3_slopes_norm = sigma_z_3_slopes / baseline_slopes[baseline_final_index]
sigma_z_4_slopes_norm = sigma_z_4_slopes / baseline_slopes[baseline_final_index]
sigma_z_5_slopes_norm = sigma_z_5_slopes / baseline_slopes[baseline_final_index]
sigma_z_6_slopes_norm = sigma_z_6_slopes / baseline_slopes[baseline_final_index]
sigma_z_7_slopes_norm = sigma_z_7_slopes / baseline_slopes[baseline_final_index]

###############################################################################

#graphical params
linewidth = 5
text_x = 0.02
text_y = 0.87

cmap = matplotlib.colormaps['viridis']
sigma_z_1_color = cmap(1 / 7)
sigma_z_2_color = cmap(2 / 7) #out of order! careful
sigma_z_3_color = cmap(3 / 7)
sigma_z_4_color = cmap(4 / 7)
sigma_z_5_color = cmap(5 / 7)
sigma_z_6_color = cmap(6 / 7)
sigma_z_7_color = cmap(0.99)
alpha = 0.7

markersize = 100

xmin_short = -0.00005
xmax_short = 0.1

#create figure: 6 panels
fig2, axs = plt.subplots(3,2, figsize = (8,8))

width = axs[0, 0]
width_hfp = axs[0, 1]
depth = axs[1, 0]
depth_hfp = axs[1, 1]
slope = axs[2, 0]
slope_hfp = axs[2, 1]

#WIDTH
width_min = 0.97
width_max = 3

#line style
runaway_depo_line = '--'

width.plot(time_array[:sigma_z_nofp_1_final_index], 
                 sigma_z_nofp_1_widths_norm[:sigma_z_nofp_1_final_index],
                 linewidth = linewidth,
                 color = sigma_z_1_color, alpha = alpha)
#width.scatter(time_array[sigma_z_nofp_1_final_index], 
#                   sigma_z_nofp_1_widths_norm[sigma_z_nofp_1_final_index],
#                   color = sigma_z_1_color, alpha = alpha, s = 100)
width.plot(time_array[:sigma_z_nofp_2_final_index], 
                 sigma_z_nofp_2_widths_norm[:sigma_z_nofp_2_final_index],
                 linewidth = linewidth,
                 color = sigma_z_2_color, alpha = alpha)
#width.scatter(time_array[sigma_z_nofp_2_final_index], 
#                   sigma_z_nofp_2_widths_norm[sigma_z_nofp_2_final_index],
#                   color = sigma_z_2_color, alpha = alpha, s = 100)
width.plot(time_array[:sigma_z_nofp_3_final_index], 
                 sigma_z_nofp_3_widths_norm[:sigma_z_nofp_3_final_index],
                 linewidth = linewidth, 
                 color = sigma_z_3_color, alpha = alpha)
#width.scatter(time_array[sigma_z_nofp_3_final_index], 
#                   sigma_z_nofp_3_widths_norm[sigma_z_nofp_3_final_index],
#                   color = sigma_z_3_color, alpha = alpha, s = 100)
width.plot(time_array[:sigma_z_nofp_4_final_index], 
                 sigma_z_nofp_4_widths_norm[:sigma_z_nofp_4_final_index],
                 linewidth = linewidth,
                 color = sigma_z_4_color, alpha = alpha)
#width.scatter(time_array[sigma_z_nofp_4_final_index], 
#                   sigma_z_nofp_4_widths_norm[sigma_z_nofp_4_final_index],
#                   color = sigma_z_4_color, alpha = alpha, s = 100)
width.plot(time_array[:sigma_z_nofp_5_final_index], 
                 sigma_z_nofp_5_widths_norm[:sigma_z_nofp_5_final_index],
                 linewidth = linewidth,
                 color = sigma_z_5_color, alpha = alpha,
                 linestyle = runaway_depo_line)
#width.scatter(time_array[sigma_z_nofp_5_final_index], 
#                   sigma_z_nofp_5_widths_norm[sigma_z_nofp_5_final_index],
#                   color = sigma_z_5_color, alpha = alpha, s = 100)
width.plot(time_array[:sigma_z_nofp_6_final_index], 
                 sigma_z_nofp_6_widths_norm[:sigma_z_nofp_6_final_index],
                 linewidth = linewidth,
                 color = sigma_z_6_color, alpha = alpha,
                 linestyle = runaway_depo_line)
#width.scatter(time_array[sigma_z_nofp_6_final_index], 
#                   sigma_z_nofp_6_widths_norm[sigma_z_nofp_6_final_index],
#                   color = sigma_z_6_color, alpha = alpha, s = 100)
width.plot(time_array[:sigma_z_nofp_7_final_index], 
                 sigma_z_nofp_7_widths_norm[:sigma_z_nofp_7_final_index],
                 linewidth = linewidth,
                 color = sigma_z_7_color, alpha = alpha,
                 linestyle = runaway_depo_line)
#width.scatter(time_array[sigma_z_nofp_7_final_index], 
#                   sigma_z_nofp_7_widths_norm[sigma_z_nofp_7_final_index],
#                   color = sigma_z_7_color, alpha = alpha, s = 100)

width.axhline(y = 1, color = 'gray', linestyle = '--')
width.get_xaxis().set_ticklabels([])
width.set_ylabel('Normalized width [-]')
width.text(text_x, text_y, 'A', transform=width.transAxes, fontsize = 20)
width.set_xlim(xmin_short, xmax_short)
width.set_ylim(width_min, width_max)

width_hfp.plot(time_array[:sigma_z_nofp_1_final_index], 
                 sigma_z_nofp_1_widths_norm[:sigma_z_nofp_1_final_index],
                 linewidth = linewidth,
                 color = sigma_z_1_color, alpha = alpha)
width_hfp.scatter(time_array[sigma_z_nofp_1_final_index], 
                   sigma_z_nofp_1_widths_norm[sigma_z_nofp_1_final_index],
                   color = sigma_z_1_color, alpha = alpha, s = 100)
width_hfp.plot(time_array[:sigma_z_nofp_2_final_index], 
                 sigma_z_nofp_2_widths_norm[:sigma_z_nofp_2_final_index],
                 linewidth = linewidth,
                 color = sigma_z_2_color, alpha = alpha)
width_hfp.scatter(time_array[sigma_z_nofp_2_final_index], 
                   sigma_z_nofp_2_widths_norm[sigma_z_nofp_2_final_index],
                   color = sigma_z_2_color, alpha = alpha, s = 100)
width_hfp.plot(time_array[:sigma_z_nofp_3_final_index], 
                 sigma_z_nofp_3_widths_norm[:sigma_z_nofp_3_final_index],
                 linewidth = linewidth, 
                 color = sigma_z_3_color, alpha = alpha)
width_hfp.scatter(time_array[sigma_z_nofp_3_final_index], 
                   sigma_z_nofp_3_widths_norm[sigma_z_nofp_3_final_index],
                   color = sigma_z_3_color, alpha = alpha, s = 100)
width_hfp.plot(time_array[:sigma_z_nofp_4_final_index], 
                 sigma_z_nofp_4_widths_norm[:sigma_z_nofp_4_final_index],
                 linewidth = linewidth,
                 color = sigma_z_4_color, alpha = alpha)
width_hfp.scatter(time_array[sigma_z_nofp_4_final_index], 
                   sigma_z_nofp_4_widths_norm[sigma_z_nofp_4_final_index],
                   color = sigma_z_4_color, alpha = alpha, s = 100)
width_hfp.plot(time_array[:sigma_z_nofp_5_final_index], 
                 sigma_z_nofp_5_widths_norm[:sigma_z_nofp_5_final_index],
                 linewidth = linewidth,
                 color = sigma_z_5_color, alpha = alpha,
                 linestyle = runaway_depo_line)
width_hfp.scatter(time_array[sigma_z_nofp_5_final_index], 
                   sigma_z_nofp_5_widths_norm[sigma_z_nofp_5_final_index],
                   color = sigma_z_5_color, alpha = alpha, s = 100)
width_hfp.plot(time_array[:sigma_z_nofp_6_final_index], 
                 sigma_z_nofp_6_widths_norm[:sigma_z_nofp_6_final_index],
                 linewidth = linewidth,
                 color = sigma_z_6_color, alpha = alpha,
                 linestyle = runaway_depo_line)
width_hfp.scatter(time_array[sigma_z_nofp_6_final_index], 
                   sigma_z_nofp_6_widths_norm[sigma_z_nofp_6_final_index],
                   color = sigma_z_6_color, alpha = alpha, s = 100,)
width_hfp.plot(time_array[:sigma_z_nofp_7_final_index], 
                 sigma_z_nofp_7_widths_norm[:sigma_z_nofp_7_final_index],
                 linewidth = linewidth,
                 color = sigma_z_7_color, alpha = alpha,
                 clip_on = False,
                 linestyle = runaway_depo_line)
width_hfp.scatter(time_array[sigma_z_nofp_7_final_index], 
                   sigma_z_nofp_7_widths_norm[sigma_z_nofp_7_final_index],
                   color = sigma_z_7_color, alpha = alpha, s = 100,
                   clip_on = False)

width_hfp.axhline(y = 1, color = 'gray', linestyle = '--')
width_hfp.get_xaxis().set_ticklabels([])
#width_long.get_yaxis().set_ticklabels([])
#width_long.set_ylabel('Equilibrium width [m]')
width_hfp.text(text_x, text_y, 'B', transform=width_hfp.transAxes, fontsize = 20)
width_hfp.set_xlim(-0.02, 1.05)
width_hfp.set_ylim(0.95, 4)

#DEPTH
depth_min = 0.95
depth_max = 2.2

depth.plot(time_array[1:sigma_z_nofp_1_final_index], 
                 sigma_z_nofp_1_depths_norm[1:sigma_z_nofp_1_final_index],
                 linewidth = linewidth, label = '$z_0=0.1$ m', 
                 color = sigma_z_1_color, alpha = alpha)
#depth.scatter(time_array[sigma_z_nofp_1_final_index], 
#                   sigma_z_nofp_1_depths_norm[sigma_z_nofp_1_final_index],
#                   color = sigma_z_1_color, alpha = alpha, s = 100)
depth.plot(time_array[1:sigma_z_nofp_2_final_index], 
                 sigma_z_nofp_2_depths_norm[1:sigma_z_nofp_2_final_index],
                 linewidth = linewidth, label = '$z_0=0.25$ m',
                 color = sigma_z_2_color, alpha = alpha)
#depth.scatter(time_array[sigma_z_nofp_2_final_index], 
#                   sigma_z_nofp_2_depths_norm[sigma_z_nofp_2_final_index],
#                   color = sigma_z_2_color, alpha = alpha, s = 100)
depth.plot(time_array[1:sigma_z_nofp_3_final_index], 
                 sigma_z_nofp_3_depths_norm[1:sigma_z_nofp_3_final_index],
                 linewidth = linewidth, label = '$z_0=0.5$ m',
                 color = sigma_z_3_color, alpha = alpha)
#depth.scatter(time_array[sigma_z_nofp_3_final_index], 
#                   sigma_z_nofp_3_depths_norm[sigma_z_nofp_3_final_index],
#                   color = sigma_z_3_color, alpha = alpha, s = 100)
depth.plot(time_array[1:sigma_z_nofp_4_final_index], 
                 sigma_z_nofp_4_depths_norm[1:sigma_z_nofp_4_final_index],
                 linewidth = linewidth, label = '$z_0=1$ m',
                 color = sigma_z_3_color, alpha = alpha)
#depth.scatter(time_array[sigma_z_nofp_4_final_index], 
#                   sigma_z_nofp_4_depths_norm[sigma_z_nofp_4_final_index],
#                   color = sigma_z_4_color, alpha = alpha, s = 100)
depth.plot(time_array[1:sigma_z_nofp_5_final_index], 
                 sigma_z_nofp_5_depths_norm[1:sigma_z_nofp_5_final_index],
                 linewidth = linewidth,  label = '$z_0=2.5$ m',
                 color = sigma_z_5_color, alpha = alpha,
                 linestyle = runaway_depo_line)
#depth.scatter(time_array[sigma_z_nofp_5_final_index], 
#                   sigma_z_nofp_5_depths_norm[sigma_z_nofp_5_final_index],
#                   color = sigma_z_5_color, alpha = alpha, s = 100)
depth.plot(time_array[1:sigma_z_nofp_6_final_index], 
                 sigma_z_nofp_6_depths_norm[1:sigma_z_nofp_6_final_index],
                 linewidth = linewidth, label = '$z_0=5$ m',
                 color = sigma_z_6_color, alpha = alpha,
                 linestyle = runaway_depo_line)
#depth.scatter(time_array[sigma_z_nofp_6_final_index], 
#                   sigma_z_nofp_6_depths_norm[sigma_z_nofp_6_final_index],
#                   color = sigma_z_6_color, alpha = alpha, s = 100)
depth.plot(time_array[1:sigma_z_nofp_7_final_index], 
                 sigma_z_nofp_7_depths_norm[1:sigma_z_nofp_7_final_index],
                 linewidth = linewidth, label = '$z_0=10$ m',
                 color = sigma_z_7_color, alpha = alpha,
                 linestyle = runaway_depo_line)
#depth.scatter(time_array[sigma_z_nofp_7_final_index], 
#                   sigma_z_nofp_7_depths_norm[sigma_z_nofp_7_final_index],
#                   color = sigma_z_7_color, alpha = alpha, s = 100)

handles, labels = depth.get_legend_handles_labels()


depth.axhline(y = 1, color = 'gray', linestyle = '--')
depth.get_xaxis().set_ticklabels([])
depth.set_ylabel('Normalized depth [-]')
depth.text(text_x, text_y, 'C', transform=depth.transAxes, fontsize = 20)
depth.set_xlim(xmin_short, xmax_short)
#depth_short.set_xlim(xmin_short, xmax_short)
depth.set_ylim(0.6, 9)

#depth_hfp.set_clip_on(False)

depth_hfp.plot(time_array[1:sigma_z_nofp_1_final_index], 
                 sigma_z_nofp_1_depths_norm[1:sigma_z_nofp_1_final_index],
                 linewidth = linewidth, label = '$z_0=0.1$ m', 
                 color = sigma_z_1_color, alpha = alpha)
depth_hfp.scatter(time_array[sigma_z_nofp_1_final_index], 
                   sigma_z_nofp_1_depths_norm[sigma_z_nofp_1_final_index],
                   color = sigma_z_1_color, alpha = alpha, s = 100)
depth_hfp.plot(time_array[1:sigma_z_nofp_2_final_index], 
                 sigma_z_nofp_2_depths_norm[1:sigma_z_nofp_2_final_index],
                 linewidth = linewidth, label = '$z_0=0.25$ m',
                 color = sigma_z_2_color, alpha = alpha)
depth_hfp.scatter(time_array[sigma_z_nofp_2_final_index], 
                   sigma_z_nofp_2_depths_norm[sigma_z_nofp_2_final_index],
                   color = sigma_z_2_color, alpha = alpha, s = 100)
depth_hfp.plot(time_array[1:sigma_z_nofp_3_final_index], 
                 sigma_z_nofp_3_depths_norm[1:sigma_z_nofp_3_final_index],
                 linewidth = linewidth, label = '$z_0=0.5$ m',
                 color = sigma_z_3_color, alpha = alpha)
depth_hfp.scatter(time_array[sigma_z_nofp_3_final_index], 
                   sigma_z_nofp_3_depths_norm[sigma_z_nofp_3_final_index],
                   color = sigma_z_3_color, alpha = alpha, s = 100)
depth_hfp.plot(time_array[1:sigma_z_nofp_4_final_index], 
                 sigma_z_nofp_4_depths_norm[1:sigma_z_nofp_4_final_index],
                 linewidth = linewidth, label = '$z_0=1$ m',
                 color = sigma_z_3_color, alpha = alpha)
depth_hfp.scatter(time_array[sigma_z_nofp_4_final_index], 
                   sigma_z_nofp_4_depths_norm[sigma_z_nofp_4_final_index],
                   color = sigma_z_4_color, alpha = alpha, s = 100)
depth_hfp.plot(time_array[1:sigma_z_nofp_5_final_index], 
                 sigma_z_nofp_5_depths_norm[1:sigma_z_nofp_5_final_index],
                 linewidth = linewidth,  label = '$z_0=2.5$ m',
                 color = sigma_z_5_color, alpha = alpha,
                 linestyle = runaway_depo_line)
depth_hfp.scatter(time_array[sigma_z_nofp_5_final_index], 
                   sigma_z_nofp_5_depths_norm[sigma_z_nofp_5_final_index],
                   color = sigma_z_5_color, alpha = alpha, s = 100)
depth_hfp.plot(time_array[1:sigma_z_nofp_6_final_index], 
                 sigma_z_nofp_6_depths_norm[1:sigma_z_nofp_6_final_index],
                 linewidth = linewidth, label = '$z_0=5$ m',
                 color = sigma_z_6_color, alpha = alpha,
                 linestyle = runaway_depo_line)
depth_hfp.scatter(time_array[sigma_z_nofp_6_final_index], 
                   sigma_z_nofp_6_depths_norm[sigma_z_nofp_6_final_index],
                   color = sigma_z_6_color, alpha = alpha, s = 100)
depth_hfp.plot(time_array[1:sigma_z_nofp_7_final_index], 
                 sigma_z_nofp_7_depths_norm[1:sigma_z_nofp_7_final_index],
                 linewidth = linewidth, label = '$z_0=10$ m',
                 color = sigma_z_7_color, alpha = alpha,
                 linestyle = runaway_depo_line)
depth_hfp.scatter(time_array[sigma_z_nofp_7_final_index], 
                   sigma_z_nofp_7_depths_norm[sigma_z_nofp_7_final_index],
                   color = sigma_z_7_color, alpha = alpha, s = 100)

depth_hfp.axhline(y = 1, color = 'gray', linestyle = '--')
depth_hfp.get_xaxis().set_ticklabels([])
#depth_long.get_yaxis().set_ticklabels([])
#depth_long.set_ylabel('Equilibrium depth [m]')
depth_hfp.text(text_x, text_y, 'D', transform=depth_hfp.transAxes, fontsize = 20)
depth_hfp.set_ylim(0.6, 9)
depth_hfp.set_xlim(-0.02, 1.05)

import matplotlib.patches as mpatches
arr = mpatches.FancyArrowPatch((0.2, 0.05), (0.38, 0.62),transform=depth_hfp.transAxes,
                               arrowstyle='|-|,widthA=0.4, widthB=0.4', mutation_scale=20,
                               linewidth = 2, zorder = 20)
#depth_hfp.add_patch(arr)
#depth_hfp.annotate("below bank", (.73, .43), xycoords=arr, ha='left', va='bottom', fontsize = 12,
#                   bbox = dict(boxstyle='square', fc = (1,1,1,0.5), color = 'k'))

#depth_hfp.annotate('Regime I', xy = (0.4, 0.05), xytext = (0.5, 0.5),
#                   xycoords = 'axes fraction', fontsize = 12, ha = 'left',
#                   va = 'top', 
#                   bbox = dict(boxstyle='square', fc = (1,1,1,0.5), color = 'k'),
#                   arrowprops = dict(arrowstyle='|-|, widthA=0.5, widthB=0.5',
#                                     lw = 2., color = 'k'))

#depth_hfp.annotate('Regime I', xy = (0.4, 0.), xytext = (0.4, -0.1),
#                   xycoords = 'axes fraction', fontsize = 14, ha = 'center',
#                   va = 'top', 
#                   arrowprops = dict(arrowstyle='-[, widthB=1.5, lengthB=0.5', 
#                                     lw = 2.0, color = 'k'))
#depth_hfp.annotate('Regime II', xy = (0.87, 0.66), xytext = (0.87, 0.56),
#                   xycoords = 'axes fraction', fontsize = 12, ha = 'center',
#                   va = 'top', 
#                   bbox = dict(boxstyle='square', fc = 'white', color = 'k'),
#                   arrowprops = dict(arrowstyle='-[, widthB=1.7, lengthB=0.5', 
#                                     lw = 2.0, color = 'k'))
#depth_hfp.text(0.45, 0.77, 'overbank', transform=depth_hfp.transAxes, fontsize = 12,
#               bbox = dict(boxstyle='square', fc = (1,1,1,0.5), color = 'k'))


#SLOPE
slope_min = 0.6
slope_max = 3

slope.plot(time_array[:sigma_z_nofp_1_final_index], 
                 sigma_z_nofp_1_slopes_norm[:sigma_z_nofp_1_final_index],
                 linewidth = linewidth, color = sigma_z_1_color, alpha = alpha)
#slope.scatter(time_array[sigma_z_nofp_1_final_index], 
#                   sigma_z_nofp_1_slopes_norm[sigma_z_nofp_1_final_index],
#                   color = sigma_z_1_color, alpha = alpha, s = 100)
slope.plot(time_array[:sigma_z_nofp_2_final_index], 
                 sigma_z_nofp_2_slopes_norm[:sigma_z_nofp_2_final_index],
                 linewidth = linewidth, color = sigma_z_2_color, alpha = alpha)
#slope.scatter(time_array[sigma_z_nofp_2_final_index], 
#                   sigma_z_nofp_2_slopes_norm[sigma_z_nofp_2_final_index],
#                   color = sigma_z_2_color, alpha = alpha, s = 100)
slope.plot(time_array[:sigma_z_nofp_3_final_index], 
                 sigma_z_nofp_3_slopes_norm[:sigma_z_nofp_3_final_index],
                 linewidth = linewidth, color = sigma_z_3_color, alpha = alpha)
#slope.scatter(time_array[sigma_z_nofp_3_final_index], 
#                   sigma_z_nofp_3_slopes_norm[sigma_z_nofp_3_final_index],
#                   color = sigma_z_3_color, alpha = alpha, s = 100)
slope.plot(time_array[:sigma_z_nofp_4_final_index], 
                 sigma_z_nofp_4_slopes_norm[:sigma_z_nofp_4_final_index],
                 linewidth = linewidth, color = sigma_z_4_color, alpha = alpha)
#slope.scatter(time_array[sigma_z_nofp_4_final_index], 
#                   sigma_z_nofp_4_slopes_norm[sigma_z_nofp_4_final_index],
#                   color = sigma_z_4_color, alpha = alpha, s = 100)
slope.plot(time_array[:sigma_z_nofp_5_final_index], 
                 sigma_z_nofp_5_slopes_norm[:sigma_z_nofp_5_final_index],
                 linewidth = linewidth, color = sigma_z_5_color, alpha = alpha,
                 linestyle = runaway_depo_line)
#slope.scatter(time_array[sigma_z_nofp_5_final_index], 
#                   sigma_z_nofp_5_slopes_norm[sigma_z_nofp_5_final_index],
#                   color = sigma_z_5_color, alpha = alpha, s = 100)
slope.plot(time_array[:sigma_z_nofp_6_final_index], 
                 sigma_z_nofp_6_slopes_norm[:sigma_z_nofp_6_final_index],
                 linewidth = linewidth, color = sigma_z_6_color, alpha = alpha,
                 linestyle = runaway_depo_line)
#slope.scatter(time_array[sigma_z_nofp_6_final_index], 
#                   sigma_z_nofp_6_slopes_norm[sigma_z_nofp_6_final_index],
#                   color = sigma_z_6_color, alpha = alpha, s = 100)
slope.plot(time_array[:sigma_z_nofp_7_final_index], 
                 sigma_z_nofp_7_slopes_norm[:sigma_z_nofp_7_final_index],
                 linewidth = linewidth, color = sigma_z_7_color, alpha = alpha, 
                 zorder = 20,
                 linestyle = runaway_depo_line)
#slope.scatter(time_array[sigma_z_nofp_7_final_index], 
#                   sigma_z_nofp_7_slopes_norm[sigma_z_nofp_7_final_index],
#                   color = sigma_z_7_color, alpha = alpha, s = 100)


slope.set_xlabel('Normalized time [-]')
slope.set_ylabel('Normalized local slope [-]')
slope.axhline(y = 1, color = 'gray', linestyle = '--')
slope.text(text_x, text_y, 'E', transform=slope.transAxes, fontsize = 20)
slope.set_xlim(xmin_short, xmax_short)
slope.set_ylim(slope_min, slope_max)


slope_legend = slope.legend(handles[::-1], labels[::-1], bbox_to_anchor=(1.1,1.88), loc = 'lower right', 
                   bbox_transform=slope.transAxes, framealpha = 1,
                   edgecolor = 'k', ncols = 2)


slope_hfp.plot(time_array[:sigma_z_nofp_1_final_index], 
                 sigma_z_nofp_1_slopes_norm[:sigma_z_nofp_1_final_index],
                 linewidth = linewidth, color = sigma_z_1_color, alpha = alpha)
slope_hfp.scatter(time_array[sigma_z_nofp_1_final_index], 
                   sigma_z_nofp_1_slopes_norm[sigma_z_nofp_1_final_index],
                   color = sigma_z_1_color, alpha = alpha, s = 100)
slope_hfp.plot(time_array[:sigma_z_nofp_2_final_index], 
                 sigma_z_nofp_2_slopes_norm[:sigma_z_nofp_2_final_index],
                 linewidth = linewidth, color = sigma_z_2_color, alpha = alpha)
slope_hfp.scatter(time_array[sigma_z_nofp_2_final_index], 
                   sigma_z_nofp_2_slopes_norm[sigma_z_nofp_2_final_index],
                   color = sigma_z_2_color, alpha = alpha, s = 100)
slope_hfp.plot(time_array[:sigma_z_nofp_3_final_index], 
                 sigma_z_nofp_3_slopes_norm[:sigma_z_nofp_3_final_index],
                 linewidth = linewidth, color = sigma_z_3_color, alpha = alpha)
slope_hfp.scatter(time_array[sigma_z_nofp_3_final_index], 
                   sigma_z_nofp_3_slopes_norm[sigma_z_nofp_3_final_index],
                   color = sigma_z_3_color, alpha = alpha, s = 100)
slope_hfp.plot(time_array[:sigma_z_nofp_4_final_index], 
                 sigma_z_nofp_4_slopes_norm[:sigma_z_nofp_4_final_index],
                 linewidth = linewidth, color = sigma_z_4_color, alpha = alpha)
slope_hfp.scatter(time_array[sigma_z_nofp_4_final_index], 
                   sigma_z_nofp_4_slopes_norm[sigma_z_nofp_4_final_index],
                   color = sigma_z_4_color, alpha = alpha, s = 100)
slope_hfp.plot(time_array[:sigma_z_nofp_5_final_index], 
                 sigma_z_nofp_5_slopes_norm[:sigma_z_nofp_5_final_index],
                 linewidth = linewidth, color = sigma_z_5_color, alpha = alpha,
                 linestyle = runaway_depo_line)
slope_hfp.scatter(time_array[sigma_z_nofp_5_final_index], 
                   sigma_z_nofp_5_slopes_norm[sigma_z_nofp_5_final_index],
                   color = sigma_z_5_color, alpha = alpha, s = 100)
slope_hfp.plot(time_array[:sigma_z_nofp_6_final_index], 
                 sigma_z_nofp_6_slopes_norm[:sigma_z_nofp_6_final_index],
                 linewidth = linewidth, color = sigma_z_6_color, alpha = alpha,
                 linestyle = runaway_depo_line)
slope_hfp.scatter(time_array[sigma_z_nofp_6_final_index], 
                   sigma_z_nofp_6_slopes_norm[sigma_z_nofp_6_final_index],
                   color = sigma_z_6_color, alpha = alpha, s = 100)
slope_hfp.plot(time_array[:sigma_z_nofp_7_final_index], 
                 sigma_z_nofp_7_slopes_norm[:sigma_z_nofp_7_final_index],
                 linewidth = linewidth, color = sigma_z_7_color, alpha = alpha, 
                 zorder = 20, linestyle = runaway_depo_line)
slope_hfp.scatter(time_array[sigma_z_nofp_7_final_index], 
                   sigma_z_nofp_7_slopes_norm[sigma_z_nofp_7_final_index],
                   color = sigma_z_7_color, alpha = alpha, s = 100)

slope_hfp.set_xlabel('Normalized time [-]')
#slope_long.get_yaxis().set_ticklabels([])
#slope_long.set_ylabel('Equilibrium slope [m/m]')
slope_hfp.axhline(y = 1, color = 'gray', linestyle = '--')
#slope_short.set_xlim(-0.02, 1)
slope_hfp.set_ylim(0.6, 4)
slope_hfp.text(text_x, text_y, 'F', transform=slope_hfp.transAxes, fontsize = 20)
#slope.legend(loc = 'upper center', framealpha = 1, edgecolor = 'k')
slope_hfp.set_xlim(-0.02, 1.05)


#plt.tight_layout()
fig2.savefig('figure_8_9_condensed.png', dpi = 1000, bbox_inches = 'tight')
fig2.savefig('figure_8_9_condensed.png', dpi = 200, bbox_inches = 'tight')



