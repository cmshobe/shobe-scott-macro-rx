#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 9 Jan 2025 09:28:38

@author: charlesshobe

run one realization (for testing)
"""

import numpy as np
import copy as cp
import matplotlib.pyplot as plt
from wood_trajectory_function import wood


#######INITIALIZE###########################################################
#parameter values, etc

run_name = 'trajectory_z0_0point25'
Q = 150 #m^3/s water discharge
Qs_in = .001 #m^3/s sediment flux in
sigma_z = 0.25 #roughness length scale including wood (ideally back-calculate from literature)
l_bed_obstacle = 0. #fraction of bed covered by wood
l_bank_obstacle = 0. #fraction of banks covered by wood
k_ero = 2. #ratio of bed to bank erodibility, unitless
k_dep = 20.
theta_deg = 60. #degrees; bank angle
theta = np.radians(theta_deg)

#constants that are not model parameters
#e = 1.5 #range of 1.33-2; Rickenmann, 2011

time_to_run = 5000000000#5000000000 #work out time units...
timestep = 100 #CHECK UNITS
print_interval = 10000000
save_interval = 100
reach_length = 10 #meters
#h_floodplain = 2.
use_fp = 0 #0 for unconfined, 1 for confined

#read in starting equilibrium S and w values

if run_name == 'trajectory_z0_baseline':
    S = 0.001#0.00164 #setting slope for now
    wb  = 50#20#25.053 #initial basal width [m]
else:
    baseline_name = 'trajectory_z0_baseline'
    print('loading baseline slope and width...')
    baseline_slopes = np.load('results/' + str(baseline_name) + '_slopes.npy')
    S = baseline_slopes[np.where(np.load('results/' + str(baseline_name) + '_slopes.npy') > 0)[0][-1]] #last slope from baseline
    print(S)
    baseline_widths = np.load('results/' + str(baseline_name) + '_widths.npy')
    wb = baseline_widths[np.where(np.load('results/' + str(baseline_name) + '_widths.npy') > 0)[0][-1]]
    print(wb)

d50 = 0.06 #m !!!connect this to z0 to eliminate an arbitrary param choice

h_floodplain = 1.95 + (S * reach_length)

param_dict = {'sigma_z': sigma_z,
              'l_bed_obstacle': l_bed_obstacle,
              'l_bank_obstacle': l_bank_obstacle,
              'k_ero': k_ero,
              'k_dep': k_dep,
              'Q': Q,
              'Qs_in': Qs_in,
              'theta': theta_deg,
              'd50': d50,
              'h_fp': h_floodplain,
              'runtime': time_to_run,
              'timestep': timestep} #dict holds only vars that are unchanging

with open('results/' + str(run_name) + '_params.txt','w') as params_file:  #write out params dict to text file
    for key, value in param_dict.items():  
        params_file.write('%s: %s\n' % (key, value))

morph_vars_perturb = wood(time_to_run,
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
     save_interval)

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


