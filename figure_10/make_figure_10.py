#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 19 14:14:51 2025

@author: charlesshobe

read and plot param space exploration data
"""

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import colors
import seaborn as sns
import numpy as np

run_name = 'results/case_study_low_z0_inversion_record.csv'
colnames = ['k_ero', 'k_dep', 'misfit']
data = pd.read_csv(run_name, header = None, names = colnames).sort_values(by = 'misfit', ascending = False)


#set up the figure grid
fig = plt.figure(figsize=(10,10))
widths = [3, 0.75, 0.75, 3, 0.75]
heights = [3, 1, 1, 5, 1.1, 2, 0.25, 2]
spec = fig.add_gridspec(ncols=len(widths), nrows=len(heights), width_ratios=widths,
                          height_ratios=heights, wspace=0.0, hspace=0.0)


#axis limit params
k_ero_min = 0.009
k_ero_max = 1.02

k_dep_min = 8
k_dep_max = 122

#LEFT COLUMN: SIGMA_Z CASE 1#################################################

bc_plot = fig.add_subplot(spec[0, 0])
k_ero_hist = fig.add_subplot(spec[2, 0])
misfit_scatter = fig.add_subplot(spec[3, 0])
k_dep_hist = fig.add_subplot(spec[3, 1])
width_timeseries = fig.add_subplot(spec[5, 0])
bed_elev_timeseries = fig.add_subplot(spec[7, 0])

observed_times = np.array([0, 33264000, 96163200, 158803200]) / 31536000
low_sigma_z_values = np.array([0.21, 0.24, 0.23])
l_bed_obst_values = np.array([11.0, 18.9, 17.1])
l_bank_obst_values = np.array([0.65, 0.61, 0.86])

linewidth = 5

sigma_z_color = '#fb8072'
bank_obst_color = '#8dd3c7'
bed_obst_color = '#bebada'

bc_plot.hlines(y = low_sigma_z_values[0], xmin = observed_times[0], 
                xmax = observed_times[1], linewidth = linewidth, color = sigma_z_color,
                label = '$z_0$')
bc_plot.hlines(y = low_sigma_z_values[1], xmin = observed_times[1], 
                xmax = observed_times[2], linewidth = linewidth, color = sigma_z_color)
bc_plot.hlines(y = low_sigma_z_values[2], xmin = observed_times[2], 
                xmax = observed_times[3], linewidth = linewidth, color = sigma_z_color)

bc_plot.hlines(y = l_bank_obst_values[0], xmin = observed_times[0], 
                xmax = observed_times[1], linewidth = linewidth, color = bank_obst_color,
                label = '$l^{\mathrm{bank}}_{\mathrm{obstacle}}$')
bc_plot.hlines(y = l_bank_obst_values[1], xmin = observed_times[1], 
                xmax = observed_times[2], linewidth = linewidth, color = bank_obst_color)
bc_plot.hlines(y = l_bank_obst_values[2], xmin = observed_times[2], 
                xmax = observed_times[3], linewidth = linewidth, color = bank_obst_color)

fc_plot = bc_plot.twinx()
fc_plot.hlines(y = l_bed_obst_values[0], xmin = observed_times[0], 
                xmax = observed_times[1], linewidth = linewidth, color = bed_obst_color,
                label = '$l^{\mathrm{bed}}_{\mathrm{obstacle}}$')
fc_plot.hlines(y = l_bed_obst_values[1], xmin = observed_times[1], 
                xmax = observed_times[2], linewidth = linewidth, color = bed_obst_color)
fc_plot.hlines(y = l_bed_obst_values[2], xmin = observed_times[2], 
                xmax = observed_times[3], linewidth = linewidth, color = bed_obst_color)

#merge handles and labels for legend
lines, labels = bc_plot.get_legend_handles_labels()
lines2, labels2 = fc_plot.get_legend_handles_labels()

bc_plot.legend(lines + lines2, labels + labels2, bbox_to_anchor = (0.69, 1.35), 
               loc = 'upper left', ncols = 3, framealpha = 1, edgecolor = 'k')

bc_plot.set_xticks(np.arange(0, 6))
bc_plot.set_xticklabels(['3/2019', '3/2020', '3/2021', '3/2022', '3/2023', '3/2024'])
bc_plot.set_xlabel('Date [m/yyyy]')
bc_plot.set_ylabel('$z_0$ and $l^{\mathrm{bank}}_{\mathrm{obstacle}}$' + '\n' + '[m]')
bc_plot.set_ylim(0, 2)
bc_plot.set_yticks(np.array([0, 1]))
bc_plot.yaxis.set_label_coords(-0.1, 0.25)
#bc_plot.set_yticklabels(['0', '1'])

fc_plot.set_ylim(-25, 20)
fc_plot.set_yticks(np.array([0, 20]))
fc_plot.set_ylabel('$l^{\mathrm{bed}}_{\mathrm{obstacle}}$' + '\n' + '[m]')
fc_plot.yaxis.set_label_coords(1.1, 0.78)

bc_plot.text(0.01, 0.83, 'A', transform=bc_plot.transAxes, fontsize = 20)


sns.kdeplot(data = data, x = 'k_ero', ax= k_ero_hist, color='k', log_scale = 10) #k histogram
#k_ero_hist.get_xaxis().set_ticks([])
#k_ero_hist.get_yaxis().set_ticks([])
k_ero_hist.axis('off')
k_ero_hist.set_xlim(k_ero_min, k_ero_max)

sns.kdeplot(data = data, y = 'k_dep', ax = k_dep_hist, color='k') #z* histogram
#r1_zstar_hist.get_xaxis().set_ticks([])
#r1_zstar_hist.get_yaxis().set_ticks([])
k_dep_hist.axis('off')
k_dep_hist.set_ylim(k_dep_min, k_dep_max)



color_min = min(data.misfit)
color_max = max(data.misfit)

cbar_mappable = misfit_scatter.scatter(data.k_ero, data.k_dep, 
                           c = (data.misfit),  
                           norm=colors.LogNorm(vmin=color_min, 
                                               vmax=color_max),
                            cmap='viridis', s = 50,
                            clip_on=False)
                           #color_min + (color_max - color_min)/10)
                           
misfit_scatter.scatter(data.k_ero.iloc[-1], data.k_dep.iloc[-1], 
                           c = data.misfit.iloc[-1],  
                           norm=colors.LogNorm(vmin=color_min, 
                                               vmax=color_max),
                            cmap='viridis', s = 400,
                            clip_on=False, marker = '*', edgecolor = 'white')

#colorbar
cax = fig.add_axes([0.4, 0.67, 0.15, 0.01])
c = fig.colorbar(cbar_mappable, cax = cax, orientation='horizontal')
c.ax.yaxis.set_visible(False)
#cax.text(1.1, 0.01, 'low', transform=cax.transAxes, fontsize=16)
#cax.text(1.1, 0.93, 'high', transform=cax.transAxes, fontsize=16)
cax.set_title('log(misfit) [-]', fontsize=12)

misfit_scatter.set_xlabel('$k^*_{\mathrm{ero}}$ [-]', labelpad = 0)
misfit_scatter.set_ylabel('$k^*_{\mathrm{dep}}$ [-]', labelpad = -5)

misfit_scatter.set_xlim(k_ero_min, k_ero_max)
misfit_scatter.set_ylim(k_dep_min, k_dep_max)

misfit_scatter.set_xscale('log')

misfit_scatter.text(0.01, 0.9, 'C', transform=misfit_scatter.transAxes, fontsize = 20)



#bring in width timesries data
width_data = np.load('results/case_study_bestfit_low_z0_widths.npy')
time_array = np.arange(0, 158803200 + 100, 100) / 31536000 #seconds per year

observed_widths = np.array([104, 108, 114, 119])

width_timeseries.plot(time_array, width_data, linewidth = 1, color = 'k',
                      label = 'modeled')

width_timeseries.scatter(observed_times, observed_widths, marker = 's', 
                         facecolor = 'darkgray', edgecolor = 'k',
                         label = 'observed')

width_timeseries.set_ylabel('$w_b$ [m]')
width_timeseries.get_xaxis().set_ticklabels([])
width_timeseries.legend(bbox_to_anchor = (1.02, 1.4), loc = 'upper left', 
                        bbox_transform = width_timeseries.transAxes,
                        framealpha = 1, edgecolor = 'k')

width_timeseries.text(0.01, 0.75, 'E', transform=width_timeseries.transAxes, fontsize = 20)




bed_elev_data = np.load('results/case_study_bestfit_low_z0_slopes.npy') * 117.1
#bed_elev_data -= min(bed_elev_data)

observed_bed_elevs = np.array([0.007, 0.007, 0.008, 0.007]) * 117.1
#observed_bed_elevs -= min(observed_bed_elevs)

bed_elev_timeseries.plot(time_array, bed_elev_data, linewidth = 1, color = 'k')
bed_elev_timeseries.scatter(observed_times, observed_bed_elevs, marker = 's', facecolor = 'darkgray', edgecolor = 'k')
bed_elev_timeseries.set_ylabel('$h$ [m]')

bed_elev_timeseries.set_xticks(np.arange(0, 6))
bed_elev_timeseries.set_xticklabels(['3/2019', '3/2020', '3/2021', '3/2022', '3/2023', '3/2024'])
bed_elev_timeseries.set_xlabel('Date [m/yyyy]')

bed_elev_timeseries.set_ylim(0.4, 1.03)

bed_elev_timeseries.text(0.01, 0.78, 'G', transform=bed_elev_timeseries.transAxes, fontsize = 20)

bestfit_k_ero = data.iloc[-1, 0]
bestfit_k_dep = data.iloc[-1, 1]

misfit_scatter.text(0.18, 0.47, 
                      '$k^*_{\mathrm{ero}}$ = ' + '%.2f'%np.round(bestfit_k_ero, 2) + '\n' + '$k^*_{\mathrm{dep}}$ = ' + '%.1f'%np.round(bestfit_k_dep, 1), 
                      transform=misfit_scatter.transAxes, fontsize = 12,
                      bbox = dict(edgecolor = 'k', facecolor = 'white', boxstyle='round', alpha = 0.5))
print(max(bed_elev_data) - min(bed_elev_data))
#RIGHT COLUMN COLUMN: SIGMA_Z CASE 2######################################

run_name_2 = 'results/case_study_high_z0_inversion_record.csv'
data_2 = pd.read_csv(run_name_2, header = None, names = colnames).sort_values(by = 'misfit', ascending = False)

bc_plot_2 = fig.add_subplot(spec[0, 3])
k_ero_hist_2 = fig.add_subplot(spec[2, 3])
misfit_scatter_2 = fig.add_subplot(spec[3, 3])
k_dep_hist_2 = fig.add_subplot(spec[3, 4])
width_timeseries_2 = fig.add_subplot(spec[5, 3])
bed_elev_timeseries_2 = fig.add_subplot(spec[7, 3])

high_sigma_z_values = np.array([0.52, 0.75, 0.67])

bc_plot_2.hlines(y = high_sigma_z_values[0], xmin = observed_times[0], 
                xmax = observed_times[1], linewidth = linewidth, color = sigma_z_color,
                label = '$z_0$')
bc_plot_2.hlines(y = high_sigma_z_values[1], xmin = observed_times[1], 
                xmax = observed_times[2], linewidth = linewidth, color = sigma_z_color)
bc_plot_2.hlines(y = high_sigma_z_values[2], xmin = observed_times[2], 
                xmax = observed_times[3], linewidth = linewidth, color = sigma_z_color)

bc_plot_2.hlines(y = l_bank_obst_values[0], xmin = observed_times[0], 
                xmax = observed_times[1], linewidth = linewidth, color = bank_obst_color,
                label = '$l^{\mathrm{bank}}_{\mathrm{obstacle}}$')
bc_plot_2.hlines(y = l_bank_obst_values[1], xmin = observed_times[1], 
                xmax = observed_times[2], linewidth = linewidth, color = bank_obst_color)
bc_plot_2.hlines(y = l_bank_obst_values[2], xmin = observed_times[2], 
                xmax = observed_times[3], linewidth = linewidth, color = bank_obst_color)

fc_plot_2 = bc_plot_2.twinx()
fc_plot_2.hlines(y = l_bed_obst_values[0], xmin = observed_times[0], 
                xmax = observed_times[1], linewidth = linewidth, color = bed_obst_color,
                label = '$l^{\mathrm{bed}}_{\mathrm{obstacle}}$')
fc_plot_2.hlines(y = l_bed_obst_values[1], xmin = observed_times[1], 
                xmax = observed_times[2], linewidth = linewidth, color = bed_obst_color)
fc_plot_2.hlines(y = l_bed_obst_values[2], xmin = observed_times[2], 
                xmax = observed_times[3], linewidth = linewidth, color = bed_obst_color)

#merge handles and labels for legend
lines, labels = bc_plot.get_legend_handles_labels()
lines2, labels2 = fc_plot.get_legend_handles_labels()

#bc_plot_2.legend(lines + lines2, labels + labels2, bbox_to_anchor = (-0.05, 1.3), 
#               loc = 'upper left', ncols = 3)

bc_plot_2.set_xticks(np.arange(0, 6))
bc_plot_2.set_xticklabels(['3/2019', '3/2020', '3/2021', '3/2022', '3/2023', '3/2024'])
bc_plot_2.set_xlabel('Date [m/yyyy]')
bc_plot_2.set_ylabel('$z_0$ and $l^{\mathrm{bank}}_{\mathrm{obstacle}}$' + '\n' + '[m]')
bc_plot_2.set_ylim(0, 2)
bc_plot_2.set_yticks(np.array([0, 1]))
bc_plot_2.yaxis.set_label_coords(-0.1, 0.25)
#bc_plot.set_yticklabels(['0', '1'])

fc_plot_2.set_ylim(-25, 20)
fc_plot_2.set_yticks(np.array([0, 20]))
fc_plot_2.set_ylabel('$l^{\mathrm{bed}}_{\mathrm{obstacle}}$' + '\n' + '[m]')
fc_plot_2.yaxis.set_label_coords(1.1, 0.78)

bc_plot_2.text(0.01, 0.83, 'B', transform=bc_plot_2.transAxes, fontsize = 20)


sns.kdeplot(data = data_2, x = 'k_ero', ax= k_ero_hist_2, color='k', log_scale = 10) #k histogram
#k_ero_hist.get_xaxis().set_ticks([])
#k_ero_hist.get_yaxis().set_ticks([])
k_ero_hist_2.axis('off')
k_ero_hist_2.set_xlim(k_ero_min, k_ero_max)

sns.kdeplot(data = data_2, y = 'k_dep', ax = k_dep_hist_2, color='k') #z* histogram
#r1_zstar_hist.get_xaxis().set_ticks([])
#r1_zstar_hist.get_yaxis().set_ticks([])
k_dep_hist_2.axis('off')
k_dep_hist_2.set_ylim(k_dep_min, k_dep_max)



color_min = min(data.misfit)
color_max = max(data.misfit)

cbar_mappable = misfit_scatter_2.scatter(data_2.k_ero, data_2.k_dep, 
                           c = (data_2.misfit),  
                           norm=colors.LogNorm(vmin=color_min, 
                                               vmax=color_max),
                            cmap='viridis', s = 50,
                            clip_on=False)
                           #color_min + (color_max - color_min)/10)
                           
misfit_scatter_2.scatter(data_2.k_ero.iloc[-1], data_2.k_dep.iloc[-1], 
                           c = data_2.misfit.iloc[-1],  
                           norm=colors.LogNorm(vmin=color_min, 
                                               vmax=color_max),
                            cmap='viridis', s = 400,
                            clip_on=False, marker = '*', edgecolor = 'white')


misfit_scatter_2.set_xlabel('$k^*_{\mathrm{ero}}$ [-]', labelpad = 0)
misfit_scatter_2.set_ylabel('$k^*_{\mathrm{dep}}$ [-]', labelpad = -5)

misfit_scatter_2.set_xlim(k_ero_min, k_ero_max)
misfit_scatter_2.set_ylim(k_dep_min, k_dep_max)

misfit_scatter_2.set_xscale('log')

misfit_scatter_2.text(0.01, 0.9, 'D', transform=misfit_scatter_2.transAxes, fontsize = 20)



#bring in width timesries data
width_data = np.load('results/case_study_bestfit_high_z0_widths.npy')
time_array = np.arange(0, 158803200 + 100, 100) / 31536000 #seconds per year

observed_times = np.array([0, 33264000, 96163200, 158803200]) / 31536000
observed_widths = np.array([104, 108, 114, 119])

width_timeseries_2.plot(time_array, width_data, linewidth = 1, color = 'k')


width_timeseries_2.scatter(observed_times, observed_widths, marker = 's', facecolor = 'darkgray', edgecolor = 'k')

width_timeseries_2.set_ylabel('$w_b$ [m]')

width_timeseries_2.get_xaxis().set_ticklabels([])

width_timeseries_2.text(0.01, 0.75, 'F', transform=width_timeseries_2.transAxes, fontsize = 20)



bed_elev_data = np.load('results/case_study_bestfit_high_z0_slopes.npy') * 117.1
#bed_elev_data -= min(bed_elev_data)

observed_bed_elevs = np.array([0.007, 0.007, 0.008, 0.007]) * 117.1
#observed_bed_elevs -= min(observed_bed_elevs)

bed_elev_timeseries_2.plot(time_array, bed_elev_data, linewidth = 1, color = 'k')
bed_elev_timeseries_2.scatter(observed_times, observed_bed_elevs, marker = 's', facecolor = 'darkgray', edgecolor = 'k')
bed_elev_timeseries_2.set_ylabel('$h$ [m]')

bed_elev_timeseries_2.set_xticks(np.arange(0, 6))
bed_elev_timeseries_2.set_xticklabels(['3/2019', '3/2020', '3/2021', '3/2022', '3/2023', '3/2024'])
bed_elev_timeseries_2.set_xlabel('Date [m/yyyy]')

bed_elev_timeseries_2.text(0.01, 0.78, 'H', transform=bed_elev_timeseries_2.transAxes, fontsize = 20)
bed_elev_timeseries_2.set_ylim(0.4, 1.03)

bestfit_k_ero_2 = data_2.iloc[-1, 0]
bestfit_k_dep_2 = data_2.iloc[-1, 1]


misfit_scatter_2.text(0.23, 0.73, 
                      '$k^*_{\mathrm{ero}}$ = ' + '%.2f'%np.round(bestfit_k_ero_2, 2) + '\n' + '$k^*_{\mathrm{dep}}$ = ' + '%.1f'%np.round(bestfit_k_dep_2, 1), 
                      transform=misfit_scatter_2.transAxes, fontsize = 12,
                      bbox = dict(edgecolor = 'k', facecolor = 'white', boxstyle='round', alpha = 0.5))

#arrowprops = {'arrowstyle': 'simple',
#              'color' : 'k'}

#misfit_scatter_2.annotate('$K^*_{\mathrm{ero}}$ = 0.20' + '\n' + '$K^*_{\mathrm{dep}}$ = 84.1', 
#                          xy = (0.6, 0.85), xytext = (0.1,0.8), 
#               fontsize = 12, va = 'center', xycoords = 'axes fraction', 
#               arrowprops = arrowprops)
print(max(bed_elev_data) - min(bed_elev_data))

fig.savefig('figure_10_case_study_hires.png', dpi = 1000, bbox_inches = 'tight')
fig.savefig('figure_10_case_study_lores.png', dpi = 100, bbox_inches = 'tight')
