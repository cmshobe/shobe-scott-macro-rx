#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 21:44:08 2025

@author: charlesshobe

Create results figure: outputs w, d, S+Sr,  and f/fr as f(sigma_z)
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#run from which to get data
run_name = 'figure_4_rev1_L1000_tol1e-13_dt1000_TESTkero1kdep10'
data = np.load('sweep_z0_values_' + str(run_name) + '.npy')

#convert to pandas dataframe for seaborn compatibility
df = pd.DataFrame({'sigma_z': data[:, 0], 
                   'width': data[:, 1], 
                   'depth': data[:, 2],
                   'slope': data[:, 3],
                   'e_slope': data[:, 4],
                   'tau_bed': data[:, 5],
                   'tau_bank': data[:, 6],
                   'fr/f0': data[:, 7],
                   'teq': data[:, 8]})

#w_r = wb + 2 * (d_r / np.tan(theta))
df['w_r'] = df['width'] + 2 * (df['depth'] / np.tan(np.radians(60)))

#normalize outputs (except fr/f) to output value for sigma_z = 0.01 m
min_rx = min(df['sigma_z']) #minimum sigma_z used
df['width_norm'] = df['width'] / float(df['width'][df['sigma_z'] == min_rx].iloc[0])
df['w_r_norm'] = df['w_r'] / float(df['w_r'][df['sigma_z'] == min_rx].iloc[0])
df['depth_norm'] = df['depth'] / float(df['depth'][df['sigma_z'] == min_rx].iloc[0])
df['slope_norm'] = df['slope'] / float(df['slope'][df['sigma_z'] == min_rx].iloc[0])
df['e_slope_norm'] = df['e_slope'] / float(df['e_slope'][df['sigma_z'] == min_rx].iloc[0])
df['tau_bed_norm'] = df['tau_bed'] / float(df['tau_bed'][df['sigma_z'] == min_rx].iloc[0])
df['tau_bank_norm'] = df['tau_bank'] / float(df['tau_bank'][df['sigma_z'] == min_rx].iloc[0])
df['fr/f0 norm'] = df['fr/f0'] / float(df['fr/f0'][df['sigma_z'] == min_rx].iloc[0])

#calculate relative roughness
bank_angle = 60
df['R'] = ((df['width'] + (df['depth']/np.tan(np.radians(bank_angle)))) * df['depth']) / (df['width'] + 2 * (df['depth'] / np.sin(np.radians(bank_angle))))
df['rel_rx'] = df['R'] / df['sigma_z']

#calculate bed elevation
reach_length = 1000 #m
h_baselevel = 0
df['bed_elev'] = df['slope'] * reach_length + h_baselevel
df['bed_elev_norm'] = df['bed_elev'] / float(df['bed_elev'][df['sigma_z'] == min_rx].iloc[0])

#############################################################################

#run from which to get DEPTH-LIMITED data
run_name = 'figure_7_rev1_L1000_tol1e-13_dt1000_hfp3' #old draft: run 15
data = np.load('../figure_7/sweep_z0_values_floodplain_' + str(run_name) + '.npy')

#convert to pandas dataframe for seaborn compatibility
df_overbank = pd.DataFrame({'sigma_z': data[:, 0], 
                   'width': data[:, 1], 
                   'depth': data[:, 2],
                   'slope': data[:, 3],
                   'e_slope': data[:, 4],
                   'tau_bed': data[:, 5],
                   'tau_bank': data[:, 6],
                   'fr/f0': data[:, 7],
                   'teq': data[:, 8]})

#normalize outputs (except fr/f) to output value for sigma_z = 0.01 m
min_rx = min(df_overbank['sigma_z']) #minimum sigma_z used
df_overbank['width_norm'] = df_overbank['width'] / float(df_overbank['width'][df_overbank['sigma_z'] == min_rx].iloc[0])
df_overbank['depth_norm'] = df_overbank['depth'] / float(df_overbank['depth'][df_overbank['sigma_z'] == min_rx].iloc[0])
df_overbank['slope_norm'] = df_overbank['slope'] / float(df_overbank['slope'][df_overbank['sigma_z'] == min_rx].iloc[0])
df_overbank['e_slope_norm'] = df_overbank['e_slope'] / float(df_overbank['e_slope'][df_overbank['sigma_z'] == min_rx].iloc[0])
df_overbank['tau_bed_norm'] = df_overbank['tau_bed'] / float(df_overbank['tau_bed'][df_overbank['sigma_z'] == min_rx].iloc[0])
df_overbank['tau_bank_norm'] = df_overbank['tau_bank'] / float(df_overbank['tau_bank'][df_overbank['sigma_z'] == min_rx].iloc[0])
df_overbank['fr/f0 norm'] = df_overbank['fr/f0'] / float(df['fr/f0'][df_overbank['sigma_z'] == min_rx].iloc[0])

#calculate relative roughness
df_overbank['R'] = ((df_overbank['width'] + (df_overbank['depth']/np.tan(np.radians(bank_angle)))) * df_overbank['depth']) / (df_overbank['width'] + 2 * (df_overbank['depth'] / np.sin(np.radians(bank_angle))))
df_overbank['rel_rx'] = df_overbank['R'] / df_overbank['sigma_z']

#calculate bed elevation
h_baselevel = 0
df_overbank['bed_elev'] = df_overbank['slope'] * reach_length + h_baselevel
df_overbank['bed_elev_norm'] = df_overbank['bed_elev'] / float(df_overbank['bed_elev'][df_overbank['sigma_z'] == min_rx].iloc[0])


##########################################################################

text_x = 0.02
text_y = 0.82

xmin = 0.007
xmax = 14

markersize = 100

alpha_belowbank = 1.0
alpha_overbank = 0.25

df['alpha'] = alpha_belowbank
df.loc[df_overbank['e_slope_norm'] < 0.001, 'alpha'] = alpha_overbank


#create figure: 4 panels
# fig, axs = plt.subplots(2,2, figsize = (8,5))

# width = axs[0, 0]
# depth = axs[0, 1]
# slope = axs[1, 0]
# f_ratio = axs[1,1]


# width.scatter(df['sigma_z'], df['width'], clip_on = False, zorder = 3,
#               edgecolor = 'k', facecolor = '#fbb4ae', s = markersize)
# width.set_xscale('log')
# width.set_xlim(xmin, xmax)
# #width.set_ylim(40, 200)
# width.get_xaxis().set_ticklabels([])
# width.set_ylabel('Equilibrium width [m]')
# width.text(0.02, 0.85, 'A', transform=width.transAxes, fontsize = 20)

# depth.scatter(df['sigma_z'], df['depth'], color = 'r', 
#               clip_on = False, zorder = 3, edgecolor = 'k', facecolor = '#b3cde3',
#               s = markersize)
# depth.set_xlim(xmin, xmax)
# #depth.set_ylim(0, 4)
# depth.set_xscale('log')
# depth.get_xaxis().set_ticklabels([])
# depth.set_ylabel('Equilibrium depth [m]')
# depth.text(0.02, 0.85, 'B', transform=depth.transAxes, fontsize = 20)

# slope.scatter(df['sigma_z'], df['slope'], label = 'bed slope', clip_on = False, 
#               zorder = 3, edgecolor = 'k', alpha = 1, marker = 's', s = markersize,
#               c = '#fdb863')
# slope.scatter(df['sigma_z'], df['e_slope'], label = 'energy slope', clip_on = False, 
#               zorder = 3, edgecolor = 'k', alpha = 1, marker = '^', s = markersize,
#               c = '#b2abd2')
# slope.set_xscale('log')
# slope.set_ylabel('Equilibrium slope [m/m]')
# slope.set_xlim(xmin, xmax)
# #slope.set_ylim(0, 0.03)
# slope.text(0.02, 0.85, 'C', transform=slope.transAxes, fontsize = 20)
# slope.legend(loc = 'upper center', framealpha = 1, edgecolor = 'k')

# f_ratio.scatter(df['sigma_z'], df['fr/f0'], color = '#b8e186', clip_on = False, 
#                 s = markersize, edgecolor = 'k', zorder = 3)
# f_ratio.set_xscale('log')
# f_ratio.set_ylabel('Normalized friction factor [-]')
# f_ratio.set_xlim(xmin, xmax)
# f_ratio.set_xlabel('Roughness length $\sigma_z$ [m]')
# f_ratio.text(0.02, 0.85, 'D', transform=f_ratio.transAxes, fontsize = 20)


# plt.tight_layout()
#fig.savefig('sweep_sigma_z_' + run_name +'.png', dpi = 1000)

###NORMALIZED FIGURE##########################################################

#create figure: 6 panels
fig2, axs = plt.subplots(3,2, figsize = (8,8))

width = axs[0, 0]
depth = axs[0, 1]
slope = axs[1, 0]
tau = axs[1, 1]
f_ratio = axs[2, 0]
rel_rx = axs[2, 1]


width.scatter(df['sigma_z'], df['width_norm'], clip_on = False, zorder = 3,
              edgecolor = 'k', facecolor = '#8dd3c7', s = markersize,
              alpha = df['alpha']) ##fbb4ae

#width.scatter(df['sigma_z'], df['w_r_norm'], clip_on = False, zorder = 3,
#              edgecolor = 'k', facecolor = 'red', s = markersize) ##fbb4ae

width.set_xscale('log')
width.set_xlim(xmin, xmax)
#width.set_ylim(40, 200)
width.get_xaxis().set_ticklabels([])
width.set_ylabel('Normalized width [-]')
width.axhline(y = 1, color = 'gray', linestyle = '--')
width.text(text_x, text_y, 'A', transform=width.transAxes, fontsize = 20)

#regime-separating lines
width.axvline(1.8, linewidth = 2, color = 'k')
width.axvline(0.4, linewidth = 2, color = 'k')

#width.text(0.1, 0.7, 'widening/\nflattening', fontsize = 16, transform=width.transAxes)
width.text(0.15, 0.77, 'widening/\nflattening', transform=width.transAxes, fontsize = 12,
               bbox = dict(boxstyle='square', fc = (1,1,1,1), edgecolor = 'k'))
width.text(0.48, 0.6, 'widening/\nsteepening', transform=width.transAxes, fontsize = 12,
               bbox = dict(boxstyle='square', fc = (1,1,1,1), edgecolor = 'k'))
width.text(0.8, 0.3, 'filling', transform=width.transAxes, fontsize = 12,
               bbox = dict(boxstyle='square', fc = (1,1,1,1), edgecolor = 'k'))

depth.scatter(df['sigma_z'], df['depth_norm'], 
              clip_on = False, zorder = 3, edgecolor = 'k', facecolor = '#ffffb3',
              s = markersize, alpha = df['alpha'], label = 'flow depth') ##b3cde3
depth.set_xlim(xmin, xmax)
#depth.set_ylim(0, 4)
depth.set_xscale('log')
depth.get_xaxis().set_ticklabels([])
depth.set_ylabel('Norm. depth and bed elevation [-]')
depth.axhline(y = 1, color = 'gray', linestyle = '--')
depth.text(text_x, text_y, 'B', transform=depth.transAxes, fontsize = 20)
depth.scatter(df['sigma_z'], df['bed_elev_norm'], clip_on = False, zorder = 3,
              edgecolor = 'k', facecolor = '#d9d9d9', s = markersize, 
              marker = 'P',alpha = df['alpha'],  label = 'bed elevation')
depth.legend(bbox_to_anchor=(0.65,1.0), loc = 'upper right', 
             bbox_transform=depth.transAxes, framealpha = 1, edgecolor = 'k')

#regime-separating lines
depth.axvline(1.8, linewidth = 2, color = 'k')
depth.axvline(0.4, linewidth = 2, color = 'k')

slope.scatter(df['sigma_z'], df['slope_norm'], label = 'bed slope', clip_on = False, 
              zorder = 3, edgecolor = 'k', marker = 's', s = markersize,
              c = '#bebada', alpha = df['alpha']) #fdb863
slope.scatter(df['sigma_z'], df['e_slope_norm'], label = 'energy slope', clip_on = False, 
              zorder = 3, edgecolor = 'k', marker = '^', s = markersize,
              c = '#fb8072', alpha = df['alpha']) #b2abd2
slope.set_xscale('log')
slope.set_ylabel('Normalized local slope [-]')
slope.legend(loc = 'upper center', framealpha = 1, edgecolor = 'k')
slope.set_xlim(xmin, xmax)
slope.get_xaxis().set_ticklabels([])
#slope.set_xlabel('Roughness length $\sigma_z$ [m]')
slope.axhline(y = 1, color = 'gray', linestyle = '--')
#slope.set_ylim(0, 0.03)
slope.text(text_x, text_y, 'C', transform=slope.transAxes, fontsize = 20)

#regime-separating lines
slope.axvline(1.8, linewidth = 2, color = 'k')
slope.axvline(0.4, linewidth = 2, color = 'k')

tau.scatter(df['sigma_z'], df['tau_bed_norm'], color = '#80b1d3', clip_on=False,
            marker = 'h', s = markersize, edgecolor = 'k', zorder = 3,
            label = 'bed shear stress', alpha = df['alpha'])
tau.scatter(df['sigma_z'], df['tau_bank_norm'], color = '#fdb462', clip_on=False,
            marker = 'v', s = markersize, edgecolor = 'k', zorder = 3,
            label = 'bank shear stress', alpha = df['alpha'])#ffd92f'
tau.set_xscale('log')
tau.set_xlim(xmin, xmax)
tau.get_xaxis().set_ticklabels([])
tau.set_ylabel('Normalized shear stress [-]')
tau.axhline(y = 1, color = 'gray', linestyle = '--')
tau.set_ylim(0.8,1.2)
tau.legend(loc = 'upper center', framealpha = 1, edgecolor = 'k')
tau.text(text_x, text_y, 'D', transform=tau.transAxes, fontsize = 20)

#regime-separating lines
tau.axvline(1.8, linewidth = 2, color = 'k')
tau.axvline(0.4, linewidth = 2, color = 'k')

f_ratio.scatter(df['sigma_z'], df['fr/f0'], color = '#b3de69', clip_on = False, 
                s = markersize, edgecolor = 'k', zorder = 3,
                alpha = df['alpha']) #b8e186
f_ratio.set_xscale('log')
f_ratio.set_ylabel('Friction factor ratio $f_r/f$ [-]')
f_ratio.set_xlim(xmin, xmax)
f_ratio.set_ylim(0.9, 40)
f_ratio.set_xlabel('Roughness length $z_0$ [m]')
f_ratio.axhline(y = 1, color = 'gray', linestyle = '--')
f_ratio.text(text_x, text_y, 'E', transform=f_ratio.transAxes, fontsize = 20)
f_ratio.set_yscale('log')

#regime-separating lines
f_ratio.axvline(1.8, linewidth = 2, color = 'k')
f_ratio.axvline(0.4, linewidth = 2, color = 'k')

rel_rx.scatter(df['sigma_z'], df['rel_rx'], color = '#fccde5', clip_on=False,
               s = markersize, edgecolor = 'k', zorder = 3,
               alpha = df['alpha'])
rel_rx.set_xlabel('Roughness length $z_0$ [m]')
rel_rx.set_xscale('log')
rel_rx.set_xlim(xmin, xmax)
rel_rx.set_ylabel('Relative submergence $R/z_0$ [-]')
rel_rx.text(text_x, text_y, 'F', transform=rel_rx.transAxes, fontsize = 20)
rel_rx.set_ylim(0.1, 100)
rel_rx.set_yscale('log')

#regime-separating lines
rel_rx.axvline(1.8, linewidth = 2, color = 'k')
rel_rx.axvline(0.4, linewidth = 2, color = 'k')


plt.tight_layout()
fig2.savefig('fig_sweep_z0_' + run_name +'_hires.png', dpi = 1000)
fig2.savefig('fig_sweep_z0_' + run_name +'_lores.png', dpi = 200)
