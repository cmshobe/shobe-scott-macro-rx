#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 11:02:30 2024

@author: charlesshobe

sweep ONE AXIS of the parameter space in a parallelized way using multiprocessing
"""

from multiprocessing import Pool
import numpy as np
from macro_roughness_functions import channel_evolution_equilibrium
import os

# protect the entry point
if __name__ == '__main__':
    run_name = 'figure_4_test_refactor'
    n_steps = 15    
    sigma_z_values = np.logspace(-2, 1, n_steps)
    l_bed_obstacle = 0.
    l_bank_obstacle = 0.
    Q = 150 #m3/s
    Qs_in = 0.001 #m3/s
    theta_deg = 60. #degrees; bank angle
    theta = np.radians(theta_deg)
    d50 = 0.06 #m
    
    k_ero = 1.
    k_dep = 10.
    
    time_to_run = 1000000000 #s
    timestep = 1000 #s
    
    reach_length = 1000 #m
    
    baseline_name = 'trajectory_z0_baseline_rev1'
    print('loading baseline slope and width...')
    baseline_slopes = np.load('results/' + str(baseline_name) + '_slopes.npy')
    S = baseline_slopes[np.where(baseline_slopes > 0)[0][-1]] #last slope from baseline
    print(S)
    baseline_widths = np.load('results/' + str(baseline_name) + '_widths.npy')
    wb = baseline_widths[np.where(baseline_slopes > 0)[0][-1]]
    print(wb)
    
    h_floodplain = 1.95 + (S * reach_length)
    use_fp = 0 #0 for no, 1 for yes
    
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
    
    with open('results/' + str(run_name) + '_params.txt','w') as params_file:  #write out params dict to text file
        for key, value in param_dict.items():  
            params_file.write('%s: %s\n' % (key, value))
    
    with Pool(os.cpu_count() - 1) as p:
        
        #prepare arguments
        args = [(time_to_run, timestep, reach_length, Q, Qs_in, wb, theta,
                 sigma_z, l_bed_obstacle, l_bank_obstacle, k_ero, k_dep, S, d50, 
                 h_floodplain, use_fp) for sigma_z in param_array_tuple]
        
        #issue tasks to thread pool
        results = p.starmap(channel_evolution_equilibrium, args)
        
    results_array = np.array(results)
    save_array = np.column_stack((sigma_z_values, results_array))
    np.save('results/sweep_z0_values_' + str(run_name) + '.npy', save_array)