#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 9 Jan 2025 09:28:38

@author: charlesshobe

run one realization (for testing)
"""

import numpy as np
import pandas as pd
import copy as cp
import matplotlib.pyplot as plt
from case_study_function import channel_evolution


#######INITIALIZE###########################################################
#parameter values, etc

run_name = 'case_study_bestfit_low_z0'
k_ero = 0.2764506604263795  #ratio of bed to bank erodibility, unitless
k_dep = 88.11428991662648
theta_deg = 60. #degrees; bank angle
theta = np.radians(theta_deg)

#constants that are not model parameters
#e = 1.5 #range of 1.33-2; Rickenmann, 2011

time_to_run = 158803200#5000000000 #1,838 days between 2019 and 2024 survey = 158,803,200 s
timestep = 100 #CHECK UNITS
print_interval = 10000000
save_interval = 100
reach_length = 117.1 #meters
use_fp = 1 #0 for unconfined, 1 for confined

#read in starting equilibrium S and w values

S = 0.007#0.00164 #setting slope for now
wb  = 104#20#25.053 #initial basal width [m]

d50 = 0.03 #m !!!connect this to z0 to eliminate an arbitrary param choice

h_floodplain = 1.947 + (S * reach_length)

#bring in Q data

Q_time_series = pd.read_csv('nf_sno_q.txt', sep = '\t', header = 29).drop(columns = ['5s', '15s', '6s', '10s']).rename(columns={"20d": "date_time", "14n": "Q (cfs)"})
Q_time_series['Q (cms)'] = Q_time_series['Q (cfs)'] * 0.0283168466

#trim discharge time series to known dates:
    #2019: 2019-03-20
    #2020: 2020-04-08
    #2022: 2022-04-06
    #2024: 2024-03-31
    
Q_time_series = Q_time_series.drop(index = range(7532)) #drop dates before noon on first survey day
Q_time_series = Q_time_series.drop(index = range(200000, 208247)) #drop dates after noon on last survey day

Q_time_series_np = Q_time_series['Q (cms)'].to_numpy()
expansion_factor = int((15 * 60) / timestep)
Q_time_series_expanded = np.repeat(Q_time_series_np, expansion_factor)

param_dict = {
              'k_ero': k_ero,
              'k_dep': k_dep,
              'theta': theta_deg,
              'd50': d50,
              'h_fp': h_floodplain,
              'runtime': time_to_run,
              'timestep': timestep} #dict holds only vars that are unchanging

with open('results/' + str(run_name) + '_params.txt','w') as params_file:  #write out params dict to text file
    for key, value in param_dict.items():  
        params_file.write('%s: %s\n' % (key, value))
        
#define input time series of sigma_z, l_bed, l_bank
sigma_z_vals = np.array([0.21, 0.24, 0.23])
l_bed_obst_vals = np.array([11.0, 18.9, 17.1])
l_bank_obst_vals = np.array([0.65, 0.61, 0.86])

morph_vars_perturb = wood(time_to_run,
     timestep,
     reach_length,
     Q_time_series_expanded,
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
     l_bank_obst_vals)

save_widths = morph_vars_perturb[0]
save_slopes = morph_vars_perturb[1]
save_depths = morph_vars_perturb[2]
save_depths_r = morph_vars_perturb[3]
save_qs_out = morph_vars_perturb[4]
save_fw = morph_vars_perturb[5]
save_tau_bed = morph_vars_perturb[6]
save_tau_bank = morph_vars_perturb[7]
save_S_r = morph_vars_perturb[8]
save_fr_over_f0 = morph_vars_perturb[9]
save_chan_depths = morph_vars_perturb[10]
teq = morph_vars_perturb[11]
which_regime = morph_vars_perturb[12]


#save everything as npys
np.save('results/' + run_name + '_widths.npy', save_widths)
np.save('results/' + run_name +'_slopes.npy', save_slopes)
np.save('results/' + run_name +'_e_slopes.npy', save_S_r)
np.save('results/' + run_name +'_depths_r.npy', save_depths_r)
np.save('results/' + run_name +'_qs_out.npy', save_qs_out)
np.save('results/' + run_name +'_tau_bed.npy', save_tau_bed)
np.save('results/' + run_name +'_tau_bank.npy', save_tau_bank)
np.save('results/' + run_name +'_fr_over_f0.npy', save_fr_over_f0)
np.save('results/' + run_name +'_chan_depths.npy', save_chan_depths)
np.save('results/' + run_name +'_teq.npy', teq)
np.save('results/' + run_name +'_regime.npy', which_regime)
