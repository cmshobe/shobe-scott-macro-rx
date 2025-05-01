#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 11:02:30 2024

@author: charlesshobe

sweep ONE AXIS of the parameter space in a parallelized way using multiprocessing
"""

from multiprocessing import Pool
from functools import partial
import numpy as np
from wood_function import wood
import time
import os

# protect the entry point
if __name__ == '__main__':
    run_name = 'figure_4'
    n_steps = 15
    #total_runs = n_steps**3
    
    sigma_z_values = np.logspace(-2, 1, n_steps)
    #sigma_z = 1
    #l_bed_obstacle_values = np.linspace(0, 250, n_steps)
    l_bed_obstacle = 0.
    #l_bank_obstacle_values = np.linspace(0, 2.5, n_steps)
    l_bank_obstacle = 0.
    Q = 150 #m3/s
    Qs_in = 0.001 #m3/s
    theta_deg = 60. #degrees; bank angle
    theta = np.radians(theta_deg)
    d50 = 0.06 #m
    
    k_ero = 2.
    k_dep = 20.
    
    time_to_run = 10000000000 #s
    timestep = 100 #s
    
    reach_length = 10 #m
    S = 0.0055593355305988265#0.005208958660154328#0.006740351232927963
    wb = 51.00417998438822#54.349856075608386#51.81330955924939
    
    h_floodplain = 1.95 + (S * reach_length)
    use_fp = 0 #0 for no, 1 for yes
    
    #make array of all combinations of three parameters of interest
    #in the resulting array...
        #column 0 is z0
        #column 1 is k_ratio
        #column 3 is d_ratio
    
    #param_array_variables = np.array(np.meshgrid(sigma_z_values, l_bed_obstacle_values, l_bank_obstacle_values)).T.reshape(-1, 3)
    #param_array_constants = np.array([np.repeat(fc_bed, total_runs), np.repeat(fc_bank, total_runs)]).T
    
    #param_array = np.hstack((param_array_variables, param_array_constants))
    
    param_array_tuple = tuple( sigma_z_values)
    save_array = np.zeros((len(sigma_z_values), 1))
    
    param_dict = {'n_runs': n_steps,
                  'k_ero': k_ero,
                  'k_dep': k_dep,
                  'Q': Q,
                  'Qs_in': Qs_in,
                  'theta': theta_deg,
                  'd50': d50,
                  'h_fp': h_floodplain,
                  'initial_slope': S,
                  'initial_width': wb,
                  'reach_length': reach_length,
                  'runtime': time_to_run,
                  'timestep': timestep} #dict holds only vars that are unchanging
    
    with open('params_' + str(run_name) + '.txt','w') as params_file:  #write out params dict to text file
        for key, value in param_dict.items():  
            params_file.write('%s: %s\n' % (key, value))
    
    with Pool(os.cpu_count() - 1) as p:
        
        #prepare arguments
        args = [(time_to_run, timestep, reach_length, Q, Qs_in, wb, theta,
                 sigma_z, l_bed_obstacle, l_bank_obstacle, k_ero, k_dep, S, d50, 
                 h_floodplain, use_fp) for sigma_z in param_array_tuple]
        
        #issue tasks to thread pool
        results = p.starmap(wood, args)
        
        #output = [p.get() for p in results]

    

        
    results_array = np.array(results)
    save_array = np.column_stack((sigma_z_values, results_array))
    np.save('sweep_z0_values_' + str(run_name) + '.npy', save_array)