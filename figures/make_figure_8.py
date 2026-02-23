#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Create figure 8 in Shobe and Scott: Trajectories of channel evolution.

Created February 2026 by @author: charlesshobe
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

#######IMPORT BASELINE DATA FOR NORMALIZATION
run_name = 'trajectory_z0_baseline_rev1'
baseline_widths = np.load('results/' + str(run_name) + '_widths.npy')
baseline_depths = np.load('results/' + str(run_name) + '_depths_r.npy')
baseline_slopes = np.load('results/' + str(run_name) + '_slopes.npy')
#baseline_e_slopes = np.load('results/' + str(run_name) + '_e_slopes.npy')
baseline_tau_bed = np.load('results/' + str(run_name) + '_tau_bed.npy')
baseline_tau_bank = np.load('results/' + str(run_name) + '_tau_bank.npy')
#baseline_fr_over_f0 = np.load('results/' + str(run_name) + '_fr_over_f0.npy')
#baseline_qs_out = np.load('results/' + str(run_name) + '_qs_out.npy')


#######IMPORT NON-DEPTH-CONSTRAINED DATA
run_name = 'trajectory_rev1_z0_0point1_L1000_tol1e-13_dt1000_kero1_kdep10'
sigma_z_nofp_1_widths = np.load('results/' + str(run_name) + '_widths.npy')
sigma_z_nofp_1_depths = np.load('results/' + str(run_name) + '_depths_r.npy')
sigma_z_nofp_1_slopes = np.load('results/' + str(run_name) + '_slopes.npy')
#sigma_z_nofp_1_e_slopes = np.load('results/' + str(run_name) + '_e_slopes.npy')
sigma_z_nofp_1_tau_bed = np.load('results/' + str(run_name) + '_tau_bed.npy')
sigma_z_nofp_1_tau_bank = np.load('results/' + str(run_name) + '_tau_bank.npy')
#sigma_z_nofp_1_fr_over_f0 = np.load('results/' + str(run_name) + '_fr_over_f0.npy')
#sigma_z_nofp_1_qs_out = np.load('results/' + str(run_name) + '_qs_out.npy')

run_name = 'trajectory_rev1_z0_0point25_L1000_tol1e-13_dt1000_kero1_kdep10'
sigma_z_nofp_2_widths = np.load('results/' + str(run_name) + '_widths.npy')
sigma_z_nofp_2_depths = np.load('results/' + str(run_name) + '_depths_r.npy')
sigma_z_nofp_2_slopes = np.load('results/' + str(run_name) + '_slopes.npy')
#sigma_z_nofp_2_e_slopes = np.load('results/' + str(run_name) + '_e_slopes.npy')
sigma_z_nofp_2_tau_bed = np.load('results/' + str(run_name) + '_tau_bed.npy')
sigma_z_nofp_2_tau_bank = np.load('results/' + str(run_name) + '_tau_bank.npy')
#sigma_z_nofp_2_fr_over_f0 = np.load('results/' + str(run_name) + '_fr_over_f0.npy')
#sigma_z_nofp_2_qs_out = np.load('results/' + str(run_name) + '_qs_out.npy')


run_name = 'trajectory_rev1_z0_0point5_L1000_tol1e-13_dt1000_kero1_kdep10'
sigma_z_nofp_3_widths = np.load('results/' + str(run_name) + '_widths.npy')
sigma_z_nofp_3_depths = np.load('results/' + str(run_name) + '_depths_r.npy')
sigma_z_nofp_3_slopes = np.load('results/' + str(run_name) + '_slopes.npy')
#sigma_z_nofp_3_e_slopes = np.load('results/' + str(run_name) + '_e_slopes.npy')
sigma_z_nofp_3_tau_bed = np.load('results/' + str(run_name) + '_tau_bed.npy')
sigma_z_nofp_3_tau_bank = np.load('results/' + str(run_name) + '_tau_bank.npy')
#sigma_z_nofp_3_fr_over_f0 = np.load('results/' + str(run_name) + '_fr_over_f0.npy')
#sigma_z_nofp_3_qs_out = np.load('results/' + str(run_name) + '_qs_out.npy')

run_name = 'trajectory_rev1_z0_1_L1000_tol1e-13_dt1000_kero1_kdep10'
sigma_z_nofp_4_widths = np.load('results/' + str(run_name) + '_widths.npy')
sigma_z_nofp_4_depths = np.load('results/' + str(run_name) + '_depths_r.npy')
sigma_z_nofp_4_slopes = np.load('results/' + str(run_name) + '_slopes.npy')
#sigma_z_nofp_4_e_slopes = np.load('results/' + str(run_name) + '_e_slopes.npy')
sigma_z_nofp_4_tau_bed = np.load('results/' + str(run_name) + '_tau_bed.npy')
sigma_z_nofp_4_tau_bank = np.load('results/' + str(run_name) + '_tau_bank.npy')
#sigma_z_nofp_4_fr_over_f0 = np.load('results/' + str(run_name) + '_fr_over_f0.npy')
#sigma_z_nofp_4_qs_out = np.load('results/' + str(run_name) + '_qs_out.npy')

run_name = 'trajectory_rev1_z0_2point5_L1000_tol1e-13_dt1000_kero1_kdep10'
sigma_z_nofp_5_widths = np.load('results/' + str(run_name) + '_widths.npy')
sigma_z_nofp_5_depths = np.load('results/' + str(run_name) + '_depths_r.npy')
sigma_z_nofp_5_slopes = np.load('results/' + str(run_name) + '_slopes.npy')
#sigma_z_nofp_5_e_slopes = np.load('results/' + str(run_name) + '_e_slopes.npy')
sigma_z_nofp_5_tau_bed = np.load('results/' + str(run_name) + '_tau_bed.npy')
sigma_z_nofp_5_tau_bank = np.load('results/' + str(run_name) + '_tau_bank.npy')
#sigma_z_nofp_5_fr_over_f0 = np.load('results/' + str(run_name) + '_fr_over_f0.npy')
#sigma_z_nofp_5_qs_out = np.load('results/' + str(run_name) + '_qs_out.npy')

run_name = 'trajectory_rev1_z0_5_L1000_tol1e-13_dt1000_kero1_kdep10'
sigma_z_nofp_6_widths = np.load('results/' + str(run_name) + '_widths.npy')
sigma_z_nofp_6_depths = np.load('results/' + str(run_name) + '_depths_r.npy')
sigma_z_nofp_6_slopes = np.load('results/' + str(run_name) + '_slopes.npy')
#sigma_z_nofp_6_e_slopes = np.load('results/' + str(run_name) + '_e_slopes.npy')
sigma_z_nofp_6_tau_bed = np.load('results/' + str(run_name) + '_tau_bed.npy')
sigma_z_nofp_6_tau_bank = np.load('results/' + str(run_name) + '_tau_bank.npy')
#sigma_z_nofp_6_fr_over_f0 = np.load('results/' + str(run_name) + '_fr_over_f0.npy')
#sigma_z_nofp_6_qs_out = np.load('results/' + str(run_name) + '_qs_out.npy')

run_name = 'trajectory_rev1_z0_10_L1000_tol1e-13_dt1000_kero1_kdep10'
sigma_z_nofp_7_widths = np.load('results/' + str(run_name) + '_widths.npy')
sigma_z_nofp_7_depths = np.load('results/' + str(run_name) + '_depths_r.npy')
sigma_z_nofp_7_slopes = np.load('results/' + str(run_name) + '_slopes.npy')
#sigma_z_nofp_7_e_slopes = np.load('results/' + str(run_name) + '_e_slopes.npy')
sigma_z_nofp_7_tau_bed = np.load('results/' + str(run_name) + '_tau_bed.npy')
sigma_z_nofp_7_tau_bank = np.load('results/' + str(run_name) + '_tau_bank.npy')
#sigma_z_nofp_7_fr_over_f0 = np.load('results/' + str(run_name) + '_fr_over_f0.npy')
#sigma_z_nofp_7_qs_out = np.load('results/' + str(run_name) + '_qs_out.npy')

# #######IMPORT DEPTH-CONSTRAINED DATA (HFP = 3 M)

# run_name = 'trajectory_rev1_z0_0point1_L1000_tol1e-13_dt1000_kero1_kdep10_fp'
# sigma_z_1_widths = np.load('results/' + str(run_name) + '_widths.npy')
# sigma_z_1_depths = np.load('results/' + str(run_name) + '_depths_r.npy')
# sigma_z_1_slopes = np.load('results/' + str(run_name) + '_slopes.npy')
# #sigma_z_1_e_slopes = np.load('results/' + str(run_name) + '_e_slopes.npy')
# #sigma_z_1_tau_bed = np.load('results/' + str(run_name) + '_tau_bed.npy')
# #sigma_z_1_tau_bank = np.load('results/' + str(run_name) + '_tau_bank.npy')
# #sigma_z_1_fr_over_f0 = np.load('results/' + str(run_name) + '_fr_over_f0.npy')
# #sigma_z_1_qs_out = np.load('results/' + str(run_name) + '_qs_out.npy')

# run_name = 'trajectory_rev1_z0_0point25_L1000_tol1e-13_dt1000_kero1_kdep10_fp'
# sigma_z_2_widths = np.load('results/' + str(run_name) + '_widths.npy')
# sigma_z_2_depths = np.load('results/' + str(run_name) + '_depths_r.npy')
# sigma_z_2_slopes = np.load('results/' + str(run_name) + '_slopes.npy')
# #sigma_z_2_e_slopes = np.load('results/' + str(run_name) + '_e_slopes.npy')
# #sigma_z_2_tau_bed = np.load('results/' + str(run_name) + '_tau_bed.npy')
# #sigma_z_2_tau_bank = np.load('results/' + str(run_name) + '_tau_bank.npy')
# #sigma_z_2_fr_over_f0 = np.load('results/' + str(run_name) + '_fr_over_f0.npy')
# #sigma_z_2_qs_out = np.load('results/' + str(run_name) + '_qs_out.npy')

# run_name = 'trajectory_rev1_z0_0point5_L1000_tol1e-13_dt1000_kero1_kdep10_fp'
# sigma_z_3_widths = np.load('results/' + str(run_name) + '_widths.npy')
# sigma_z_3_depths = np.load('results/' + str(run_name) + '_depths_r.npy')
# sigma_z_3_slopes = np.load('results/' + str(run_name) + '_slopes.npy')
# #sigma_z_3_e_slopes = np.load('results/' + str(run_name) + '_e_slopes.npy')
# #sigma_z_3_tau_bed = np.load('results/' + str(run_name) + '_tau_bed.npy')
# #sigma_z_3_tau_bank = np.load('results/' + str(run_name) + '_tau_bank.npy')
# #sigma_z_3_fr_over_f0 = np.load('results/' + str(run_name) + '_fr_over_f0.npy')
# #sigma_z_3_qs_out = np.load('results/' + str(run_name) + '_qs_out.npy')

# run_name = 'trajectory_rev1_z0_1_L1000_tol1e-13_dt1000_kero1_kdep10_fp'
# sigma_z_4_widths = np.load('results/' + str(run_name) + '_widths.npy')
# sigma_z_4_depths = np.load('results/' + str(run_name) + '_depths_r.npy')
# sigma_z_4_slopes = np.load('results/' + str(run_name) + '_slopes.npy')
# #sigma_z_4_e_slopes = np.load('results/' + str(run_name) + '_e_slopes.npy')
# #sigma_z_4_tau_bed = np.load('results/' + str(run_name) + '_tau_bed.npy')
# #sigma_z_4_tau_bank = np.load('results/' + str(run_name) + '_tau_bank.npy')
# #sigma_z_4_fr_over_f0 = np.load('results/' + str(run_name) + '_fr_over_f0.npy')
# #sigma_z_4_qs_out = np.load('results/' + str(run_name) + '_qs_out.npy')

# run_name = 'trajectory_rev1_z0_2point5_L1000_tol1e-13_dt1000_kero1_kdep10_fp'
# sigma_z_5_widths = np.load('results/' + str(run_name) + '_widths.npy')
# sigma_z_5_depths = np.load('results/' + str(run_name) + '_depths_r.npy')
# sigma_z_5_slopes = np.load('results/' + str(run_name) + '_slopes.npy')
# #sigma_z_5_e_slopes = np.load('results/' + str(run_name) + '_e_slopes.npy')
# #sigma_z_5_tau_bed = np.load('results/' + str(run_name) + '_tau_bed.npy')
# #sigma_z_5_tau_bank = np.load('results/' + str(run_name) + '_tau_bank.npy')
# #sigma_z_5_fr_over_f0 = np.load('results/' + str(run_name) + '_fr_over_f0.npy')
# #sigma_z_5_qs_out = np.load('results/' + str(run_name) + '_qs_out.npy')

# run_name = 'trajectory_rev1_z0_5_L1000_tol1e-13_dt1000_kero1_kdep10_fp'
# sigma_z_6_widths = np.load('results/' + str(run_name) + '_widths.npy')
# sigma_z_6_depths = np.load('results/' + str(run_name) + '_depths_r.npy')
# sigma_z_6_slopes = np.load('results/' + str(run_name) + '_slopes.npy')
# #sigma_z_6_e_slopes = np.load('results/' + str(run_name) + '_e_slopes.npy')
# #sigma_z_6_tau_bed = np.load('results/' + str(run_name) + '_tau_bed.npy')
# #sigma_z_6_tau_bank = np.load('results/' + str(run_name) + '_tau_bank.npy')
# #sigma_z_6_fr_over_f0 = np.load('results/' + str(run_name) + '_fr_over_f0.npy')
# #sigma_z_6_qs_out = np.load('results/' + str(run_name) + '_qs_out.npy')

# run_name = 'trajectory_rev1_z0_10_L1000_tol1e-13_dt1000_kero1_kdep10_fp'
# sigma_z_7_widths = np.load('results/' + str(run_name) + '_widths.npy')
# sigma_z_7_depths = np.load('results/' + str(run_name) + '_depths_r.npy')
# sigma_z_7_slopes = np.load('results/' + str(run_name) + '_slopes.npy')
# #sigma_z_7_e_slopes = np.load('results/' + str(run_name) + '_e_slopes.npy')
# #sigma_z_7_tau_bed = np.load('results/' + str(run_name) + '_tau_bed.npy')
# #sigma_z_7_tau_bank = np.load('results/' + str(run_name) + '_tau_bank.npy')
# #sigma_z_7_fr_over_f0 = np.load('results/' + str(run_name) + '_fr_over_f0.npy')
# #sigma_z_7_qs_out = np.load('results/' + str(run_name) + '_qs_out.npy')
# ##############################################################################

#get time normalization info
baseline_final_index = np.where(baseline_widths > 0)[0][-1]

sigma_z_nofp_1_final_index = np.where(sigma_z_nofp_1_widths > 0)[0][-1]
sigma_z_nofp_2_final_index = np.where(sigma_z_nofp_2_widths > 0)[0][-1]
sigma_z_nofp_3_final_index = np.where(sigma_z_nofp_3_widths > 0)[0][-1]
sigma_z_nofp_4_final_index = np.where(sigma_z_nofp_4_widths > 0)[0][-1]
sigma_z_nofp_5_final_index = np.where(sigma_z_nofp_5_widths > 0)[0][-1]
sigma_z_nofp_6_final_index = np.where(sigma_z_nofp_6_widths > 0)[0][-1]
sigma_z_nofp_7_final_index = np.where(sigma_z_nofp_7_widths > 0)[0][-1]

# sigma_z_1_final_index = np.where(sigma_z_1_widths > 0)[0][-1]
# sigma_z_2_final_index = np.where(sigma_z_2_widths > 0)[0][-1]
# sigma_z_3_final_index = np.where(sigma_z_3_widths > 0)[0][-1]
# sigma_z_4_final_index = np.where(sigma_z_4_widths > 0)[0][-1]
# sigma_z_5_final_index = np.where(sigma_z_5_widths > 0)[0][-1]
# sigma_z_6_final_index = np.where(sigma_z_6_widths > 0)[0][-1]
# sigma_z_7_final_index = np.where(sigma_z_7_widths > 0)[0][-1]


max_final_index = np.max(np.array([baseline_final_index, 
                             sigma_z_nofp_1_final_index,
                             sigma_z_nofp_2_final_index, 
                             sigma_z_nofp_3_final_index,
                             sigma_z_nofp_4_final_index,
                             sigma_z_nofp_5_final_index, 
                             sigma_z_nofp_6_final_index,
                             sigma_z_nofp_7_final_index])) + 1
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

sigma_z_nofp_1_tau_bed_norm = sigma_z_nofp_1_tau_bed / baseline_tau_bed[baseline_final_index]
sigma_z_nofp_2_tau_bed_norm = sigma_z_nofp_2_tau_bed / baseline_tau_bed[baseline_final_index]
sigma_z_nofp_3_tau_bed_norm = sigma_z_nofp_3_tau_bed / baseline_tau_bed[baseline_final_index]
sigma_z_nofp_4_tau_bed_norm = sigma_z_nofp_4_tau_bed / baseline_tau_bed[baseline_final_index]
sigma_z_nofp_5_tau_bed_norm = sigma_z_nofp_5_tau_bed / baseline_tau_bed[baseline_final_index]
sigma_z_nofp_6_tau_bed_norm = sigma_z_nofp_6_tau_bed / baseline_tau_bed[baseline_final_index]
sigma_z_nofp_7_tau_bed_norm = sigma_z_nofp_7_tau_bed / baseline_tau_bed[baseline_final_index]

sigma_z_nofp_1_tau_bank_norm = sigma_z_nofp_1_tau_bank / baseline_tau_bank[baseline_final_index]
sigma_z_nofp_2_tau_bank_norm = sigma_z_nofp_2_tau_bank / baseline_tau_bank[baseline_final_index]
sigma_z_nofp_3_tau_bank_norm = sigma_z_nofp_3_tau_bank / baseline_tau_bank[baseline_final_index]
sigma_z_nofp_4_tau_bank_norm = sigma_z_nofp_4_tau_bank / baseline_tau_bank[baseline_final_index]
sigma_z_nofp_5_tau_bank_norm = sigma_z_nofp_5_tau_bank / baseline_tau_bank[baseline_final_index]
sigma_z_nofp_6_tau_bank_norm = sigma_z_nofp_6_tau_bank / baseline_tau_bank[baseline_final_index]
sigma_z_nofp_7_tau_bank_norm = sigma_z_nofp_7_tau_bank / baseline_tau_bank[baseline_final_index]

# sigma_z_1_widths_norm = sigma_z_1_widths / baseline_widths[baseline_final_index]
# sigma_z_2_widths_norm = sigma_z_2_widths / baseline_widths[baseline_final_index]
# sigma_z_3_widths_norm = sigma_z_3_widths / baseline_widths[baseline_final_index]
# sigma_z_4_widths_norm = sigma_z_4_widths / baseline_widths[baseline_final_index]
# sigma_z_5_widths_norm = sigma_z_5_widths / baseline_widths[baseline_final_index]
# sigma_z_6_widths_norm = sigma_z_6_widths / baseline_widths[baseline_final_index]
# sigma_z_7_widths_norm = sigma_z_7_widths / baseline_widths[baseline_final_index]

# sigma_z_1_depths_norm = sigma_z_1_depths / baseline_depths[baseline_final_index]
# sigma_z_2_depths_norm = sigma_z_2_depths / baseline_depths[baseline_final_index]
# sigma_z_3_depths_norm = sigma_z_3_depths / baseline_depths[baseline_final_index]
# sigma_z_4_depths_norm = sigma_z_4_depths / baseline_depths[baseline_final_index]
# sigma_z_5_depths_norm = sigma_z_5_depths / baseline_depths[baseline_final_index]
# sigma_z_6_depths_norm = sigma_z_6_depths / baseline_depths[baseline_final_index]
# sigma_z_7_depths_norm = sigma_z_7_depths / baseline_depths[baseline_final_index]

# sigma_z_1_slopes_norm = sigma_z_1_slopes / baseline_slopes[baseline_final_index]
# sigma_z_2_slopes_norm = sigma_z_2_slopes / baseline_slopes[baseline_final_index]
# sigma_z_3_slopes_norm = sigma_z_3_slopes / baseline_slopes[baseline_final_index]
# sigma_z_4_slopes_norm = sigma_z_4_slopes / baseline_slopes[baseline_final_index]
# sigma_z_5_slopes_norm = sigma_z_5_slopes / baseline_slopes[baseline_final_index]
# sigma_z_6_slopes_norm = sigma_z_6_slopes / baseline_slopes[baseline_final_index]
# sigma_z_7_slopes_norm = sigma_z_7_slopes / baseline_slopes[baseline_final_index]

###############################################################################

#graphical params
linewidth = 5
text_x = 0.05
text_y = 0.86

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

xmin_v_short = -0.00001
xmax_v_short = 0.001

xmin_long = -0.02
xmax_long = 1.05

#create figure: 6 panels
fig2, axs = plt.subplots(5,3, figsize = (12,14))

width_short = axs[0, 0]
width = axs[0, 1]
width_hfp = axs[0, 2]

depth_short = axs[1, 0]
depth = axs[1, 1]
depth_hfp = axs[1, 2]

slope_short = axs[2, 0]
slope = axs[2, 1]
slope_hfp = axs[2, 2]

tau_bed_short = axs[3, 0]
tau_bed = axs[3, 1]
tau_bed_hfp = axs[3, 2]

tau_bank_short = axs[4, 0]
tau_bank = axs[4, 1]
tau_bank_hfp = axs[4, 2]

#WIDTH

width_vshort_min = 0.96
width_vshort_max = 1.08

width_min = 0.97
width_max = 3

#line style
runaway_depo_line = '--'

width_short.plot(time_array[:sigma_z_nofp_1_final_index], 
                 sigma_z_nofp_1_widths_norm[:sigma_z_nofp_1_final_index],
                 linewidth = linewidth,
                 color = sigma_z_1_color, alpha = alpha)
width_short.plot(time_array[:sigma_z_nofp_2_final_index], 
                 sigma_z_nofp_2_widths_norm[:sigma_z_nofp_2_final_index],
                 linewidth = linewidth,
                 color = sigma_z_2_color, alpha = alpha)
width_short.plot(time_array[:sigma_z_nofp_3_final_index], 
                 sigma_z_nofp_3_widths_norm[:sigma_z_nofp_3_final_index],
                 linewidth = linewidth, 
                 color = sigma_z_3_color, alpha = alpha)
width_short.plot(time_array[:sigma_z_nofp_4_final_index], 
                 sigma_z_nofp_4_widths_norm[:sigma_z_nofp_4_final_index],
                 linewidth = linewidth,
                 color = sigma_z_4_color, alpha = alpha)
width_short.plot(time_array[:sigma_z_nofp_5_final_index], 
                 sigma_z_nofp_5_widths_norm[:sigma_z_nofp_5_final_index],
                 linewidth = linewidth,
                 color = sigma_z_5_color, alpha = alpha,
                 linestyle = runaway_depo_line)
width_short.plot(time_array[:sigma_z_nofp_6_final_index], 
                 sigma_z_nofp_6_widths_norm[:sigma_z_nofp_6_final_index],
                 linewidth = linewidth,
                 color = sigma_z_6_color, alpha = alpha,
                 linestyle = runaway_depo_line)
width_short.plot(time_array[:sigma_z_nofp_7_final_index], 
                 sigma_z_nofp_7_widths_norm[:sigma_z_nofp_7_final_index],
                 linewidth = linewidth,
                 color = sigma_z_7_color, alpha = alpha,
                 linestyle = runaway_depo_line)

width_short.set_title('Months')
width_short.axhline(y = 1, color = 'gray', linestyle = '--')
width_short.get_xaxis().set_ticklabels([])
width_short.set_ylabel('Normalized width [-]')
width_short.text(text_x, text_y, 'A', transform=width_short.transAxes, fontsize = 20)
width_short.set_xlim(xmin_v_short, xmax_v_short)
width_short.set_ylim(width_vshort_min, width_vshort_max)


width.plot(time_array[:sigma_z_nofp_1_final_index], 
                 sigma_z_nofp_1_widths_norm[:sigma_z_nofp_1_final_index],
                 linewidth = linewidth,
                 color = sigma_z_1_color, alpha = alpha)
width.plot(time_array[:sigma_z_nofp_2_final_index], 
                 sigma_z_nofp_2_widths_norm[:sigma_z_nofp_2_final_index],
                 linewidth = linewidth,
                 color = sigma_z_2_color, alpha = alpha)
width.plot(time_array[:sigma_z_nofp_3_final_index], 
                 sigma_z_nofp_3_widths_norm[:sigma_z_nofp_3_final_index],
                 linewidth = linewidth, 
                 color = sigma_z_3_color, alpha = alpha)
width.plot(time_array[:sigma_z_nofp_4_final_index], 
                 sigma_z_nofp_4_widths_norm[:sigma_z_nofp_4_final_index],
                 linewidth = linewidth,
                 color = sigma_z_4_color, alpha = alpha)
width.plot(time_array[:sigma_z_nofp_5_final_index], 
                 sigma_z_nofp_5_widths_norm[:sigma_z_nofp_5_final_index],
                 linewidth = linewidth,
                 color = sigma_z_5_color, alpha = alpha,
                 linestyle = runaway_depo_line)
width.plot(time_array[:sigma_z_nofp_6_final_index], 
                 sigma_z_nofp_6_widths_norm[:sigma_z_nofp_6_final_index],
                 linewidth = linewidth,
                 color = sigma_z_6_color, alpha = alpha,
                 linestyle = runaway_depo_line)
width.plot(time_array[:sigma_z_nofp_7_final_index], 
                 sigma_z_nofp_7_widths_norm[:sigma_z_nofp_7_final_index],
                 linewidth = linewidth,
                 color = sigma_z_7_color, alpha = alpha,
                 linestyle = runaway_depo_line)

width.set_title('Years to decades')
width.axhline(y = 1, color = 'gray', linestyle = '--')
width.get_xaxis().set_ticklabels([])
#width.set_ylabel('Normalized width [-]')
width.text(text_x, text_y, 'B', transform=width.transAxes, fontsize = 20)
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

width_hfp.set_title('Decades to centuries')
width_hfp.axhline(y = 1, color = 'gray', linestyle = '--')
width_hfp.get_xaxis().set_ticklabels([])
#width_long.get_yaxis().set_ticklabels([])
#width_long.set_ylabel('Equilibrium width [m]')
width_hfp.text(text_x, text_y, 'C', transform=width_hfp.transAxes, fontsize = 20)
width_hfp.set_xlim(xmin_long, xmax_long)
width_hfp.set_ylim(0.95, 4)

#DEPTH
depth_min = 0.95
depth_max = 2.2


depth_short.plot(time_array[1:sigma_z_nofp_1_final_index], 
                 sigma_z_nofp_1_depths_norm[1:sigma_z_nofp_1_final_index],
                 linewidth = linewidth, label = '$z_0=0.1$ m', 
                 color = sigma_z_1_color, alpha = alpha)
depth_short.plot(time_array[1:sigma_z_nofp_2_final_index], 
                 sigma_z_nofp_2_depths_norm[1:sigma_z_nofp_2_final_index],
                 linewidth = linewidth, label = '$z_0=0.25$ m',
                 color = sigma_z_2_color, alpha = alpha)
depth_short.plot(time_array[1:sigma_z_nofp_3_final_index], 
                 sigma_z_nofp_3_depths_norm[1:sigma_z_nofp_3_final_index],
                 linewidth = linewidth, label = '$z_0=0.5$ m',
                 color = sigma_z_3_color, alpha = alpha)
depth_short.plot(time_array[1:sigma_z_nofp_4_final_index], 
                 sigma_z_nofp_4_depths_norm[1:sigma_z_nofp_4_final_index],
                 linewidth = linewidth, label = '$z_0=1$ m',
                 color = sigma_z_3_color, alpha = alpha)
depth_short.plot(time_array[1:sigma_z_nofp_5_final_index], 
                 sigma_z_nofp_5_depths_norm[1:sigma_z_nofp_5_final_index],
                 linewidth = linewidth,  label = '$z_0=2.5$ m',
                 color = sigma_z_5_color, alpha = alpha,
                 linestyle = runaway_depo_line)
depth_short.plot(time_array[1:sigma_z_nofp_6_final_index], 
                 sigma_z_nofp_6_depths_norm[1:sigma_z_nofp_6_final_index],
                 linewidth = linewidth, label = '$z_0=5$ m',
                 color = sigma_z_6_color, alpha = alpha,
                 linestyle = runaway_depo_line)
depth_short.plot(time_array[1:sigma_z_nofp_7_final_index], 
                 sigma_z_nofp_7_depths_norm[1:sigma_z_nofp_7_final_index],
                 linewidth = linewidth, label = '$z_0=10$ m',
                 color = sigma_z_7_color, alpha = alpha,
                 linestyle = runaway_depo_line)

depth_short.axhline(y = 1, color = 'gray', linestyle = '--')
depth_short.get_xaxis().set_ticklabels([])
depth_short.set_ylabel('Normalized depth [-]')
depth_short.text(text_x, text_y, 'D', transform=depth_short.transAxes, fontsize = 20)
depth_short.set_xlim(xmin_v_short, xmax_v_short)
#depth_short.set_xlim(xmin_short, xmax_short)
depth_short.set_ylim(0.6, 9)

depth.plot(time_array[1:sigma_z_nofp_1_final_index], 
                 sigma_z_nofp_1_depths_norm[1:sigma_z_nofp_1_final_index],
                 linewidth = linewidth, label = '$z_0=0.1$ m', 
                 color = sigma_z_1_color, alpha = alpha)
depth.plot(time_array[1:sigma_z_nofp_2_final_index], 
                 sigma_z_nofp_2_depths_norm[1:sigma_z_nofp_2_final_index],
                 linewidth = linewidth, label = '$z_0=0.25$ m',
                 color = sigma_z_2_color, alpha = alpha)
depth.plot(time_array[1:sigma_z_nofp_3_final_index], 
                 sigma_z_nofp_3_depths_norm[1:sigma_z_nofp_3_final_index],
                 linewidth = linewidth, label = '$z_0=0.5$ m',
                 color = sigma_z_3_color, alpha = alpha)
depth.plot(time_array[1:sigma_z_nofp_4_final_index], 
                 sigma_z_nofp_4_depths_norm[1:sigma_z_nofp_4_final_index],
                 linewidth = linewidth, label = '$z_0=1$ m',
                 color = sigma_z_3_color, alpha = alpha)
depth.plot(time_array[1:sigma_z_nofp_5_final_index], 
                 sigma_z_nofp_5_depths_norm[1:sigma_z_nofp_5_final_index],
                 linewidth = linewidth,  label = '$z_0=2.5$ m',
                 color = sigma_z_5_color, alpha = alpha,
                 linestyle = runaway_depo_line)
depth.plot(time_array[1:sigma_z_nofp_6_final_index], 
                 sigma_z_nofp_6_depths_norm[1:sigma_z_nofp_6_final_index],
                 linewidth = linewidth, label = '$z_0=5$ m',
                 color = sigma_z_6_color, alpha = alpha,
                 linestyle = runaway_depo_line)
depth.plot(time_array[1:sigma_z_nofp_7_final_index], 
                 sigma_z_nofp_7_depths_norm[1:sigma_z_nofp_7_final_index],
                 linewidth = linewidth, label = '$z_0=10$ m',
                 color = sigma_z_7_color, alpha = alpha,
                 linestyle = runaway_depo_line)

handles, labels = depth.get_legend_handles_labels()


depth.axhline(y = 1, color = 'gray', linestyle = '--')
depth.get_xaxis().set_ticklabels([])
#depth.set_ylabel('Normalized depth [-]')
depth.text(text_x, text_y, 'E', transform=depth.transAxes, fontsize = 20)
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
depth_hfp.text(text_x, text_y, 'F', transform=depth_hfp.transAxes, fontsize = 20)
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

slope_short_min = 0.65
slope_short_max = 1.3


slope_short.plot(time_array[:sigma_z_nofp_1_final_index], 
                 sigma_z_nofp_1_slopes_norm[:sigma_z_nofp_1_final_index],
                 linewidth = linewidth, color = sigma_z_1_color, alpha = alpha)
slope_short.plot(time_array[:sigma_z_nofp_2_final_index], 
                 sigma_z_nofp_2_slopes_norm[:sigma_z_nofp_2_final_index],
                 linewidth = linewidth, color = sigma_z_2_color, alpha = alpha)
slope_short.plot(time_array[:sigma_z_nofp_3_final_index], 
                 sigma_z_nofp_3_slopes_norm[:sigma_z_nofp_3_final_index],
                 linewidth = linewidth, color = sigma_z_3_color, alpha = alpha)
slope_short.plot(time_array[:sigma_z_nofp_4_final_index], 
                 sigma_z_nofp_4_slopes_norm[:sigma_z_nofp_4_final_index],
                 linewidth = linewidth, color = sigma_z_4_color, alpha = alpha)
slope_short.plot(time_array[:sigma_z_nofp_5_final_index], 
                 sigma_z_nofp_5_slopes_norm[:sigma_z_nofp_5_final_index],
                 linewidth = linewidth, color = sigma_z_5_color, alpha = alpha,
                 linestyle = runaway_depo_line)
slope_short.plot(time_array[:sigma_z_nofp_6_final_index], 
                 sigma_z_nofp_6_slopes_norm[:sigma_z_nofp_6_final_index],
                 linewidth = linewidth, color = sigma_z_6_color, alpha = alpha,
                 linestyle = runaway_depo_line)
slope_short.plot(time_array[:sigma_z_nofp_7_final_index], 
                 sigma_z_nofp_7_slopes_norm[:sigma_z_nofp_7_final_index],
                 linewidth = linewidth, color = sigma_z_7_color, alpha = alpha, 
                 zorder = 20,
                 linestyle = runaway_depo_line)

slope_short.get_xaxis().set_ticklabels([])
slope_short.set_ylabel('Normalized local slope [-]')
slope_short.axhline(y = 1, color = 'gray', linestyle = '--')
slope_short.text(text_x, text_y, 'G', transform=slope_short.transAxes, fontsize = 20)
slope_short.set_xlim(xmin_v_short, xmax_v_short)
slope_short.set_ylim(slope_short_min, slope_short_max)

slope.plot(time_array[:sigma_z_nofp_1_final_index], 
                 sigma_z_nofp_1_slopes_norm[:sigma_z_nofp_1_final_index],
                 linewidth = linewidth, color = sigma_z_1_color, alpha = alpha)
slope.plot(time_array[:sigma_z_nofp_2_final_index], 
                 sigma_z_nofp_2_slopes_norm[:sigma_z_nofp_2_final_index],
                 linewidth = linewidth, color = sigma_z_2_color, alpha = alpha)
slope.plot(time_array[:sigma_z_nofp_3_final_index], 
                 sigma_z_nofp_3_slopes_norm[:sigma_z_nofp_3_final_index],
                 linewidth = linewidth, color = sigma_z_3_color, alpha = alpha)
slope.plot(time_array[:sigma_z_nofp_4_final_index], 
                 sigma_z_nofp_4_slopes_norm[:sigma_z_nofp_4_final_index],
                 linewidth = linewidth, color = sigma_z_4_color, alpha = alpha)
slope.plot(time_array[:sigma_z_nofp_5_final_index], 
                 sigma_z_nofp_5_slopes_norm[:sigma_z_nofp_5_final_index],
                 linewidth = linewidth, color = sigma_z_5_color, alpha = alpha,
                 linestyle = runaway_depo_line)
slope.plot(time_array[:sigma_z_nofp_6_final_index], 
                 sigma_z_nofp_6_slopes_norm[:sigma_z_nofp_6_final_index],
                 linewidth = linewidth, color = sigma_z_6_color, alpha = alpha,
                 linestyle = runaway_depo_line)
slope.plot(time_array[:sigma_z_nofp_7_final_index], 
                 sigma_z_nofp_7_slopes_norm[:sigma_z_nofp_7_final_index],
                 linewidth = linewidth, color = sigma_z_7_color, alpha = alpha, 
                 zorder = 20,
                 linestyle = runaway_depo_line)


#slope.set_ylabel('Normalized local slope [-]')
slope.get_xaxis().set_ticklabels([])
slope.axhline(y = 1, color = 'gray', linestyle = '--')
slope.text(text_x, text_y, 'H', transform=slope.transAxes, fontsize = 20)
slope.set_xlim(xmin_short, xmax_short)
slope.set_ylim(slope_min, slope_max)


slope_legend = slope.legend(handles[::-1], labels[::-1], bbox_to_anchor=(1.15,1.88), loc = 'lower right', 
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

slope_hfp.get_xaxis().set_ticklabels([])
#slope_long.get_yaxis().set_ticklabels([])
#slope_long.set_ylabel('Equilibrium slope [m/m]')
slope_hfp.axhline(y = 1, color = 'gray', linestyle = '--')
#slope_short.set_xlim(-0.02, 1)
slope_hfp.set_ylim(0.6, 4)
slope_hfp.text(text_x, text_y, 'I', transform=slope_hfp.transAxes, fontsize = 20)
slope_hfp.set_xlim(-0.02, 1.05)



tau_bed_short.plot(time_array[1:sigma_z_nofp_1_final_index], 
                 sigma_z_nofp_1_tau_bed_norm[1:sigma_z_nofp_1_final_index],
                 linewidth = linewidth,
                 color = sigma_z_1_color, alpha = alpha)
tau_bed_short.plot(time_array[1:sigma_z_nofp_2_final_index], 
                 sigma_z_nofp_2_tau_bed_norm[1:sigma_z_nofp_2_final_index],
                 linewidth = linewidth,
                 color = sigma_z_2_color, alpha = alpha)
tau_bed_short.plot(time_array[1:sigma_z_nofp_3_final_index], 
                 sigma_z_nofp_3_tau_bed_norm[1:sigma_z_nofp_3_final_index],
                 linewidth = linewidth, 
                 color = sigma_z_3_color, alpha = alpha)
tau_bed_short.plot(time_array[1:sigma_z_nofp_4_final_index], 
                 sigma_z_nofp_4_tau_bed_norm[1:sigma_z_nofp_4_final_index],
                 linewidth = linewidth,
                 color = sigma_z_4_color, alpha = alpha)
tau_bed_short.plot(time_array[1:sigma_z_nofp_5_final_index], 
                 sigma_z_nofp_5_tau_bed_norm[1:sigma_z_nofp_5_final_index],
                 linewidth = linewidth,
                 color = sigma_z_5_color, alpha = alpha,
                 linestyle = runaway_depo_line)
tau_bed_short.plot(time_array[1:sigma_z_nofp_6_final_index], 
                 sigma_z_nofp_6_tau_bed_norm[1:sigma_z_nofp_6_final_index],
                 linewidth = linewidth,
                 color = sigma_z_6_color, alpha = alpha,
                 linestyle = runaway_depo_line)
tau_bed_short.plot(time_array[1:sigma_z_nofp_7_final_index], 
                 sigma_z_nofp_7_tau_bed_norm[1:sigma_z_nofp_7_final_index],
                 linewidth = linewidth,
                 color = sigma_z_7_color, alpha = alpha,
                 linestyle = runaway_depo_line)

tau_bed_short.set_xlim(xmin_v_short, xmax_v_short)
tau_bed_short.get_xaxis().set_ticklabels([])
tau_bed_short.set_ylabel('Norm. bed shear stress [-]')
tau_bed_short.set_ylim(0.75, 1.25)
tau_bed_short.axhline(y = 1, color = 'gray', linestyle = '--')
tau_bed_short.text(text_x, text_y, 'J', transform=tau_bed_short.transAxes, fontsize = 20)


tau_bed.plot(time_array[1:sigma_z_nofp_1_final_index], 
                 sigma_z_nofp_1_tau_bed_norm[1:sigma_z_nofp_1_final_index],
                 linewidth = linewidth,
                 color = sigma_z_1_color, alpha = alpha)
tau_bed.plot(time_array[1:sigma_z_nofp_2_final_index], 
                 sigma_z_nofp_2_tau_bed_norm[1:sigma_z_nofp_2_final_index],
                 linewidth = linewidth,
                 color = sigma_z_2_color, alpha = alpha)
tau_bed.plot(time_array[1:sigma_z_nofp_3_final_index], 
                 sigma_z_nofp_3_tau_bed_norm[1:sigma_z_nofp_3_final_index],
                 linewidth = linewidth, 
                 color = sigma_z_3_color, alpha = alpha)
tau_bed.plot(time_array[1:sigma_z_nofp_4_final_index], 
                 sigma_z_nofp_4_tau_bed_norm[1:sigma_z_nofp_4_final_index],
                 linewidth = linewidth,
                 color = sigma_z_4_color, alpha = alpha)
tau_bed.plot(time_array[1:sigma_z_nofp_5_final_index], 
                 sigma_z_nofp_5_tau_bed_norm[1:sigma_z_nofp_5_final_index],
                 linewidth = linewidth,
                 color = sigma_z_5_color, alpha = alpha,
                 linestyle = runaway_depo_line)
tau_bed.plot(time_array[1:sigma_z_nofp_6_final_index], 
                 sigma_z_nofp_6_tau_bed_norm[1:sigma_z_nofp_6_final_index],
                 linewidth = linewidth,
                 color = sigma_z_6_color, alpha = alpha,
                 linestyle = runaway_depo_line)
tau_bed.plot(time_array[1:sigma_z_nofp_7_final_index], 
                 sigma_z_nofp_7_tau_bed_norm[1:sigma_z_nofp_7_final_index],
                 linewidth = linewidth,
                 color = sigma_z_7_color, alpha = alpha,
                 linestyle = runaway_depo_line)

tau_bed.set_xlim(xmin_short, xmax_short)
tau_bed.get_xaxis().set_ticklabels([])
tau_bed.set_ylim(0.75, 1.25)
tau_bed.axhline(y = 1, color = 'gray', linestyle = '--')
tau_bed.text(text_x, text_y, 'K', transform=tau_bed.transAxes, fontsize = 20)


tau_bed_hfp.plot(time_array[1:sigma_z_nofp_1_final_index], 
                 sigma_z_nofp_1_tau_bed_norm[1:sigma_z_nofp_1_final_index],
                 linewidth = linewidth,
                 color = sigma_z_1_color, alpha = alpha)
tau_bed_hfp.plot(time_array[1:sigma_z_nofp_2_final_index], 
                 sigma_z_nofp_2_tau_bed_norm[1:sigma_z_nofp_2_final_index],
                 linewidth = linewidth,
                 color = sigma_z_2_color, alpha = alpha)
tau_bed_hfp.plot(time_array[1:sigma_z_nofp_3_final_index], 
                 sigma_z_nofp_3_tau_bed_norm[1:sigma_z_nofp_3_final_index],
                 linewidth = linewidth, 
                 color = sigma_z_3_color, alpha = alpha)
tau_bed_hfp.plot(time_array[1:sigma_z_nofp_4_final_index], 
                 sigma_z_nofp_4_tau_bed_norm[1:sigma_z_nofp_4_final_index],
                 linewidth = linewidth,
                 color = sigma_z_4_color, alpha = alpha)
tau_bed_hfp.plot(time_array[1:sigma_z_nofp_5_final_index], 
                 sigma_z_nofp_5_tau_bed_norm[1:sigma_z_nofp_5_final_index],
                 linewidth = linewidth,
                 color = sigma_z_5_color, alpha = alpha,
                 linestyle = runaway_depo_line)
tau_bed_hfp.plot(time_array[1:sigma_z_nofp_6_final_index], 
                 sigma_z_nofp_6_tau_bed_norm[1:sigma_z_nofp_6_final_index],
                 linewidth = linewidth,
                 color = sigma_z_6_color, alpha = alpha,
                 linestyle = runaway_depo_line)
tau_bed_hfp.plot(time_array[1:sigma_z_nofp_7_final_index], 
                 sigma_z_nofp_7_tau_bed_norm[1:sigma_z_nofp_7_final_index],
                 linewidth = linewidth,
                 color = sigma_z_7_color, alpha = alpha,
                 linestyle = runaway_depo_line)
tau_bed_hfp.scatter(time_array[sigma_z_nofp_1_final_index], 
                   sigma_z_nofp_1_tau_bed_norm[sigma_z_nofp_1_final_index],
                   color = sigma_z_1_color, alpha = alpha, s = 100)
tau_bed_hfp.scatter(time_array[sigma_z_nofp_2_final_index], 
                   sigma_z_nofp_2_tau_bed_norm[sigma_z_nofp_2_final_index],
                   color = sigma_z_2_color, alpha = alpha, s = 100)
tau_bed_hfp.scatter(time_array[sigma_z_nofp_3_final_index], 
                   sigma_z_nofp_3_tau_bed_norm[sigma_z_nofp_3_final_index],
                   color = sigma_z_3_color, alpha = alpha, s = 100)
tau_bed_hfp.scatter(time_array[sigma_z_nofp_4_final_index], 
                   sigma_z_nofp_4_tau_bed_norm[sigma_z_nofp_4_final_index],
                   color = sigma_z_4_color, alpha = alpha, s = 100)
tau_bed_hfp.scatter(time_array[sigma_z_nofp_5_final_index], 
                   sigma_z_nofp_5_tau_bed_norm[sigma_z_nofp_5_final_index],
                   color = sigma_z_5_color, alpha = alpha, s = 100)
tau_bed_hfp.scatter(time_array[sigma_z_nofp_6_final_index], 
                   sigma_z_nofp_6_tau_bed_norm[sigma_z_nofp_6_final_index],
                   color = sigma_z_6_color, alpha = alpha, s = 100)
tau_bed_hfp.scatter(time_array[sigma_z_nofp_7_final_index], 
                   sigma_z_nofp_7_tau_bed_norm[sigma_z_nofp_7_final_index],
                   color = sigma_z_7_color, alpha = alpha, s = 100)

tau_bed_hfp.set_xlim(xmin_long, xmax_long)
tau_bed_hfp.get_xaxis().set_ticklabels([])
tau_bed_hfp.set_ylim(0.75, 1.25)
tau_bed_hfp.axhline(y = 1, color = 'gray', linestyle = '--')
tau_bed_hfp.text(text_x, text_y, 'L', transform=tau_bed_hfp.transAxes, fontsize = 20)


tau_bank_short.plot(time_array[1:sigma_z_nofp_1_final_index], 
                 sigma_z_nofp_1_tau_bank_norm[1:sigma_z_nofp_1_final_index],
                 linewidth = linewidth,
                 color = sigma_z_1_color, alpha = alpha)
tau_bank_short.plot(time_array[1:sigma_z_nofp_2_final_index], 
                 sigma_z_nofp_2_tau_bank_norm[1:sigma_z_nofp_2_final_index],
                 linewidth = linewidth,
                 color = sigma_z_2_color, alpha = alpha)
tau_bank_short.plot(time_array[1:sigma_z_nofp_3_final_index], 
                 sigma_z_nofp_3_tau_bank_norm[1:sigma_z_nofp_3_final_index],
                 linewidth = linewidth, 
                 color = sigma_z_3_color, alpha = alpha)
tau_bank_short.plot(time_array[1:sigma_z_nofp_4_final_index], 
                 sigma_z_nofp_4_tau_bank_norm[1:sigma_z_nofp_4_final_index],
                 linewidth = linewidth,
                 color = sigma_z_4_color, alpha = alpha)
tau_bank_short.plot(time_array[1:sigma_z_nofp_5_final_index], 
                 sigma_z_nofp_5_tau_bank_norm[1:sigma_z_nofp_5_final_index],
                 linewidth = linewidth,
                 color = sigma_z_5_color, alpha = alpha,
                 linestyle = runaway_depo_line)
tau_bank_short.plot(time_array[1:sigma_z_nofp_6_final_index], 
                 sigma_z_nofp_6_tau_bank_norm[1:sigma_z_nofp_6_final_index],
                 linewidth = linewidth,
                 color = sigma_z_6_color, alpha = alpha,
                 linestyle = runaway_depo_line)
tau_bank_short.plot(time_array[1:sigma_z_nofp_7_final_index], 
                 sigma_z_nofp_7_tau_bank_norm[1:sigma_z_nofp_7_final_index],
                 linewidth = linewidth,
                 color = sigma_z_7_color, alpha = alpha,
                 linestyle = runaway_depo_line)

tau_bank_short.set_xlim(xmin_v_short, xmax_v_short)
tau_bank_short.set_xlabel('Normalized time [-]')
tau_bank_short.set_ylabel('Norm. bank shear stress [-]')
tau_bank_short.axhline(y = 1, color = 'gray', linestyle = '--')
tau_bank_short.set_ylim(0.95, 1.65)
tau_bank_short.text(text_x, text_y, 'M', transform=tau_bank_short.transAxes, fontsize = 20)


tau_bank.plot(time_array[1:sigma_z_nofp_1_final_index], 
                 sigma_z_nofp_1_tau_bank_norm[1:sigma_z_nofp_1_final_index],
                 linewidth = linewidth,
                 color = sigma_z_1_color, alpha = alpha)
tau_bank.plot(time_array[1:sigma_z_nofp_2_final_index], 
                 sigma_z_nofp_2_tau_bank_norm[1:sigma_z_nofp_2_final_index],
                 linewidth = linewidth,
                 color = sigma_z_2_color, alpha = alpha)
tau_bank.plot(time_array[1:sigma_z_nofp_3_final_index], 
                 sigma_z_nofp_3_tau_bank_norm[1:sigma_z_nofp_3_final_index],
                 linewidth = linewidth, 
                 color = sigma_z_3_color, alpha = alpha)
tau_bank.plot(time_array[1:sigma_z_nofp_4_final_index], 
                 sigma_z_nofp_4_tau_bank_norm[1:sigma_z_nofp_4_final_index],
                 linewidth = linewidth,
                 color = sigma_z_4_color, alpha = alpha)
tau_bank.plot(time_array[1:sigma_z_nofp_5_final_index], 
                 sigma_z_nofp_5_tau_bank_norm[1:sigma_z_nofp_5_final_index],
                 linewidth = linewidth,
                 color = sigma_z_5_color, alpha = alpha,
                 linestyle = runaway_depo_line)
tau_bank.plot(time_array[1:sigma_z_nofp_6_final_index], 
                 sigma_z_nofp_6_tau_bank_norm[1:sigma_z_nofp_6_final_index],
                 linewidth = linewidth,
                 color = sigma_z_6_color, alpha = alpha,
                 linestyle = runaway_depo_line)
tau_bank.plot(time_array[1:sigma_z_nofp_7_final_index], 
                 sigma_z_nofp_7_tau_bank_norm[1:sigma_z_nofp_7_final_index],
                 linewidth = linewidth,
                 color = sigma_z_7_color, alpha = alpha,
                 linestyle = runaway_depo_line)

tau_bank.set_xlim(xmin_short, xmax_short)
tau_bank.set_xlabel('Normalized time [-]')
tau_bank.axhline(y = 1, color = 'gray', linestyle = '--')
tau_bank.set_ylim(0.95, 1.65)
tau_bank.text(text_x, text_y, 'N', transform=tau_bank.transAxes, fontsize = 20)


tau_bank_hfp.plot(time_array[1:sigma_z_nofp_1_final_index], 
                 sigma_z_nofp_1_tau_bank_norm[1:sigma_z_nofp_1_final_index],
                 linewidth = linewidth,
                 color = sigma_z_1_color, alpha = alpha)
tau_bank_hfp.plot(time_array[1:sigma_z_nofp_2_final_index], 
                 sigma_z_nofp_2_tau_bank_norm[1:sigma_z_nofp_2_final_index],
                 linewidth = linewidth,
                 color = sigma_z_2_color, alpha = alpha)
tau_bank_hfp.plot(time_array[1:sigma_z_nofp_3_final_index], 
                 sigma_z_nofp_3_tau_bank_norm[1:sigma_z_nofp_3_final_index],
                 linewidth = linewidth, 
                 color = sigma_z_3_color, alpha = alpha)
tau_bank_hfp.plot(time_array[1:sigma_z_nofp_4_final_index], 
                 sigma_z_nofp_4_tau_bank_norm[1:sigma_z_nofp_4_final_index],
                 linewidth = linewidth,
                 color = sigma_z_4_color, alpha = alpha)
tau_bank_hfp.plot(time_array[1:sigma_z_nofp_5_final_index], 
                 sigma_z_nofp_5_tau_bank_norm[1:sigma_z_nofp_5_final_index],
                 linewidth = linewidth,
                 color = sigma_z_5_color, alpha = alpha,
                 linestyle = runaway_depo_line)
tau_bank_hfp.plot(time_array[1:sigma_z_nofp_6_final_index], 
                 sigma_z_nofp_6_tau_bank_norm[1:sigma_z_nofp_6_final_index],
                 linewidth = linewidth,
                 color = sigma_z_6_color, alpha = alpha,
                 linestyle = runaway_depo_line)
tau_bank_hfp.plot(time_array[1:sigma_z_nofp_7_final_index], 
                 sigma_z_nofp_7_tau_bank_norm[1:sigma_z_nofp_7_final_index],
                 linewidth = linewidth,
                 color = sigma_z_7_color, alpha = alpha,
                 linestyle = runaway_depo_line)
tau_bank_hfp.scatter(time_array[sigma_z_nofp_1_final_index], 
                   sigma_z_nofp_1_tau_bank_norm[sigma_z_nofp_1_final_index],
                   color = sigma_z_1_color, alpha = alpha, s = 100)
tau_bank_hfp.scatter(time_array[sigma_z_nofp_2_final_index], 
                   sigma_z_nofp_2_tau_bank_norm[sigma_z_nofp_2_final_index],
                   color = sigma_z_2_color, alpha = alpha, s = 100)
tau_bank_hfp.scatter(time_array[sigma_z_nofp_3_final_index], 
                   sigma_z_nofp_3_tau_bank_norm[sigma_z_nofp_3_final_index],
                   color = sigma_z_3_color, alpha = alpha, s = 100)
tau_bank_hfp.scatter(time_array[sigma_z_nofp_4_final_index], 
                   sigma_z_nofp_4_tau_bank_norm[sigma_z_nofp_4_final_index],
                   color = sigma_z_4_color, alpha = alpha, s = 100)
tau_bank_hfp.scatter(time_array[sigma_z_nofp_5_final_index], 
                   sigma_z_nofp_5_tau_bank_norm[sigma_z_nofp_5_final_index],
                   color = sigma_z_5_color, alpha = alpha, s = 100)
tau_bank_hfp.scatter(time_array[sigma_z_nofp_6_final_index], 
                   sigma_z_nofp_6_tau_bank_norm[sigma_z_nofp_6_final_index],
                   color = sigma_z_6_color, alpha = alpha, s = 100)
tau_bank_hfp.scatter(time_array[sigma_z_nofp_7_final_index], 
                   sigma_z_nofp_7_tau_bank_norm[sigma_z_nofp_7_final_index],
                   color = sigma_z_7_color, alpha = alpha, s = 100)

tau_bank_hfp.set_xlim(xmin_long, xmax_long)
tau_bank_hfp.set_xlabel('Normalized time [-]')
tau_bank_hfp.axhline(y = 1, color = 'gray', linestyle = '--')
tau_bank_hfp.set_ylim(0.95, 1.65)
tau_bank_hfp.text(text_x, text_y, 'O', transform=tau_bank_hfp.transAxes, fontsize = 20)


#plt.tight_layout()
fig2.savefig('figure_trajectories_condensed_3times_hires.png', dpi = 1000, bbox_inches = 'tight')
fig2.savefig('figure_trajectories_condensed_3times_lores.png', dpi = 100, bbox_inches = 'tight')



