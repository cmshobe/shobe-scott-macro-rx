#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Create figure 7 in Shobe and Scott: Effects of erosion and deposition constants 
on channel geometry.

Created February 2026 by @author: charlesshobe
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#run from which to get data
run_name = 'figure_7_nofp'
data = np.load('../results/sweep_k_values_' + str(run_name) + '.npy')

#convert to pandas dataframe for seaborn compatibility
df = pd.DataFrame({'k_ero': data[:, 0], 
                   'k_dep': data[:, 1],
                   'width': data[:, 2], 
                   'depth': data[:, 3],
                   'slope': data[:, 4],
                   'e_slope': data[:, 5],
                   'tau_bed': data[:, 6],
                   'tau_bank': data[:, 7],
                   'fr/f0': data[:, 8],
                   'teq': data[:, 9]})

theta = 60 #degrees
z0 = 0.1 #m
df['w_r'] = df['width'] + 2 * (df['depth'] / np.tan(np.radians(theta)))

#run from which to normalize
run_name_norm = 'figure_4'
data_norm = np.load('../results/sweep_z0_values_' + str(run_name_norm) + '.npy')

#convert to pandas dataframe for seaborn compatibility
df_norm = pd.DataFrame({'z0': data_norm[:, 0], 
                   'width': data_norm[:, 1], 
                   'depth': data_norm[:, 2],
                   'slope': data_norm[:, 3],
                   'e_slope': data_norm[:, 4],
                   'tau_bed': data_norm[:, 5],
                   'tau_bank': data_norm[:, 6],
                   'fr/f0': data_norm[:, 7],
                   'teq': data_norm[:, 8]})

#w_r = wb + 2 * (d_r / np.tan(theta))
df_norm['w_r'] = df_norm['width'] + 2 * (df_norm['depth'] / np.tan(np.radians(60)))



#normalize outputs (except fr/f) to output value for z0 = 0.01 m
min_rx = min(df_norm['z0']) #minimum z0 used
df['width_norm'] = df['width'] / float(df_norm['width'][df_norm['z0'] == min_rx].iloc[0])
df['w_r_norm'] = df['w_r'] / float(df_norm['w_r'][df_norm['z0'] == min_rx].iloc[0])
df['depth_norm'] = df['depth'] / float(df_norm['depth'][df_norm['z0'] == min_rx].iloc[0])
df['slope_norm'] = df['slope'] / float(df_norm['slope'][df_norm['z0'] == min_rx].iloc[0])
df['e_slope_norm'] = df['e_slope'] / float(df_norm['e_slope'][df_norm['z0'] == min_rx].iloc[0])
df['tau_bed_norm'] = df['tau_bed'] / float(df_norm['tau_bed'][df_norm['z0'] == min_rx].iloc[0])
df['tau_bank_norm'] = df['tau_bank'] / float(df_norm['tau_bank'][df_norm['z0'] == min_rx].iloc[0])
df['fr/f0 norm'] = df['fr/f0'] / float(df_norm['fr/f0'][df_norm['z0'] == min_rx].iloc[0])

#calculate relative roughness
bank_angle = 60
df['R'] = ((df['width'] + (df['depth']/np.tan(np.radians(bank_angle)))) * df['depth']) / (df['width'] + 2 * (df['depth'] / np.sin(np.radians(bank_angle))))
df['rel_rx'] = df['R'] / z0

#calculate bed elevation
reach_length = 1000 #m
h_baselevel = 0
df['bed_elev'] = df['slope'] * reach_length + h_baselevel
df_norm['bed_elev'] = df_norm['slope'] * reach_length + h_baselevel
df['bed_elev_norm'] = df['bed_elev'] / float(df_norm['bed_elev'][df_norm['z0'] == min_rx].iloc[0])




###########run from which to get filling regime shape
run_name_fill = 'figure_7'#'figure_k_rev1_L1000_tol1e-13_dt1000_n100_ero1-5_dep10-50_hfp5_newSw'
data_fill = np.load('../results/sweep_k_values_' + str(run_name_fill) + '.npy')

#convert to pandas dataframe for seaborn compatibility
df_fill = pd.DataFrame({'k_ero': data_fill[:, 0], 
                   'k_dep': data_fill[:, 1],
                   'width': data_fill[:, 2], 
                   'depth': data_fill[:, 3],
                   'slope': data_fill[:, 4],
                   'e_slope': data_fill[:, 5],
                   'tau_bed': data_fill[:, 6],
                   'tau_bank': data_fill[:, 7],
                   'fr/f0': data_fill[:, 8],
                   'teq': data_fill[:, 9]})

df['filled_flag'] = 0
df.loc[df_fill['slope'] >= 0.01056, 'filled_flag'] = 1


#meshgrid parameters
n = 20
ero = np.logspace(-1, np.log10(5), n)#np.logspace(-1, 1, 10)#np.linspace(1, 5, num = n)
dep = np.logspace(1, 2, 20)#np.linspace(10, 50, num = n)

X, Y = np.meshgrid(ero, dep)

#plot parameters
lines = ':'
k_ero_lims = (min(ero), max(ero))
k_dep_lims = (min(dep), max(dep))


text_500_x = 0.
text_500_y = 0.63
text_500_r = 48

text_200_x = 0.
text_200_y = 0.4
text_200_r = 48

text_100_x = 0.
text_100_y = 0.11
text_100_r = 48

text_50_x = 0.22
text_50_y = 0.19
text_50_r = 48

text_20_x = 0.34
text_20_y = 0.02
text_20_r = 48

text_10_x = 0.52
text_10_y = 0.02
text_10_r = 48

text_5_x = 0.67
text_5_y = 0.02
text_5_r = 48



######start figure
fig, axs = plt.subplots(3,2, figsize = (8,8))

width = axs[0, 0]
depth = axs[0, 1]
slope = axs[1, 0]
tau = axs[1, 1]
f_ratio = axs[2, 0]
rel_rx = axs[2, 1]

cbar_ax = fig.add_axes([.93, .35, .03, .3])

clevels2 = np.array([0.5, 1.5])
arr2 = np.array(df['filled_flag']).reshape(n,n)
alpha2 = 0.5
alpha2_line = 1

###########width subplot

vmin_w = min(df['width_norm'])
vmax_w = max(df['width_norm'])

arr = np.array(df['width_norm']).reshape(n,n)



clevels = np.arange(0, 14, 1)
contsf = width.contourf(X, Y, arr, zorder = 0, vmin = vmin_w, vmax = vmax_w,
                     levels = clevels)
conts = width.contour(X, Y, arr, zorder = 1, vmin = vmin_w, vmax = vmax_w, 
                   colors = 'k', levels = clevels)
width.clabel(conts, fontsize = 12, zorder = 1)
contsf2 = width.contourf(X, Y, arr2, levels = clevels2, cmap = 'binary', alpha = alpha2, vmin = 0.5, vmax = 0.5)
conts2 = width.contour(X, Y, arr2, levels = clevels2, alpha = alpha2_line, colors = 'white', vmin = 0.5, vmax = 0.5)

x = np.arange(min(ero), max(ero) + 1)
width.plot(x, x * 500, color = 'w', linewidth = 2, zorder = 10, linestyle = lines) #kero/kdep = 1/500
width.plot(x, x * 200, color = 'w', linewidth = 2, zorder = 10, linestyle = lines) #kero/kdep = 1/200
width.plot(x, x * 100, color = 'w', linewidth = 2, zorder = 10, linestyle = lines) #kero/kdep = 1/100
width.plot(x, x * 50, color = 'w', linewidth = 2, zorder = 10, linestyle = lines) #kero/kdep = 1/50
width.plot(x, x * 20, color = 'w', linewidth = 2, zorder = 10, linestyle = lines) #kero/kdep = 1/20
width.plot(x, x * 10, color = 'w', linewidth = 2, zorder = 10, linestyle = lines) #kero/kdep = 1/10
width.plot(x, x * 5, color = 'w', linewidth = 2, zorder = 10, linestyle = lines) #kero/kdep = 1/5
width.set_xlim(k_ero_lims)
width.set_ylim(k_dep_lims)

#dummy colorbar mappable
import matplotlib.colors as mcolors
import matplotlib.cm as cm
vmin = 0
vmax = 100
colormap = 'viridis'
norm = mcolors.Normalize(vmin=vmin, vmax=vmax)
mappable = cm.ScalarMappable(norm = norm, cmap = colormap)

fig.colorbar(mappable, cax = cbar_ax)
cbar_ax.set_ylim(vmin, vmax)
cbar_ax.set_ylabel('Quantity of interest', labelpad = -20, fontsize = 12)
cbar_ax.set_yticks(np.array([vmin, vmax]))
cbar_ax.set_yticklabels(['Low', 'High'])

width.set_ylabel(r'$k^*_{\mathrm{dep}}$')
width.set_title('A) Normalized width [-]')

#now annotate each line 
width.text(text_500_x, text_500_y, r'$500$', color = 'w',
        transform=width.transAxes, rotation = text_5_r, fontsize = 14)
width.text(text_200_x, text_200_y, r'$200$', color = 'w',
        transform=width.transAxes, rotation = text_20_r, fontsize = 14)
width.text(text_100_x, text_100_y, r'$100$', color = 'w',
        transform=width.transAxes, rotation = text_10_r, fontsize = 14)
width.text(text_50_x, text_50_y, r'$50$', color = 'w',
        transform=width.transAxes, rotation = text_5_r, fontsize = 14)
width.text(text_20_x, text_20_y, r'$20$', color = 'w',
        transform=width.transAxes, rotation = text_20_r, fontsize = 14)
width.text(text_10_x, text_10_y, r'$10$', color = 'w',
        transform=width.transAxes, rotation = text_10_r, fontsize = 14)
width.text(text_5_x, text_5_y, r'$k^*_{\mathrm{dep}}/k^*_{\mathrm{ero}}=5$', color = 'w',
        transform=width.transAxes, rotation = text_5_r, fontsize = 14)

width.set_xscale('log')
width.set_yscale('log')
width.get_xaxis().set_ticklabels([])


##########depth subplot
vmin_d = min(df['depth_norm'])
vmax_d = max(df['depth_norm'])

arr = np.array(df['depth_norm']).reshape(n,n)



clevels = np.arange(0, 5.5, 0.5)
contsf = depth.contourf(X, Y, arr, zorder = 0, vmin = vmin_d, vmax = vmax_d,
                     levels = clevels)
conts = depth.contour(X, Y, arr, zorder = 1, vmin = vmin_d, vmax = vmax_d, 
                   colors = 'k', levels = clevels)
depth.clabel(conts, fontsize = 12, zorder = 1)
contsf2 = depth.contourf(X, Y, arr2, levels = clevels2, cmap = 'binary', alpha = alpha2, vmin = 0.5, vmax = 0.5)
conts2 = depth.contour(X, Y, arr2, levels = clevels2, alpha = alpha2_line, colors = 'white', vmin = 0.5, vmax = 0.5)

depth.plot(x, x * 500, color = 'w', linewidth = 2, zorder = 10, linestyle = lines) #kero/kdep = 1/500
depth.plot(x, x * 200, color = 'w', linewidth = 2, zorder = 10, linestyle = lines) #kero/kdep = 1/200
depth.plot(x, x * 100, color = 'w', linewidth = 2, zorder = 10, linestyle = lines) #kero/kdep = 1/100
depth.plot(x, x * 50, color = 'w', linewidth = 2, zorder = 10, linestyle = lines) #kero/kdep = 1/50
depth.plot(x, x * 20, color = 'w', linewidth = 2, zorder = 10, linestyle = lines) #kero/kdep = 1/20
depth.plot(x, x * 10, color = 'w', linewidth = 2, zorder = 10, linestyle = lines) #kero/kdep = 1/10
depth.plot(x, x * 5, color = 'w', linewidth = 2, zorder = 10, linestyle = lines) #kero/kdep = 1/5
depth.set_xlim(k_ero_lims)
depth.set_ylim(k_dep_lims)

depth.set_title('B) Normalized depth [-]')

depth.set_xscale('log')
depth.set_yscale('log')

depth.get_xaxis().set_ticklabels([])
depth.get_yaxis().set_ticklabels([])
depth.tick_params(axis='y', which = 'minor', labelleft=False)


###############slope subplot
vmin_s = min(df['slope_norm'])
vmax_s = max(df['slope_norm'])

arr = np.array(df['slope_norm']).reshape(n,n)



clevels = np.arange(0, 10.0, 1)
contsf = slope.contourf(X, Y, arr, zorder = 0, vmin = vmin_s, vmax = vmax_s,
                     levels = clevels)
conts = slope.contour(X, Y, arr, zorder = 1, vmin = vmin_s, vmax = vmax_s, 
                   colors = 'k', levels = clevels)
slope.clabel(conts, fontsize = 12, zorder = 1)
contsf2 = slope.contourf(X, Y, arr2, levels = clevels2, cmap = 'binary', alpha = alpha2, vmin = 0.5, vmax = 0.5)
conts2 = slope.contour(X, Y, arr2, levels = clevels2, alpha = alpha2_line, colors = 'white', vmin = 0.5, vmax = 0.5)

slope.plot(x, x * 500, color = 'w', linewidth = 2, zorder = 10, linestyle = lines) #kero/kdep = 1/500
slope.plot(x, x * 200, color = 'w', linewidth = 2, zorder = 10, linestyle = lines) #kero/kdep = 1/200
slope.plot(x, x * 100, color = 'w', linewidth = 2, zorder = 10, linestyle = lines) #kero/kdep = 1/100
slope.plot(x, x * 50, color = 'w', linewidth = 2, zorder = 10, linestyle = lines) #kero/kdep = 1/50
slope.plot(x, x * 20, color = 'w', linewidth = 2, zorder = 10, linestyle = lines) #kero/kdep = 1/20
slope.plot(x, x * 10, color = 'w', linewidth = 2, zorder = 10, linestyle = lines) #kero/kdep = 1/10
slope.plot(x, x * 5, color = 'w', linewidth = 2, zorder = 10, linestyle = lines) #kero/kdep = 1/5
slope.set_xlim(k_ero_lims)
slope.set_ylim(k_dep_lims)

slope.set_ylabel(r'$k^*_{\mathrm{dep}}$')
slope.set_title('C) Normalized local bed slope [-]')

slope.set_xscale('log')
slope.set_yscale('log')

slope.get_xaxis().set_ticklabels([])


################tau_subplot (bank??)
vmin_t = min(df['tau_bank_norm'])
vmax_t = max(df['tau_bank_norm'])

arr = np.array(df['tau_bank_norm']).reshape(n,n)



clevels = np.arange(0, 2.5, 0.25)
contsf = tau.contourf(X, Y, arr, zorder = 0, vmin = vmin_t, vmax = vmax_t,
                     levels = clevels)
conts = tau.contour(X, Y, arr, zorder = 1, vmin = vmin_t, vmax = vmax_t, 
                   colors = 'k', levels = clevels)
tau.clabel(conts, fontsize = 12, zorder = 1)
contsf2 = tau.contourf(X, Y, arr2, levels = clevels2, cmap = 'binary', alpha = alpha2, vmin = 0.5, vmax = 0.5)
conts2 = tau.contour(X, Y, arr2, levels = clevels2, alpha = alpha2_line, colors = 'white', vmin = 0.5, vmax = 0.5)

tau.plot(x, x * 500, color = 'w', linewidth = 2, zorder = 10, linestyle = lines) #kero/kdep = 1/500
tau.plot(x, x * 200, color = 'w', linewidth = 2, zorder = 10, linestyle = lines) #kero/kdep = 1/200
tau.plot(x, x * 100, color = 'w', linewidth = 2, zorder = 10, linestyle = lines) #kero/kdep = 1/100
tau.plot(x, x * 50, color = 'w', linewidth = 2, zorder = 10, linestyle = lines) #kero/kdep = 1/50
tau.plot(x, x * 20, color = 'w', linewidth = 2, zorder = 10, linestyle = lines) #kero/kdep = 1/20
tau.plot(x, x * 10, color = 'w', linewidth = 2, zorder = 10, linestyle = lines) #kero/kdep = 1/10
tau.plot(x, x * 5, color = 'w', linewidth = 2, zorder = 10, linestyle = lines) #kero/kdep = 1/5
tau.set_xlim(k_ero_lims)
tau.set_ylim(k_dep_lims)

tau.set_title('D) Normalized bank shear stress [-]')

tau.set_xscale('log')
tau.set_yscale('log')

tau.get_xaxis().set_ticklabels([])
tau.get_yaxis().set_ticklabels([])
tau.tick_params(axis='y', which = 'minor', labelleft=False)

################fric_factor ratio subplot
vmin_f = min(df['fr/f0'])
vmax_f = max(df['fr/f0'])

arr = np.array(df['fr/f0']).reshape(n,n)



clevels = np.arange(0, 3, 0.25)
contsf_f_ratio = f_ratio.contourf(X, Y, arr, zorder = 0, vmin = vmin_f, vmax = vmax_f,
                     levels = clevels)
conts = f_ratio.contour(X, Y, arr, zorder = 1, vmin = vmin_f, vmax = vmax_f, 
                   colors = 'k', levels = clevels)
f_ratio.clabel(conts, fontsize = 12, zorder = 1)
contsf2 = f_ratio.contourf(X, Y, arr2, levels = clevels2, cmap = 'binary', alpha = alpha2, vmin = 0.5, vmax = 0.5)
conts2 = f_ratio.contour(X, Y, arr2, levels = clevels2, alpha = alpha2_line, colors = 'white', vmin = 0.5, vmax = 0.5)

f_ratio.plot(x, x * 500, color = 'w', linewidth = 2, zorder = 10, linestyle = lines) #kero/kdep = 1/500
f_ratio.plot(x, x * 200, color = 'w', linewidth = 2, zorder = 10, linestyle = lines) #kero/kdep = 1/200
f_ratio.plot(x, x * 100, color = 'w', linewidth = 2, zorder = 10, linestyle = lines) #kero/kdep = 1/100
f_ratio.plot(x, x * 50, color = 'w', linewidth = 2, zorder = 10, linestyle = lines) #kero/kdep = 1/50
f_ratio.plot(x, x * 20, color = 'w', linewidth = 2, zorder = 10, linestyle = lines) #kero/kdep = 1/20
f_ratio.plot(x, x * 10, color = 'w', linewidth = 2, zorder = 10, linestyle = lines) #kero/kdep = 1/10
f_ratio.plot(x, x * 5, color = 'w', linewidth = 2, zorder = 10, linestyle = lines) #kero/kdep = 1/5
f_ratio.set_xlim(k_ero_lims)
f_ratio.set_ylim(k_dep_lims)

f_ratio.set_xlabel(r'$k^*_{\mathrm{ero}}$')
f_ratio.set_ylabel(r'$k^*_{\mathrm{dep}}$')
f_ratio.set_title('E) Friction factor ratio $f_r/f$ [-]')

f_ratio.set_xscale('log')
f_ratio.set_yscale('log')

################relative submergence subplot
vmin_r = min(df['rel_rx'])
vmax_r = max(df['rel_rx'])

arr = np.array(df['rel_rx']).reshape(n,n)



clevels = np.arange(0, 35, 4)
contsf = rel_rx.contourf(X, Y, arr, zorder = 0, vmin = vmin_r, vmax = vmax_r,
                     levels = clevels)
conts = rel_rx.contour(X, Y, arr, zorder = 1, vmin = vmin_r, vmax = vmax_r, 
                   colors = 'k', levels = clevels)
rel_rx.clabel(conts, fontsize = 12, zorder = 1)
contsf2 = rel_rx.contourf(X, Y, arr2, levels = clevels2, cmap = 'binary', alpha = alpha2, vmin = 0.5, vmax = 0.5)
conts2 = rel_rx.contour(X, Y, arr2, levels = clevels2, alpha = alpha2_line, colors = 'white', vmin = 0.5, vmax = 0.5)

rel_rx.plot(x, x * 500, color = 'w', linewidth = 2, zorder = 10, linestyle = lines) #kero/kdep = 1/500
rel_rx.plot(x, x * 200, color = 'w', linewidth = 2, zorder = 10, linestyle = lines) #kero/kdep = 1/200
rel_rx.plot(x, x * 100, color = 'w', linewidth = 2, zorder = 10, linestyle = lines) #kero/kdep = 1/100
rel_rx.plot(x, x * 50, color = 'w', linewidth = 2, zorder = 10, linestyle = lines) #kero/kdep = 1/50
rel_rx.plot(x, x * 20, color = 'w', linewidth = 2, zorder = 10, linestyle = lines) #kero/kdep = 1/20
rel_rx.plot(x, x * 10, color = 'w', linewidth = 2, zorder = 10, linestyle = lines) #kero/kdep = 1/10
rel_rx.plot(x, x * 5, color = 'w', linewidth = 2, zorder = 10, linestyle = lines) #kero/kdep = 1/5
rel_rx.set_xlim(k_ero_lims)
rel_rx.set_ylim(k_dep_lims)

rel_rx.set_xlabel(r'$k^*_{\mathrm{ero}}$')
rel_rx.set_title('F) Relative submergence $R_r/z_0$ [-]')

rel_rx.set_xscale('log')
rel_rx.set_yscale('log')

rel_rx.get_yaxis().set_ticklabels([])
rel_rx.tick_params(axis='y', which = 'minor', labelleft=False)

###########################################

fig.savefig('figure_7_hires.png', dpi = 1000, bbox_inches = 'tight')
fig.savefig('figure_7_lores.png', dpi = 100, bbox_inches = 'tight')
