#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Run a suite of simulations that assess equilibrium channel response to
different values of the bed cover length w_bed_roughness. Output from this 
script is used to generate figure 5 in the paper.

Created February 2026 by @author: charlesshobe
"""

from multiprocessing import Pool
import numpy as np
from macro_roughness_functions import channel_evolution_equilibrium
import os

# protect the entry point
if __name__ == '__main__':
    run_name = 'figure_5'
    n_steps = 15
    z0 = 0.1
    w_bed_roughness_values = np.linspace(0, 120, n_steps)
    l_bank_roughness = 0.
    Q = 150 #m3/s
    Qs_in = 0.001 #m3/s
    theta_deg = 60. #degrees; bank angle
    theta = np.radians(theta_deg)
    d50 = 0.06 #m
    
    k_ero = 1.
    k_dep = 10.
    
    time_to_run = 200000000000 #s
    timestep = 1000 #s
    
    reach_length = 1000 #m
    
    baseline_name = 'trajectory_z0_baseline_rev1'
    print('loading baseline slope and width...')
    baseline_slopes = np.load('results/' + str(baseline_name) + '_slopes.npy')
    S = baseline_slopes[np.where(baseline_slopes > 0)[0][-1]]
    print(S)
    baseline_widths = np.load('results/' + str(baseline_name) + '_widths.npy')
    wb = baseline_widths[np.where(baseline_slopes > 0)[0][-1]]
    print(wb)
    
    h_floodplain = 5. + (S * reach_length)
    use_fp = 1 #0 for no, 1 for yes
    
    param_array_tuple = tuple(w_bed_roughness_values)
    save_array = np.zeros((len(w_bed_roughness_values), 1))
    
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
                  'timestep': timestep}
    
    #write out params dict to text file
    with open('results/' + str(run_name) + '_params.txt','w') as params_file:
        for key, value in param_dict.items():  
            params_file.write('%s: %s\n' % (key, value))
    
    with Pool(os.cpu_count() - 1) as p:
        
        #prepare arguments
        args = [(time_to_run, timestep, reach_length, Q, Qs_in, wb, theta,
                 z0, w_bed_roughness, l_bank_roughness, k_ero, k_dep, S, d50, 
                 h_floodplain, use_fp) for w_bed_roughness in param_array_tuple]
        
        #issue tasks to thread pool
        results = p.starmap(channel_evolution_equilibrium, args)
        
    results_array = np.array(results)
    save_array = np.column_stack((w_bed_roughness_values, results_array))
    np.save('results/sweep_bed_cover_values_' + str(run_name) + '.npy', save_array)