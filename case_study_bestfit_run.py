#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Run a single realization of the model using data from the field case study and 
the best fit erosion and deposition constant values constrained by the 
inversion. Output from this script is used to generate figure 9 in the paper 
using data from the SF Snoqualmie River case study.

Created February 2026 by @author: charlesshobe
"""

import numpy as np
import pandas as pd
from macro_roughness_functions import channel_evolution_bestfit
from datetime import datetime

#######INITIALIZE###########################################################
#parameter values, etc

run_name = 'figure_9_bestfit_high_z0'
inversion_record_name = 'results/figure_9_inversion_high_z0_inversion_record.csv'
colnames = ['k_ero', 'k_dep', 'misfit']
data = (pd.read_csv(inversion_record_name, header = None, names = colnames)
        .sort_values(by = 'misfit', ascending = False))


#get bestfit k_ero and k_dep from inversion record

k_ero = data.k_ero.iloc[-1]  #ratio of bed to bank erodibility, unitless
k_dep = data.k_dep.iloc[-1]
theta_deg = 60. #degrees; bank angle
theta = np.radians(theta_deg)

#get survey times
datetime_format_code = '%Y-%m-%d %H:%M:%S'
survey_2019_date = datetime.strptime('2019-03-21 12:00:00', 
                                     datetime_format_code)
survey_2020_date = datetime.strptime('2020-04-08 12:00:00', 
                                     datetime_format_code)
survey_2022_date = datetime.strptime('2022-04-06 12:00:00', 
                                     datetime_format_code)
survey_2024_date = datetime.strptime('2024-03-31 12:00:00', 
                                     datetime_format_code)

duration_2019_2020 = survey_2020_date - survey_2019_date
time_checkpoint_1 = duration_2019_2020.total_seconds()
duration_2020_2022 = survey_2022_date - survey_2020_date
time_checkpoint_2 = duration_2020_2022.total_seconds() + time_checkpoint_1
duration_2019_2024 = survey_2024_date - survey_2019_date

time_to_run = duration_2019_2024.total_seconds()
timestep = 100 #CHECK UNITS
print_interval = 10000000
save_interval = 100
reach_length = 1100.2 #meters
use_fp = 1 #0 for unconfined, 1 for confined

#starting S and wb values

S = 0.0029
wb  = 43.6 #m

d50 = 0.03 #m 
h_floodplain = 2.95 + (S * reach_length)

#bring in Q data and trim to date bounds
Q_time_series = pd.read_parquet('inputs/sf_sno_Q.parquet')
Q_time_series[(Q_time_series['datetime'] >= survey_2019_date) & 
              (Q_time_series['datetime'] <= survey_2024_date)]
Q_time_series_np = Q_time_series['Q (cms)'].to_numpy()
expansion_factor = int((15 * 60) / timestep)
Q_time_series_expanded = np.repeat(Q_time_series_np, expansion_factor)

param_dict = {'k_ero': k_ero,
              'k_dep': k_dep,
              'theta': theta_deg,
              'd50': d50,
              'h_fp': h_floodplain,
              'runtime': time_to_run,
              'timestep': timestep}

#write out params dict to text file
with open('results/' + str(run_name) + '_params.txt','w') as params_file:
    for key, value in param_dict.items():  
        params_file.write('%s: %s\n' % (key, value))
        
#define input time series of z0, l_bed, l_bank

#low z0 array: np.array([0.13, 0.13, 0.14])
#high z0 array: np.array([0.22, 0.20, 0.23])

z0_vals = np.array([0.22, 0.20, 0.23])
w_bed_roughness_vals = np.array([1.74, 1.35, 1.84])
l_bank_roughness_vals = np.array([0.95, 0.61, 0.92])

morph_vars_perturb = channel_evolution_bestfit(time_to_run,
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
     z0_vals,
     w_bed_roughness_vals,
     l_bank_roughness_vals)

save_widths = morph_vars_perturb[0]
save_slopes = morph_vars_perturb[1]
save_depths_r = morph_vars_perturb[2]
save_qs_out = morph_vars_perturb[3]
save_fw = morph_vars_perturb[4]
save_tau_bed = morph_vars_perturb[5]
save_tau_bank = morph_vars_perturb[6]
save_S_r = morph_vars_perturb[7]
save_fr_over_f0 = morph_vars_perturb[8]
save_chan_depths = morph_vars_perturb[9]
teq = morph_vars_perturb[10]

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
