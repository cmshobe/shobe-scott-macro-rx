#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Create figure 9 in Shobe and Scott: Case study results.

Created February 2026 by @author: charlesshobe
"""

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import colors
import seaborn as sns
import numpy as np
from datetime import datetime

run_name = 'figure_9_inversion_low_z0_inversion_record.csv'
colnames = ['k_ero', 'k_dep', 'misfit']
data = (pd.read_csv('../results/' + str(run_name), header = None, names = colnames)
        .sort_values(by = 'misfit', ascending = False))


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
time = duration_2019_2024.total_seconds()

#set up the figure grid
fig = plt.figure(figsize=(10,10))
widths = [3, 0.75, 0.75, 3, 0.75]
heights = [3, 1, 1, 5, 1.1, 2, 0.25, 2]
spec = fig.add_gridspec(ncols=len(widths), nrows=len(heights), width_ratios=widths,
                          height_ratios=heights, wspace=0.0, hspace=0.0)

reach_length = 1100.2

observed_widths = np.array([43.6, 45., 46., 45.9])
observed_bed_elevs = np.array([0.0029, 0.0028, 0.0032, 0.003]) * reach_length

#axis limit params
k_ero_min = 0.01
k_ero_max = 10.02

k_dep_min = 0
k_dep_max = 122

#DATA and axis lims FOR BOUNDARY CONDITION PLOTS
low_z0_values = np.array([0.13, 0.13, 0.14])
high_z0_values = np.array([0.22, 0.20, 0.23])

l_bed_obst_values = np.array([1.74, 1.35, 1.84])
l_bank_obst_values = np.array([0.95, 0.61, 0.92])#np.array([1.91, 1.23, 1.84])

#x-tick array for A,B,E,F,G,H
#x-tick label array for A,B,E,F,G,H
time_ticks = np.arange(0, time + 1000, time / 5)
time_tick_labels = ['3/2019', '3/2020', '3/2021', '3/2022', '3/2023', '3/2024']


#LEFT COLUMN: z0 CASE 1#################################################

bc_plot = fig.add_subplot(spec[0, 0])
k_ero_hist = fig.add_subplot(spec[2, 0])
misfit_scatter = fig.add_subplot(spec[3, 0])
k_dep_hist = fig.add_subplot(spec[3, 1])
width_timeseries = fig.add_subplot(spec[5, 0])
bed_elev_timeseries = fig.add_subplot(spec[7, 0])

observed_times = np.array([0, time_checkpoint_1, time_checkpoint_2, time])

linewidth = 5

z0_color = '#fb8072'
bank_obst_color = '#8dd3c7'
bed_obst_color = '#bebada'

bc_plot.hlines(y = low_z0_values[0], xmin = observed_times[0], 
                xmax = observed_times[1], linewidth = linewidth, color = z0_color,
                label = '$z_0$')
bc_plot.hlines(y = low_z0_values[1], xmin = observed_times[1], 
                xmax = observed_times[2], linewidth = linewidth, color = z0_color)
bc_plot.hlines(y = low_z0_values[2], xmin = observed_times[2], 
                xmax = observed_times[3], linewidth = linewidth, color = z0_color)

fc_plot = bc_plot.twinx()
fc_plot.hlines(y = l_bed_obst_values[0], xmin = observed_times[0], 
                xmax = observed_times[1], linewidth = linewidth, color = bed_obst_color, linestyle = '--',
                label = '$w^{\mathrm{bed}}_{\mathrm{roughness}}$')
fc_plot.hlines(y = l_bed_obst_values[1], xmin = observed_times[1], 
                xmax = observed_times[2], linewidth = linewidth, color = bed_obst_color, linestyle = '--')
fc_plot.hlines(y = l_bed_obst_values[2], xmin = observed_times[2], 
                xmax = observed_times[3], linewidth = linewidth, color = bed_obst_color, linestyle = '--')

fc_plot.hlines(y = l_bank_obst_values[0], xmin = observed_times[0], 
                xmax = observed_times[1], linewidth = linewidth, color = bank_obst_color, linestyle = '--',
                label = '$l^{\mathrm{bank}}_{\mathrm{roughness}}$')
fc_plot.hlines(y = l_bank_obst_values[1], xmin = observed_times[1], 
                xmax = observed_times[2], linewidth = linewidth, color = bank_obst_color, linestyle = '--')
fc_plot.hlines(y = l_bank_obst_values[2], xmin = observed_times[2], 
                xmax = observed_times[3], linewidth = linewidth, color = bank_obst_color, linestyle = '--')

#merge handles and labels for legend
lines, labels = bc_plot.get_legend_handles_labels()
lines2, labels2 = fc_plot.get_legend_handles_labels()

bc_plot.legend(lines + lines2, labels + labels2, bbox_to_anchor = (0.69, 1.35), 
               loc = 'upper left', ncols = 3, framealpha = 1, edgecolor = 'k')

bc_plot.set_xticks(time_ticks)
bc_plot.set_xticklabels(time_tick_labels)
bc_plot.set_xlabel('Date [m/yyyy]')
bc_plot.set_ylabel('$z_0$ [m]')
bc_plot.set_ylim(0.1, 0.7)
bc_plot.set_yticks(np.array([0.1, 0.3]))
bc_plot.yaxis.set_label_coords(-0.13, 0.18)

fc_plot.set_ylim(-2, 2.5)
fc_plot.set_yticks(np.array([0, 2]))
fc_plot.set_ylabel('$w^{\mathrm{bed}}_{\mathrm{roughness}}$ and' + '\n' '$l^{\mathrm{bank}}_{\mathrm{roughness}}$ ' + '[m]')
fc_plot.yaxis.set_label_coords(1.1, 0.72)

fc_plot.text(0.01, 0.83, 'A', transform=fc_plot.transAxes, fontsize = 20, zorder = 10)


sns.kdeplot(data = data, x = 'k_ero', ax= k_ero_hist, color='k', log_scale = 10)
k_ero_hist.axis('off')
k_ero_hist.set_xlim(k_ero_min, k_ero_max)

sns.kdeplot(data = data, y = 'k_dep', ax = k_dep_hist, color='k')
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
c.ax.set_xticks(np.array([data.misfit.min(), data.misfit.max()]))
c.ax.set_xticklabels(['low', 'high'])
cax.set_title('log(misfit) [-]', fontsize=12)

misfit_scatter.set_xlabel('$k^*_{\mathrm{ero}}$ [-]', labelpad = 0)
misfit_scatter.set_ylabel('$k^*_{\mathrm{dep}}$ [-]', labelpad = -5)

misfit_scatter.set_xlim(k_ero_min, k_ero_max)
misfit_scatter.set_ylim(k_dep_min, k_dep_max)

misfit_scatter.set_xscale('log')

misfit_scatter.text(0.01, 0.9, 'C', transform=misfit_scatter.transAxes, fontsize = 20)



#bring in width timeseries data
bestfit_run_name_low_z0 = 'figure_9_bestfit_low_z0'
width_data = np.load('../results/' + str(bestfit_run_name_low_z0) + '_widths.npy')
time_array = np.arange(0, time + 100, 100) #seconds per year


width_timeseries.plot(time_array, width_data, linewidth = 1, color = 'k',
                      label = 'modeled')

width_timeseries.errorbar(observed_times, observed_widths, yerr = np.repeat(2.5, 4), 
                               xerr = None, fmt = 'none', color = 'darkgray', zorder = 0)

width_timeseries.scatter(observed_times, observed_widths, marker = 's', 
                         facecolor = 'darkgray', edgecolor = 'k',
                         label = 'observed')
width_timeseries.set_ylim(40, 50)
width_timeseries.set_ylabel('$w_b$ [m]')
width_timeseries.get_xaxis().set_ticklabels([])

width_timeseries.text(0.01, 0.75, 'E', transform=width_timeseries.transAxes, fontsize = 20)




bed_elev_data = np.load('../results/' + str(bestfit_run_name_low_z0) + '_slopes.npy') * reach_length

bed_elev_timeseries.plot(time_array, bed_elev_data, linewidth = 1, color = 'k',
                         label = 'modeled')
bed_elev_timeseries.errorbar(observed_times, observed_bed_elevs, yerr = np.repeat(0.5, 4), 
                               xerr = None, fmt = 'none', color = 'darkgray', zorder = 0)
bed_elev_timeseries.scatter(observed_times, observed_bed_elevs, marker = 's', 
                            facecolor = 'darkgray', edgecolor = 'k', label = 'observed')
bed_elev_timeseries.set_ylabel('$h$ [m]')

bed_elev_timeseries.set_xticks(time_ticks)
bed_elev_timeseries.set_xticklabels(time_tick_labels)
bed_elev_timeseries.set_xlabel('Date [m/yyyy]')

bed_elev_timeseries.legend(bbox_to_anchor = (0.95, 1.35), loc = 'upper left', 
                        bbox_transform = bed_elev_timeseries.transAxes,
                        framealpha = 1, edgecolor = 'k')

bed_elev_timeseries.text(0.01, 0.76, 'G', transform=bed_elev_timeseries.transAxes, fontsize = 20)

bestfit_k_ero = data.iloc[-1, 0]
bestfit_k_dep = data.iloc[-1, 1]

misfit_scatter.text(0.6, 0.75, 
                      '$k^*_{\mathrm{ero}}$ = ' + '%.2f'%np.round(bestfit_k_ero, 2) + '\n' + '$k^*_{\mathrm{dep}}$ = ' + '%.1f'%np.round(bestfit_k_dep, 1), 
                      transform=misfit_scatter.transAxes, fontsize = 12,
                      bbox = dict(edgecolor = 'k', facecolor = 'white', boxstyle='round', alpha = 0.5))

#RIGHT COLUMN COLUMN: z0 CASE 2######################################

run_name_2 = 'figure_9_inversion_high_z0_inversion_record.csv'
data_2 = pd.read_csv('../results/' + str(run_name_2), header = None, names = colnames).sort_values(by = 'misfit', ascending = False)

bc_plot_2 = fig.add_subplot(spec[0, 3])
k_ero_hist_2 = fig.add_subplot(spec[2, 3])
misfit_scatter_2 = fig.add_subplot(spec[3, 3])
k_dep_hist_2 = fig.add_subplot(spec[3, 4])
width_timeseries_2 = fig.add_subplot(spec[5, 3])
bed_elev_timeseries_2 = fig.add_subplot(spec[7, 3])

bc_plot_2.hlines(y = high_z0_values[0], xmin = observed_times[0], 
                xmax = observed_times[1], linewidth = linewidth, color = z0_color,
                label = '$z_0$')
bc_plot_2.hlines(y = high_z0_values[1], xmin = observed_times[1], 
                xmax = observed_times[2], linewidth = linewidth, color = z0_color)
bc_plot_2.hlines(y = high_z0_values[2], xmin = observed_times[2], 
                xmax = observed_times[3], linewidth = linewidth, color = z0_color)

fc_plot_2 = bc_plot_2.twinx()
fc_plot_2.hlines(y = l_bed_obst_values[0], xmin = observed_times[0], 
                xmax = observed_times[1], linewidth = linewidth, color = bed_obst_color,linestyle = '--',
                label = '$w^{\mathrm{bed}}_{\mathrm{roughness}}$')
fc_plot_2.hlines(y = l_bed_obst_values[1], xmin = observed_times[1], 
                xmax = observed_times[2], linewidth = linewidth, color = bed_obst_color,linestyle = '--')
fc_plot_2.hlines(y = l_bed_obst_values[2], xmin = observed_times[2], 
                xmax = observed_times[3], linewidth = linewidth, color = bed_obst_color,linestyle = '--')

fc_plot_2.hlines(y = l_bank_obst_values[0], xmin = observed_times[0], 
                xmax = observed_times[1], linewidth = linewidth, color = bank_obst_color,linestyle = '--',
                label = '$l^{\mathrm{bank}}_{\mathrm{roughness}}$')
fc_plot_2.hlines(y = l_bank_obst_values[1], xmin = observed_times[1], 
                xmax = observed_times[2], linewidth = linewidth, color = bank_obst_color, linestyle = '--')
fc_plot_2.hlines(y = l_bank_obst_values[2], xmin = observed_times[2], 
                xmax = observed_times[3], linewidth = linewidth, color = bank_obst_color, linestyle = '--')


#merge handles and labels for legend
lines, labels = bc_plot.get_legend_handles_labels()
lines2, labels2 = fc_plot.get_legend_handles_labels()

bc_plot_2.set_xticks(time_ticks)
bc_plot_2.set_xticklabels(time_tick_labels)
bc_plot_2.set_xlabel('Date [m/yyyy]')
bc_plot_2.set_ylabel('$z_0$ [m]')
bc_plot_2.set_ylim(0.1, 0.7)
bc_plot_2.set_yticks(np.array([0.1, 0.3]))
bc_plot_2.yaxis.set_label_coords(-0.13, 0.18)

fc_plot_2.set_ylim(-2, 2.5)
fc_plot_2.set_yticks(np.array([0, 2]))
fc_plot_2.set_ylabel('$w^{\mathrm{bed}}_{\mathrm{roughness}}$ and' + '\n' '$l^{\mathrm{bank}}_{\mathrm{roughness}}$ ' + '[m]')
fc_plot_2.yaxis.set_label_coords(1.1, 0.72)

fc_plot_2.text(0.01, 0.83, 'B', transform=fc_plot_2.transAxes, fontsize = 20)


sns.kdeplot(data = data_2, x = 'k_ero', ax= k_ero_hist_2, color='k', log_scale = 10)
k_ero_hist_2.axis('off')
k_ero_hist_2.set_xlim(k_ero_min, k_ero_max)

sns.kdeplot(data = data_2, y = 'k_dep', ax = k_dep_hist_2, color='k')
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
bestfit_run_name_high_z0 = 'figure_9_bestfit_high_z0'
width_data = np.load('../results/' + str(bestfit_run_name_high_z0) + '_widths.npy')
time_array = np.arange(0, time + 100, 100)

width_timeseries_2.plot(time_array, width_data, linewidth = 1, color = 'k')

width_timeseries_2.errorbar(observed_times, observed_widths, yerr = np.repeat(2.5, 4), 
                               xerr = None, fmt = 'none', color = 'darkgray', zorder = 0)

width_timeseries_2.scatter(observed_times, observed_widths, marker = 's', facecolor = 'darkgray', edgecolor = 'k')

width_timeseries_2.set_ylim(40, 50)
width_timeseries_2.set_ylabel('$w_b$ [m]')
width_timeseries_2.get_xaxis().set_ticklabels([])
width_timeseries_2.text(0.01, 0.75, 'F', transform=width_timeseries_2.transAxes, fontsize = 20)


bed_elev_data = np.load('../results/' + str(bestfit_run_name_high_z0) + '_slopes.npy') * reach_length


bed_elev_timeseries_2.plot(time_array, bed_elev_data, linewidth = 1, color = 'k')
bed_elev_timeseries_2.errorbar(observed_times, observed_bed_elevs, yerr = np.repeat(0.5, 4), 
                               xerr = None, fmt = 'none', color = 'darkgray', zorder = 0)
bed_elev_timeseries_2.scatter(observed_times, observed_bed_elevs, marker = 's', facecolor = 'darkgray', edgecolor = 'k')
bed_elev_timeseries_2.set_ylabel('$h$ [m]')

bed_elev_timeseries_2.set_xticks(np.arange(0, time + 1000, time / 5))
bed_elev_timeseries_2.set_xticklabels(['3/2019', '3/2020', '3/2021', '3/2022', '3/2023', '3/2024'])
bed_elev_timeseries_2.set_xlabel('Date [m/yyyy]')

bed_elev_timeseries_2.text(0.01, 0.76, 'H', transform=bed_elev_timeseries_2.transAxes, fontsize = 20)

bestfit_k_ero_2 = data_2.iloc[-1, 0]
bestfit_k_dep_2 = data_2.iloc[-1, 1]


misfit_scatter_2.text(0.6, 0.75, 
                      '$k^*_{\mathrm{ero}}$ = ' + '%.2f'%np.round(bestfit_k_ero_2, 2) + '\n' + '$k^*_{\mathrm{dep}}$ = ' + '%.1f'%np.round(bestfit_k_dep_2, 1), 
                      transform=misfit_scatter_2.transAxes, fontsize = 12,
                      bbox = dict(edgecolor = 'k', facecolor = 'white', boxstyle='round', alpha = 0.5))

fig.savefig('figure_9_hires.png', dpi = 1000, bbox_inches = 'tight')
fig.savefig('figure_9_lores.png', dpi = 100, bbox_inches = 'tight')
