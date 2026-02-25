#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Create figure 6 in Shobe and Scott: Effects of bank cover on equilibrium 
channel geometry.

Created February 2026 by @author: charlesshobe
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#run from which to get data
run_name = 'figure_6'
data = np.load('../results/sweep_bank_cover_values_' + str(run_name) + '.npy')

#convert to pandas dataframe for seaborn compatibility
df = pd.DataFrame({'l_bank': data[:, 0], 
                   'width': data[:, 1], 
                   'depth': data[:, 2],
                   'slope': data[:, 3],
                   'e_slope': data[:, 4],
                   'tau_bed': data[:, 5],
                   'tau_bank': data[:, 6],
                   'fr/f0': data[:, 7],
                   'teq': data[:, 8]})

#normalize outputs (except fr/f) to output value for sigma_z = 0.01 m
min_rx = min(df['l_bank']) #minimum sigma_z used
df['width_norm'] = df['width'] / float(df['width'][df['l_bank'] == min_rx].iloc[0])
df['depth_norm'] = df['depth'] / float(df['depth'][df['l_bank'] == min_rx].iloc[0])
df['slope_norm'] = df['slope'] / float(df['slope'][df['l_bank'] == min_rx].iloc[0])
df['e_slope_norm'] = df['e_slope'] / float(df['e_slope'][df['l_bank'] == min_rx].iloc[0])
df['tau_bed_norm'] = df['tau_bed'] / float(df['tau_bed'][df['l_bank'] == min_rx].iloc[0])
df['tau_bank_norm'] = df['tau_bank'] / float(df['tau_bank'][df['l_bank'] == min_rx].iloc[0])
df['fr/f0 norm'] = df['fr/f0'] / float(df['fr/f0'][df['l_bank'] == min_rx].iloc[0])

#calculate relative roughness, cover, etc
bank_angle = 60
z0 = 0.1
reach_length = 1000 #m
initial_slope = 0.0055645631326687005
h_baselevel = 0
hfp = 5 + h_baselevel + initial_slope * reach_length #5 + initial slope + reach length
df['chan_depth'] = hfp - (df['slope'] * reach_length)
df['R'] = ((df['width'] + (df['depth']/np.tan(np.radians(bank_angle)))) * df['depth']) / (df['width'] + 2 * (df['depth'] / np.sin(np.radians(bank_angle))))
df['rel_rx'] = df['R'] / z0

#calculate fc_bed
df['fc_bank'] = np.minimum(df['l_bank'] / (2 * df['chan_depth'] * np.sin(np.radians(bank_angle))), 1)
df['fc_bank_norm'] = df['fc_bank'] / float(df['fc_bank'][df['l_bank'] == min_rx].iloc[0])


#calculate bed elevation
df['bed_elev'] = df['slope'] * reach_length + h_baselevel
df['bed_elev_norm'] = df['bed_elev'] / float(df['bed_elev'][df['l_bank'] == min_rx].iloc[0])


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


width.scatter(df['fc_bank'], df['width_norm'], clip_on = False, zorder = 3,
              edgecolor = 'k', facecolor = '#8dd3c7', s = markersize)
width.set_xlim(xmin, xmax)
width.set_ylim(0.3, 1.2)
width.get_xaxis().set_ticklabels([])
width.set_ylabel('Normalized width [-]')
width.axhline(y = 1, color = 'gray', linestyle = '--')
width.text(text_x, text_y, 'A', transform=width.transAxes, fontsize = 20)

depth.scatter(df['fc_bank'], df['depth_norm'], 
              clip_on = False, zorder = 3, edgecolor = 'k', facecolor = '#ffffb3',
              s = markersize, label = 'flow depth')
depth.set_xlim(xmin, xmax)
depth.get_xaxis().set_ticklabels([])
depth.set_ylabel('Norm. depth and bed elevation [-]')
depth.axhline(y = 1, color = 'gray', linestyle = '--')
depth.text(text_x, text_y, 'B', transform=depth.transAxes, fontsize = 20)
depth.scatter(df['fc_bank'], df['bed_elev_norm'], clip_on = False, zorder = 3,
              edgecolor = 'k', facecolor = '#d9d9d9', s = markersize, 
              marker = 'P', label = 'bed elevation')
depth.legend(bbox_to_anchor=(0.65,1.0), loc = 'upper right', 
             bbox_transform=depth.transAxes, framealpha = 1, edgecolor = 'k')

slope.scatter(df['fc_bank'], df['slope_norm'], label = 'bed slope', clip_on = False, 
              zorder = 3, edgecolor = 'k', alpha = 1, marker = 's', s = markersize,
              c = '#bebada')
slope.scatter(df['fc_bank'], df['e_slope_norm'], label = 'energy slope', clip_on = False, 
              zorder = 3, edgecolor = 'k', alpha = 1, marker = '^', s = markersize,
              c = '#fb8072')
slope.set_ylabel('Normalized local slope [-]')
slope.legend(bbox_to_anchor=(0.7,1.02), loc = 'upper right', bbox_transform=slope.transAxes, framealpha = 1, edgecolor = 'k')
slope.set_xlim(xmin, xmax)
slope.get_xaxis().set_ticklabels([])
slope.axhline(y = 1, color = 'gray', linestyle = '--')
slope.set_ylim(0.4, 1.2)
slope.text(text_x, text_y, 'C', transform=slope.transAxes, fontsize = 20)

tau.scatter(df['fc_bank'], df['tau_bed_norm'], color = '#80b1d3', clip_on=False,
            marker = 'h', s = markersize, edgecolor = 'k', zorder = 3,
            label = 'bed shear stress')
tau.scatter(df['fc_bank'], df['tau_bank_norm'], color = '#fdb462', clip_on=False,
            marker = 'v', s = markersize, edgecolor = 'k', zorder = 3,
            label = 'bank shear stress')
tau.set_xlim(xmin, xmax)
tau.get_xaxis().set_ticklabels([])
tau.set_ylabel('Normalized shear stress [-]')
tau.axhline(y = 1, color = 'gray', linestyle = '--')
tau.set_ylim(0.9,1.6)
tau.legend(bbox_to_anchor=(0.7,1.02), loc = 'upper right', bbox_transform=tau.transAxes, framealpha = 1, edgecolor = 'k')
tau.text(text_x, text_y, 'D', transform=tau.transAxes, fontsize = 20)

f_ratio.scatter(df['fc_bank'], df['fr/f0'], color = '#b3de69', clip_on = False, 
                s = markersize, edgecolor = 'k', zorder = 3)
f_ratio.set_ylabel('Friction factor ratio $f_r/f$ [-]')
f_ratio.set_xlim(xmin, xmax)
f_ratio.set_ylim(1, 1.2)
f_ratio.set_xlabel('Bank cover fraction $f_c^{\mathrm{bank}}$ [-]')
f_ratio.text(text_x, text_y, 'E', transform=f_ratio.transAxes, fontsize = 20)


rel_rx.scatter(df['fc_bank'], df['rel_rx'], color = '#fccde5', clip_on=False,
               s = markersize, edgecolor = 'k', zorder = 3)
rel_rx.set_ylabel('Relative submergence $R/z_0$ [-]')
rel_rx.set_xlim(xmin, xmax)
rel_rx.set_xlabel('Bank cover fraction $f_c^{\mathrm{bank}}$ [-]')
rel_rx.text(text_x, text_y, 'F', transform=rel_rx.transAxes, fontsize = 20)
rel_rx.set_ylim(0.1, 100)
rel_rx.set_yscale('log')


plt.tight_layout()
fig2.savefig('figure_6_hires.png', dpi = 1000)
fig2.savefig('figure_6_lores.png', dpi = 100)