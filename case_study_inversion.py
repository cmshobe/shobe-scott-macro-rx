#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 11 Mar 2025 09:28:38

@author: charlesshobe

differential evolution optimization"""

import numpy as np
import pandas as pd
from macro_roughness_functions import channel_evolution_inversion
from scipy.optimize import differential_evolution

#######INITIALIZE###########################################################
#parameter values, etc


np.random.seed(987654)
run_name = 'case_study_test_refactor'
theta_deg = 60. #degrees; bank angle
theta = np.radians(theta_deg)

#constants that are not model parameters
#e = 1.5 #range of 1.33-2; Rickenmann, 2011

time_to_run = 158803200#5000000000 #1,838 days between 2019 and 2024 survey = 158,803,200 s
timestep = 100 #CHECK UNITS
print_interval = 1000000000
save_interval = 100
reach_length = 1100.2 #meters
#h_floodplain = 2.
use_fp = 1 #0 for unconfined, 1 for confined

S = 0.0029#0.00164 #setting slope for now
wb  = 43.6#20#25.053 #initial basal width [m]

d50 = 0.03 #m !!!connect this to z0 to eliminate an arbitrary param choice
h_floodplain = 2.95 + (S * reach_length)

#bring in Q data

#Q_time_series = pd.read_csv('sf_sno_q.txt', sep = '\t', header = 27).drop(columns = ['5s', '15s', '6s', '10s', '14n.1', '10s.1']).rename(columns={"20d": "date_time", "14n": "Q (cfs)"})
#Q_time_series['Q (cms)'] = Q_time_series['Q (cfs)'] * 0.0283168466

Q_time_series = pd.read_parquet('inputs/sf_sno_Q.parquet')
Q_time_series[(Q_time_series['datetime'] >= '2019-03-20 12:00:00') & (Q_time_series['datetime'] <= '2024-03-31 12:00:00')]


#trim discharge time series to known dates:
    #2019: 2019-03-20
    #2020: 2020-04-08
    #2022: 2022-04-06
    #2024: 2024-03-31
    
#Q_time_series = Q_time_series.drop(index = range(7532)) #drop dates before noon on first survey day
#Q_time_series = Q_time_series.drop(index = range(200000, 208247)) #drop dates after noon on last survey day

Q_time_series_np = Q_time_series['Q (cms)'].to_numpy()
expansion_factor = int((15 * 60) / timestep)
Q_time_series_expanded = np.repeat(Q_time_series_np, expansion_factor)

param_dict = {
              'theta': theta_deg,
              'd50': d50,
              'h_fp': h_floodplain,
              'runtime': time_to_run,
              'timestep': timestep} #dict holds only vars that are unchanging

with open('results/' + str(run_name) + '_params.txt','w') as params_file:  #write out params dict to text file
    for key, value in param_dict.items():  
        params_file.write('%s: %s\n' % (key, value))

bounds = [(np.log10(0.01), np.log10(10)), (1, 120)] #order: k*ero, k*dep

#define known time series of w and h
w_obs = np.array([45., 46., 45.9])#np.array([108, 114, 119])
h_obs = np.array([0.0028, 0.0032, 0.003]) * reach_length #convert slope to elev above baselevel elev of 0 m

#define input time series of sigma_z, l_bed, l_bank
sigma_z_vals = np.array([0.13, 0.13, 0.14])#np.array([0.21, 0.24, 0.23])
l_bed_obst_vals = np.array([1.74, 1.35, 1.84])#np.array([11.0, 18.9, 17.1])
l_bank_obst_vals = np.array([1.91, 1.23, 1.84])#np.array([0.65, 0.61, 0.86])

#define fixed arguments
args = (time_to_run, timestep, reach_length, Q_time_series_expanded, wb, theta,
        S, d50, h_floodplain,
        use_fp, print_interval, save_interval, w_obs, h_obs, run_name,
        sigma_z_vals, l_bed_obst_vals, l_bank_obst_vals)

pop_size = 1#100
max_iter = 1#25
recomb = 0.5

#define initial array for optimization that ensures full param space coverage:
init_array_k_ero = np.linspace(bounds[0][0], bounds[0][1], pop_size)
init_array_k_dep = np.linspace(bounds[1][0], bounds[1][1], pop_size)

init_array = np.array([init_array_k_ero, init_array_k_dep]).T

optimization_results = differential_evolution(channel_evolution_inversion, bounds, args = args,
                                              maxiter = max_iter, popsize = pop_size,
                                              recombination = recomb, #default is 0.7
                                              polish = False)



