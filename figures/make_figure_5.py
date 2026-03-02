#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Create figure 5 in Shobe and Scott: Effects of bed cover on equilibrium 
channel geometry.

Created February 2026 by @author: charlesshobe
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#run from which to get data
run_name = 'figure_5_nofp'
data = np.load('../results/sweep_bed_cover_values_' + str(run_name) + '.npy')

#convert to pandas dataframe for seaborn compatibility
df = pd.DataFrame({'l_bed': data[:, 0], 
                   'width': data[:, 1], 
                   'depth': data[:, 2],
                   'slope': data[:, 3],
                   'e_slope': data[:, 4],
                   'tau_bed': data[:, 5],
                   'tau_bank': data[:, 6],
                   'fr/f0': data[:, 7],
                   'teq': data[:, 8]})

#normalize outputs (except fr/f) to minimum bed cover run
min_rx = min(df['l_bed']) #minimum bed cover used
df['width_norm'] = df['width'] / float(df['width'][df['l_bed'] == min_rx].iloc[0])
df['depth_norm'] = df['depth'] / float(df['depth'][df['l_bed'] == min_rx].iloc[0])
df['slope_norm'] = df['slope'] / float(df['slope'][df['l_bed'] == min_rx].iloc[0])
df['e_slope_norm'] = df['e_slope'] / float(df['e_slope'][df['l_bed'] == min_rx].iloc[0])
df['tau_bed_norm'] = df['tau_bed'] / float(df['tau_bed'][df['l_bed'] == min_rx].iloc[0])
df['tau_bank_norm'] = df['tau_bank'] / float(df['tau_bank'][df['l_bed'] == min_rx].iloc[0])
df['fr/f0 norm'] = df['fr/f0'] / float(df['fr/f0'][df['l_bed'] == min_rx].iloc[0])

#calculate relative roughness
bank_angle = 60
z0 = 0.1
df['R'] = ((df['width'] + (df['depth']/np.tan(np.radians(bank_angle)))) * df['depth']) / (df['width'] + 2 * (df['depth'] / np.sin(np.radians(bank_angle))))
df['rel_rx'] = df['R'] / z0

#calculate fc_bed
df['fc_bed'] = df['l_bed'] / df['width']
df['fc_bed_norm'] = df['fc_bed'] / float(df['fc_bed'][df['l_bed'] == min_rx].iloc[0])

#calculate bed elevation
reach_length = 1000 #m
h_baselevel = 0
df['bed_elev'] = df['slope'] * reach_length + h_baselevel
df['bed_elev_norm'] = df['bed_elev'] / float(df['bed_elev'][df['l_bed'] == min_rx].iloc[0])

#############################################################################

#run from which to get DEPTH-LIMITED data
run_name = 'figure_5' 
data = np.load('../results/sweep_bed_cover_values_' + str(run_name) + '.npy')

#convert to pandas dataframe for seaborn compatibility
df_overbank = pd.DataFrame({'z0': data[:, 0], 
                   'width': data[:, 1], 
                   'depth': data[:, 2],
                   'slope': data[:, 3],
                   'e_slope': data[:, 4],
                   'tau_bed': data[:, 5],
                   'tau_bank': data[:, 6],
                   'fr/f0': data[:, 7],
                   'teq': data[:, 8]})

#normalize outputs (except fr/f) to minimum bed cover run
min_rx = min(df_overbank['z0']) #minimum bed cover used
df_overbank['width_norm'] = df_overbank['width'] / float(df_overbank['width'][df_overbank['z0'] == min_rx].iloc[0])
df_overbank['depth_norm'] = df_overbank['depth'] / float(df_overbank['depth'][df_overbank['z0'] == min_rx].iloc[0])
df_overbank['slope_norm'] = df_overbank['slope'] / float(df_overbank['slope'][df_overbank['z0'] == min_rx].iloc[0])
df_overbank['e_slope_norm'] = df_overbank['e_slope'] / float(df_overbank['e_slope'][df_overbank['z0'] == min_rx].iloc[0])
df_overbank['tau_bed_norm'] = df_overbank['tau_bed'] / float(df_overbank['tau_bed'][df_overbank['z0'] == min_rx].iloc[0])
df_overbank['tau_bank_norm'] = df_overbank['tau_bank'] / float(df_overbank['tau_bank'][df_overbank['z0'] == min_rx].iloc[0])
df_overbank['fr/f0 norm'] = df_overbank['fr/f0'] / float(df['fr/f0'][df_overbank['z0'] == min_rx].iloc[0])

#calculate relative roughness
df_overbank['R'] = ((df_overbank['width'] + (df_overbank['depth']/np.tan(np.radians(bank_angle)))) * df_overbank['depth']) / (df_overbank['width'] + 2 * (df_overbank['depth'] / np.sin(np.radians(bank_angle))))
df_overbank['rel_rx'] = df_overbank['R'] / z0

#calculate bed elevation
h_baselevel = 0
df_overbank['bed_elev'] = df_overbank['slope'] * reach_length + h_baselevel
df_overbank['bed_elev_norm'] = df_overbank['bed_elev'] / float(df_overbank['bed_elev'][df_overbank['z0'] == min_rx].iloc[0])


##########################################################################
alpha_belowbank = 1.0
alpha_overbank = 0.25

df['alpha'] = alpha_belowbank
df.loc[df_overbank['e_slope_norm'] < 0.01, 'alpha'] = alpha_overbank



text_x = 0.02
text_y = 0.88

xmin = 0.0
xmax = 0.8

markersize = 100

###NORMALIZED FIGURE##########################################################

#create figure: 6 panels
fig2, axs = plt.subplots(3,2, figsize = (8,8))

width = axs[0, 0]
depth = axs[0, 1]
slope = axs[1, 0]
tau = axs[1, 1]
f_ratio = axs[2, 0]
rel_rx = axs[2, 1]


width.scatter(df['fc_bed'], df['width_norm'], clip_on = False, zorder = 3,
              edgecolor = 'k', facecolor = '#8dd3c7', s = markersize,
              alpha = df['alpha']) ##fbb4ae
width.set_xlim(xmin, xmax)
width.get_xaxis().set_ticklabels([])
width.set_ylabel('Normalized width [-]')
width.axhline(y = 1, color = 'gray', linestyle = '--')
width.text(text_x, text_y, 'A', transform=width.transAxes, fontsize = 20)

depth.scatter(df['fc_bed'], df['depth_norm'], 
              clip_on = False, zorder = 3, edgecolor = 'k', facecolor = '#ffffb3',
              s = markersize, label = 'flow depth',
              alpha = df['alpha']) ##b3cde3
depth.set_xlim(xmin, xmax)
depth.get_xaxis().set_ticklabels([])
depth.set_ylabel('Norm. depth and bed elevation [-]')
depth.axhline(y = 1, color = 'gray', linestyle = '--')
depth.text(text_x, text_y, 'B', transform=depth.transAxes, fontsize = 20)
depth.scatter(df['fc_bed'], df['bed_elev_norm'], clip_on = False, zorder = 3,
              edgecolor = 'k', facecolor = '#d9d9d9', s = markersize, 
              marker = 'P', label = 'bed elevation', alpha = df['alpha'])
depth.legend(bbox_to_anchor=(0.65,1.0), loc = 'upper right', 
             bbox_transform=depth.transAxes, framealpha = 1, edgecolor = 'k')

slope.scatter(df['fc_bed'], df['slope_norm'], label = 'bed slope', clip_on = False, 
              zorder = 3, edgecolor = 'k', marker = 's', s = markersize,
              c = '#bebada', alpha = df['alpha']) #fdb863
slope.scatter(df['fc_bed'], df['e_slope_norm'], label = 'energy slope', clip_on = False, 
              zorder = 3, edgecolor = 'k', marker = '^', s = markersize,
              c = '#fb8072', alpha = df['alpha']) #b2abd2
slope.set_ylabel('Normalized local slope [-]')
slope.legend(bbox_to_anchor=(0.7,1.02), loc = 'upper right', bbox_transform=slope.transAxes, framealpha = 1, edgecolor = 'k')
slope.set_xlim(xmin, xmax)
slope.get_xaxis().set_ticklabels([])
slope.axhline(y = 1, color = 'gray', linestyle = '--')
slope.text(text_x, text_y, 'C', transform=slope.transAxes, fontsize = 20)

tau.scatter(df['fc_bed'], df['tau_bed_norm'], color = '#80b1d3', clip_on=False,
            marker = 'h', s = markersize, edgecolor = 'k', zorder = 3,
            label = 'bed shear stress', alpha = df['alpha'])
tau.scatter(df['fc_bed'], df['tau_bank_norm'], color = '#fdb462', clip_on=False,
            marker = 'v', s = markersize, edgecolor = 'k', zorder = 3,
            label = 'bank shear stress', alpha = df['alpha'])#ffd92f'
tau.set_xlim(xmin, xmax)
tau.get_xaxis().set_ticklabels([])
tau.set_ylabel('Normalized shear stress [-]')
tau.axhline(y = 1, color = 'gray', linestyle = '--')
tau.set_ylim(0.4, 1.25)
tau.legend(bbox_to_anchor=(0.8,1.02), loc = 'upper right', bbox_transform=tau.transAxes, framealpha = 1, edgecolor = 'k')
tau.text(text_x, text_y, 'D', transform=tau.transAxes, fontsize = 20)

f_ratio.scatter(df['fc_bed'], df['fr/f0'], color = '#b3de69', clip_on = False, 
                s = markersize, edgecolor = 'k', zorder = 3, alpha = df['alpha']) #b8e186
f_ratio.set_ylabel('Friction factor ratio $f_r/f$ [-]')
f_ratio.set_xlim(xmin, xmax)
f_ratio.set_ylim(1, 2)
f_ratio.set_xlabel('Bed cover fraction $f_c^{\mathrm{bed}}$ [-]')
f_ratio.text(text_x, text_y, 'E', transform=f_ratio.transAxes, fontsize = 20)


rel_rx.scatter(df['fc_bed'], df['rel_rx'], color = '#fccde5', clip_on=False,
               s = markersize, edgecolor = 'k', zorder = 3, alpha = df['alpha'])
rel_rx.set_ylabel('Relative submergence $R/z_0$ [-]')
rel_rx.set_xlim(xmin, xmax)
rel_rx.set_xlabel('Bed cover fraction $f_c^{\mathrm{bed}}$ [-]')
rel_rx.text(text_x, text_y, 'F', transform=rel_rx.transAxes, fontsize = 20)
rel_rx.set_ylim(0.1, 100)
rel_rx.set_yscale('log')


plt.tight_layout()
fig2.savefig('figure_5_hires.png', dpi = 1000)
fig2.savefig('figure_5_lores.png', dpi = 100)
