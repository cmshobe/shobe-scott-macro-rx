#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Run a single model realization while recording information about flow and 
morphology over time in the modeled channel. Output from this script is used to
generate figure 8 in the paper.

Created February 2026 by @author: charlesshobe
"""

import numpy as np
from macro_roughness_functions import channel_evolution_trajectory
import time

start_time = time.time()

#######INITIALIZE###########################################################
#parameter values, etc

run_name = 'figure_8_z0_0point1'
Q = 150 #m^3/s water discharge
Qs_in = .001 #m^3/s sediment flux in
z0 = 0.1 #roughness length scale including macro-rx
w_bed_roughness = 0. #fraction of bed covered by wood
l_bank_roughness = 0. #fraction of banks covered by wood
k_ero = 1. #ratio of bed to bank erodibility, unitless
k_dep = 10. #ratio of bed to bank deposition, unitless
theta_deg = 60. #degrees; bank angle
theta = np.radians(theta_deg)

time_to_run = 200000000000
timestep = 1000 
print_interval = 200000000000
save_interval = 10000
reach_length = 1000 #meters
use_fp = 0 #0 for unconfined, 1 for confined

#read in starting equilibrium S and w values

if run_name == 'trajectory_z0_baseline_rev1':
    S = 0.001#0.00164 #setting slope for now
    wb  = 50#20#25.053 #initial basal width [m]
else:
    baseline_name = 'trajectory_z0_baseline_rev1'
    print('loading baseline slope and width...')
    baseline_slopes = np.load('results/' + str(baseline_name) + '_slopes.npy')
    S = baseline_slopes[np.where(baseline_slopes > 0)[0][-1]]
    print(S)
    baseline_widths = np.load('results/' + str(baseline_name) + '_widths.npy')
    wb = baseline_widths[np.where(baseline_slopes > 0)[0][-1]]
    print(wb)

d50 = 0.06 #m

h_floodplain = 5. + (S * reach_length)

param_dict = {'z0': z0,
              'w_bed_roughness': w_bed_roughness,
              'l_bank_roughness': l_bank_roughness,
              'k_ero': k_ero,
              'k_dep': k_dep,
              'Q': Q,
              'Qs_in': Qs_in,
              'theta': theta_deg,
              'd50': d50,
              'h_fp': h_floodplain,
              'runtime': time_to_run,
              'timestep': timestep}

#write out params dict to text file
with open('results/' + str(run_name) + '_params.txt','w') as params_file:
    for key, value in param_dict.items():  
        params_file.write('%s: %s\n' % (key, value))

morph_vars_perturb = channel_evolution_trajectory(time_to_run,
     timestep,
     reach_length,
     Q,
     Qs_in,
     wb,
     theta,
     z0,
     w_bed_roughness,
     l_bank_roughness,
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
save_depths_r = morph_vars_perturb[2]
save_qs_out = morph_vars_perturb[3]
save_fw = morph_vars_perturb[4]
save_tau_total = morph_vars_perturb[5]
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
np.save('results/' + run_name +'_tau_total.npy', save_tau_total)
np.save('results/' + run_name +'_tau_bed.npy', save_tau_bed)
np.save('results/' + run_name +'_tau_bank.npy', save_tau_bank)
np.save('results/' + run_name +'_fr_over_f0.npy', save_fr_over_f0)
np.save('results/' + run_name +'_chan_depths.npy', save_chan_depths)
np.save('results/' + run_name +'_teq.npy', teq)

end_time = time.time()

print('Runtime: ' + str(end_time - start_time) + 'seconds')
