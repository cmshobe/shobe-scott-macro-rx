#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Run an inverse modeling experiment in which the differential evolution 
algorithm is used to converge on best-fit values of the erosion and deposition
constants by comparing modeled channel geometry against field measurements.
Output from this script is used to generate figure 9 in the paper using data 
from the SF Snoqualmie River case study.

Created February 2026 by @author: charlesshobe
"""

import numpy as np
import pandas as pd
from macro_roughness_functions import channel_evolution_inversion
from scipy.optimize import differential_evolution
from datetime import datetime

#######INITIALIZE###########################################################
#parameter values, etc

np.random.seed(987654)
run_name = 'figure_9_inversion_high_z0'
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
timestep = 100 #s
print_interval = 1000000000
reach_length = 1100.2 #meters
use_fp = 1 #0 for unconfined, 1 for confined

S = 0.0029#0.00164 #setting slope for now
wb  = 43.6#20#25.053 #initial basal width [m]

d50 = 0.03 #m
h_floodplain = 2.95 + (S * reach_length)

#bring in Q data and trim to date bounds
Q_time_series = pd.read_parquet('inputs/sf_sno_Q.parquet')
Q_time_series[(Q_time_series['datetime'] >= survey_2019_date) & 
              (Q_time_series['datetime'] <= survey_2024_date)]
Q_time_series_np = Q_time_series['Q (cms)'].to_numpy()
expansion_factor = int((15 * 60) / timestep)
Q_time_series_expanded = np.repeat(Q_time_series_np, expansion_factor)

param_dict = {'theta': theta_deg,
              'd50': d50,
              'h_fp': h_floodplain,
              'runtime': time_to_run,
              'timestep': timestep} 

#write out params dict to text file
with open('results/' + str(run_name) + '_params.txt','w') as params_file:
    for key, value in param_dict.items():  
        params_file.write('%s: %s\n' % (key, value))

bounds = [(np.log10(0.01), np.log10(10)), (1, 120)] #order: k*ero, k*dep

#define known time series of w and h
w_obs = np.array([45., 46., 45.9])
#convert slope to elev above baselevel elev of 0 m
h_obs = np.array([0.0028, 0.0032, 0.003]) * reach_length

#define input time series of z0, l_bed, l_bank

#low z0 array: np.array([0.13, 0.13, 0.14])
#high z0 array: np.array([0.22, 0.20, 0.23])

z0_vals = np.array([0.22, 0.20, 0.23])
w_bed_roughness_vals = np.array([1.74, 1.35, 1.84])
l_bank_roughness_vals = np.array([1.91, 1.23, 1.84])

#define fixed arguments
args = (time_to_run, timestep, reach_length, Q_time_series_expanded, wb, theta,
        S, d50, h_floodplain,
        use_fp, print_interval, w_obs, h_obs, run_name,
        z0_vals, w_bed_roughness_vals, l_bank_roughness_vals,
        time_checkpoint_1, time_checkpoint_2)

pop_size = 100
max_iter = 25
recomb = 0.5

#define initial array for optimization that ensures full param space coverage:
init_array_k_ero = np.linspace(bounds[0][0], bounds[0][1], pop_size)
init_array_k_dep = np.linspace(bounds[1][0], bounds[1][1], pop_size)

init_array = np.array([init_array_k_ero, init_array_k_dep]).T

optimization_results = differential_evolution(channel_evolution_inversion, 
                                              bounds, args = args,
                                              maxiter = max_iter, 
                                              popsize = pop_size,
                                              recombination = recomb,
                                              polish = False)



