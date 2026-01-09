#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  9 11:39:53 2026

@author: charlesshobe
"""
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


#run from which to get data
run_name = 'figure_k_rev1_L1000_tol1e-13_dt1000_exact_vals'
data = np.load('sweep_k_values_' + str(run_name) + '.npy')

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

#w_r = wb + 2 * (d_r / np.tan(theta))
df['w_r'] = df['width'] + 2 * (df['depth'] / np.tan(np.radians(60)))

#run from which to normalize
run_name_norm = 'figure_4_rev1_L1000_tol1e-13_dt1000_TESTkero1kdep10'
data_norm = np.load('../figure_4/sweep_z0_values_' + str(run_name_norm) + '.npy')

#convert to pandas dataframe for seaborn compatibility
df_norm = pd.DataFrame({'sigma_z': data_norm[:, 0], 
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



#normalize outputs (except fr/f) to output value for sigma_z = 0.01 m
min_rx = min(df_norm['sigma_z']) #minimum sigma_z used
df['width_norm'] = df['width'] / float(df_norm['width'][df_norm['sigma_z'] == min_rx].iloc[0])
df['w_r_norm'] = df['w_r'] / float(df_norm['w_r'][df_norm['sigma_z'] == min_rx].iloc[0])
df['depth_norm'] = df['depth'] / float(df_norm['depth'][df_norm['sigma_z'] == min_rx].iloc[0])
df['slope_norm'] = df['slope'] / float(df_norm['slope'][df_norm['sigma_z'] == min_rx].iloc[0])
df['e_slope_norm'] = df['e_slope'] / float(df_norm['e_slope'][df_norm['sigma_z'] == min_rx].iloc[0])
df['tau_bed_norm'] = df['tau_bed'] / float(df_norm['tau_bed'][df_norm['sigma_z'] == min_rx].iloc[0])
df['tau_bank_norm'] = df['tau_bank'] / float(df_norm['tau_bank'][df_norm['sigma_z'] == min_rx].iloc[0])
df['fr/f0 norm'] = df['fr/f0'] / float(df_norm['fr/f0'][df_norm['sigma_z'] == min_rx].iloc[0])

#calculate relative roughness
bank_angle = 60
df['R'] = ((df['width'] + (df['depth']/np.tan(np.radians(bank_angle)))) * df['depth']) / (df['width'] + 2 * (df['depth'] / np.sin(np.radians(bank_angle))))
df['rel_rx'] = df['R'] / 1#df['sigma_z']

#calculate bed elevation
reach_length = 1000 #m
h_baselevel = 0
df['bed_elev'] = df['slope'] * reach_length + h_baselevel
df_norm['bed_elev'] = df_norm['slope'] * reach_length + h_baselevel
df['bed_elev_norm'] = df['bed_elev'] / float(df_norm['bed_elev'][df_norm['sigma_z'] == min_rx].iloc[0])


#meshgrid parameters
n = 5
ero = np.linspace(1, 5, num = n)
dep = np.linspace(10, 50, num = n)

X, Y = np.meshgrid(ero, dep)

#plot parameters
lines = ':'


######start figure
fig, axs = plt.subplots(3,2, figsize = (8,8))

width = axs[0, 0]
depth = axs[0, 1]
slope = axs[1, 0]
tau = axs[1, 1]
f_ratio = axs[2, 0]
rel_rx = axs[2, 1]

cbar_ax = fig.add_axes([.91, .15, .03, .7])

###########width subplot

vmin_w = min(df['width_norm'])
vmax_w = max(df['width_norm'])

arr = np.array(df['width_norm']).reshape(n,n)



clevels = np.arange(0, 5.5, 0.5)
contsf = width.contourf(X, Y, arr, zorder = 0, vmin = vmin_w, vmax = vmax_w,
                     levels = clevels)
conts = width.contour(X, Y, arr, zorder = 2, vmin = vmin_w, vmax = vmax_w, 
                   colors = 'k', levels = clevels)
width.clabel(conts, fontsize = 12, zorder = 1)
#ax2 = ax.twinx()
x = np.arange(1,6)
width.plot(x, x * 30, color = 'w', linewidth = 2, zorder = 10, linestyle = lines) #kero/kdep = 1/30
width.plot(x, x * 20, color = 'w', linewidth = 2, zorder = 10, linestyle = lines) #kero/kdep = 1/20
width.plot(x, x * 10, color = 'w', linewidth = 2, zorder = 10, linestyle = lines) #kero/kdep = 1/10
width.plot(x, x * 5, color = 'w', linewidth = 2, zorder = 10, linestyle = lines) #kero/kdep = 1/5
width.plot(x, x * 3.33, color = 'w', linewidth = 2, zorder = 10, linestyle = lines) #kero/kdep = 1/3
width.set_xlim(1, 5)
width.set_ylim(10, 50)
#fig.colorbar(contsf, cax = cbar_ax)
cbar_ax.set_ylim(vmin_w, vmax_w)
cbar_ax.set_ylabel('Normalized width')
#ax.set_box_aspect(1) #set square but not with 'equal' because that relies on data coords

#width.set_xlabel(r'$k^*_{\mathrm{ero}}$')
width.set_ylabel(r'$k^*_{\mathrm{dep}}$')
width.get_xaxis().set_ticklabels([])
width.set_title('A) Normalized width [-]')

#now find a way to annotate each line 
width.text(0.075, 0.7, r'$k^*_{\mathrm{dep}}=30k^*_{\mathrm{ero}}$', color = 'w',
        transform=width.transAxes, rotation = 63)
width.text(0.27, 0.75, r'$k^*_{\mathrm{dep}}=20k^*_{\mathrm{ero}}$', color = 'w',
        transform=width.transAxes, rotation = 55)
width.text(0.75, 0.7, r'$k^*_{\mathrm{dep}}=10k^*_{\mathrm{ero}}$', color = 'w',
        transform=width.transAxes, rotation = 35)
width.text(0.78, 0.21, r'$k^*_{\mathrm{dep}}=5k^*_{\mathrm{ero}}$', color = 'w',
        transform=width.transAxes, rotation = 18)
width.text(0.8, 0.05, r'$k^*_{\mathrm{dep}}=3k^*_{\mathrm{ero}}$', color = 'w',
        transform=width.transAxes, rotation = 12)

##########depth subplot
vmin_d = min(df['depth_norm'])
vmax_d = max(df['depth_norm'])

arr = np.array(df['depth_norm']).reshape(n,n)



clevels = np.arange(0, 5.5, 0.5)
contsf = depth.contourf(X, Y, arr, zorder = 0, vmin = vmin_d, vmax = vmax_d,
                     levels = clevels)
conts = depth.contour(X, Y, arr, zorder = 2, vmin = vmin_d, vmax = vmax_d, 
                   colors = 'k', levels = clevels)
depth.clabel(conts, fontsize = 12, zorder = 1)
#ax2 = ax.twinx()
x = np.arange(1,6)
depth.plot(x, x * 30, color = 'w', linewidth = 2, zorder = 10, linestyle = lines) #kero/kdep = 1/30
depth.plot(x, x * 20, color = 'w', linewidth = 2, zorder = 10, linestyle = lines) #kero/kdep = 1/20
depth.plot(x, x * 10, color = 'w', linewidth = 2, zorder = 10, linestyle = lines) #kero/kdep = 1/10
depth.plot(x, x * 5, color = 'w', linewidth = 2, zorder = 10, linestyle = lines) #kero/kdep = 1/5
depth.plot(x, x * 3.33, color = 'w', linewidth = 2, zorder = 10, linestyle = lines) #kero/kdep = 1/3
depth.set_xlim(1, 5)
depth.set_ylim(10, 50)
#plt.tight_layout()
fig.colorbar(contsf, cax = cbar_ax)
cbar_ax.set_ylim(vmin_d, vmax_d)
cbar_ax.set_ylabel('Normalized width')
#ax.set_box_aspect(1) #set square but not with 'equal' because that relies on data coords

#depth.set_xlabel(r'$k^*_{\mathrm{ero}}$')
#depth.set_ylabel(r'$k^*_{\mathrm{dep}}$')
depth.get_xaxis().set_ticklabels([])
depth.get_yaxis().set_ticklabels([])
depth.set_title('B) Normalized depth [-]')

#now find a way to annotate each line 
depth.text(0.075, 0.7, r'$k^*_{\mathrm{dep}}=30k^*_{\mathrm{ero}}$', color = 'w',
        transform=depth.transAxes, rotation = 63)
depth.text(0.27, 0.75, r'$k^*_{\mathrm{dep}}=20k^*_{\mathrm{ero}}$', color = 'w',
        transform=depth.transAxes, rotation = 55)
depth.text(0.75, 0.7, r'$k^*_{\mathrm{dep}}=10k^*_{\mathrm{ero}}$', color = 'w',
        transform=depth.transAxes, rotation = 35)
depth.text(0.78, 0.21, r'$k^*_{\mathrm{dep}}=5k^*_{\mathrm{ero}}$', color = 'w',
        transform=depth.transAxes, rotation = 18)
depth.text(0.8, 0.05, r'$k^*_{\mathrm{dep}}=3k^*_{\mathrm{ero}}$', color = 'w',
        transform=depth.transAxes, rotation = 12)


###############slope subplot
vmin_s = min(df['slope_norm'])
vmax_s = max(df['slope_norm'])

arr = np.array(df['slope_norm']).reshape(n,n)



clevels = np.arange(0, 5.5, 0.5)
contsf = slope.contourf(X, Y, arr, zorder = 0, vmin = vmin_s, vmax = vmax_s,
                     levels = clevels)
conts = slope.contour(X, Y, arr, zorder = 2, vmin = vmin_s, vmax = vmax_s, 
                   colors = 'k', levels = clevels)
slope.clabel(conts, fontsize = 12, zorder = 1)
#ax2 = ax.twinx()
x = np.arange(1,6)
slope.plot(x, x * 30, color = 'w', linewidth = 2, zorder = 10, linestyle = lines) #kero/kdep = 1/30
slope.plot(x, x * 20, color = 'w', linewidth = 2, zorder = 10, linestyle = lines) #kero/kdep = 1/20
slope.plot(x, x * 10, color = 'w', linewidth = 2, zorder = 10, linestyle = lines) #kero/kdep = 1/10
slope.plot(x, x * 5, color = 'w', linewidth = 2, zorder = 10, linestyle = lines) #kero/kdep = 1/5
slope.plot(x, x * 3.33, color = 'w', linewidth = 2, zorder = 10, linestyle = lines) #kero/kdep = 1/3
slope.set_xlim(1, 5)
slope.set_ylim(10, 50)
#plt.tight_layout()
fig.colorbar(contsf, cax = cbar_ax)
cbar_ax.set_ylim(vmin_s, vmax_s)
cbar_ax.set_ylabel('Normalized width')
#ax.set_box_aspect(1) #set square but not with 'equal' because that relies on data coords

#slope.set_xlabel(r'$k^*_{\mathrm{ero}}$')
slope.set_ylabel(r'$k^*_{\mathrm{dep}}$')
slope.get_xaxis().set_ticklabels([])
slope.set_title('C) Normalized local bed slope [-]')

#now find a way to annotate each line 
slope.text(0.075, 0.7, r'$k^*_{\mathrm{dep}}=30k^*_{\mathrm{ero}}$', color = 'w',
        transform=slope.transAxes, rotation = 63)
slope.text(0.27, 0.75, r'$k^*_{\mathrm{dep}}=20k^*_{\mathrm{ero}}$', color = 'w',
        transform=slope.transAxes, rotation = 55)
slope.text(0.75, 0.7, r'$k^*_{\mathrm{dep}}=10k^*_{\mathrm{ero}}$', color = 'w',
        transform=slope.transAxes, rotation = 35)
slope.text(0.78, 0.21, r'$k^*_{\mathrm{dep}}=5k^*_{\mathrm{ero}}$', color = 'w',
        transform=slope.transAxes, rotation = 18)
slope.text(0.8, 0.05, r'$k^*_{\mathrm{dep}}=3k^*_{\mathrm{ero}}$', color = 'w',
        transform=slope.transAxes, rotation = 12)


################tau_subplot (bank??)
vmin_t = min(df['tau_bank_norm'])
vmax_t = max(df['tau_bank_norm'])

arr = np.array(df['tau_bank_norm']).reshape(n,n)



clevels = np.arange(0, 2.0, 0.2)
contsf = tau.contourf(X, Y, arr, zorder = 0, vmin = vmin_t, vmax = vmax_t,
                     levels = clevels)
conts = tau.contour(X, Y, arr, zorder = 2, vmin = vmin_t, vmax = vmax_t, 
                   colors = 'k', levels = clevels)
tau.clabel(conts, fontsize = 12, zorder = 1)
#ax2 = ax.twinx()
x = np.arange(1,6)
tau.plot(x, x * 30, color = 'w', linewidth = 2, zorder = 10, linestyle = lines) #kero/kdep = 1/30
tau.plot(x, x * 20, color = 'w', linewidth = 2, zorder = 10, linestyle = lines) #kero/kdep = 1/20
tau.plot(x, x * 10, color = 'w', linewidth = 2, zorder = 10, linestyle = lines) #kero/kdep = 1/10
tau.plot(x, x * 5, color = 'w', linewidth = 2, zorder = 10, linestyle = lines) #kero/kdep = 1/5
tau.plot(x, x * 3.33, color = 'w', linewidth = 2, zorder = 10, linestyle = lines) #kero/kdep = 1/3
tau.set_xlim(1, 5)
tau.set_ylim(10, 50)
#plt.tight_layout()
fig.colorbar(contsf, cax = cbar_ax)
cbar_ax.set_ylim(vmin_t, vmax_t)
cbar_ax.set_ylabel('Normalized width')
#ax.set_box_aspect(1) #set square but not with 'equal' because that relies on data coords

#tau.set_xlabel(r'$k^*_{\mathrm{ero}}$')
#tau.set_ylabel(r'$k^*_{\mathrm{dep}}$')
tau.get_xaxis().set_ticklabels([])
tau.get_yaxis().set_ticklabels([])
tau.set_title('D) Normalized bank shear stress [-]')

#now find a way to annotate each line 
tau.text(0.075, 0.7, r'$k^*_{\mathrm{dep}}=30k^*_{\mathrm{ero}}$', color = 'w',
        transform=tau.transAxes, rotation = 63)
tau.text(0.27, 0.75, r'$k^*_{\mathrm{dep}}=20k^*_{\mathrm{ero}}$', color = 'w',
        transform=tau.transAxes, rotation = 55)
tau.text(0.75, 0.7, r'$k^*_{\mathrm{dep}}=10k^*_{\mathrm{ero}}$', color = 'w',
        transform=tau.transAxes, rotation = 35)
tau.text(0.78, 0.21, r'$k^*_{\mathrm{dep}}=5k^*_{\mathrm{ero}}$', color = 'w',
        transform=tau.transAxes, rotation = 18)
tau.text(0.8, 0.05, r'$k^*_{\mathrm{dep}}=3k^*_{\mathrm{ero}}$', color = 'w',
        transform=tau.transAxes, rotation = 12)

################fric_factor ratio subplot
vmin_f = min(df['fr/f0'])
vmax_f = max(df['fr/f0'])

arr = np.array(df['fr/f0']).reshape(n,n)



clevels = np.arange(0, 7.5, 0.5)
contsf = f_ratio.contourf(X, Y, arr, zorder = 0, vmin = vmin_f, vmax = vmax_f,
                     levels = clevels)
conts = f_ratio.contour(X, Y, arr, zorder = 2, vmin = vmin_f, vmax = vmax_f, 
                   colors = 'k', levels = clevels)
f_ratio.clabel(conts, fontsize = 12, zorder = 1)
#ax2 = ax.twinx()
x = np.arange(1,6)
f_ratio.plot(x, x * 30, color = 'w', linewidth = 2, zorder = 10, linestyle = lines) #kero/kdep = 1/30
f_ratio.plot(x, x * 20, color = 'w', linewidth = 2, zorder = 10, linestyle = lines) #kero/kdep = 1/20
f_ratio.plot(x, x * 10, color = 'w', linewidth = 2, zorder = 10, linestyle = lines) #kero/kdep = 1/10
f_ratio.plot(x, x * 5, color = 'w', linewidth = 2, zorder = 10, linestyle = lines) #kero/kdep = 1/5
f_ratio.plot(x, x * 3.33, color = 'w', linewidth = 2, zorder = 10, linestyle = lines) #kero/kdep = 1/3
f_ratio.set_xlim(1, 5)
f_ratio.set_ylim(10, 50)
#plt.tight_layout()
fig.colorbar(contsf, cax = cbar_ax)
cbar_ax.set_ylim(vmin_f, vmax_f)
cbar_ax.set_ylabel('Normalized width')
#ax.set_box_aspect(1) #set square but not with 'equal' because that relies on data coords

f_ratio.set_xlabel(r'$k^*_{\mathrm{ero}}$')
f_ratio.set_ylabel(r'$k^*_{\mathrm{dep}}$')
f_ratio.set_title('E) Friction factor ratio $f_r/f$ [-]')

#now find a way to annotate each line 
f_ratio.text(0.075, 0.7, r'$k^*_{\mathrm{dep}}=30k^*_{\mathrm{ero}}$', color = 'w',
        transform=f_ratio.transAxes, rotation = 63)
f_ratio.text(0.27, 0.75, r'$k^*_{\mathrm{dep}}=20k^*_{\mathrm{ero}}$', color = 'w',
        transform=f_ratio.transAxes, rotation = 55)
f_ratio.text(0.75, 0.7, r'$k^*_{\mathrm{dep}}=10k^*_{\mathrm{ero}}$', color = 'w',
        transform=f_ratio.transAxes, rotation = 35)
f_ratio.text(0.78, 0.21, r'$k^*_{\mathrm{dep}}=5k^*_{\mathrm{ero}}$', color = 'w',
        transform=f_ratio.transAxes, rotation = 18)
f_ratio.text(0.8, 0.05, r'$k^*_{\mathrm{dep}}=3k^*_{\mathrm{ero}}$', color = 'w',
        transform=f_ratio.transAxes, rotation = 12)

################relative submergence subplot
vmin_r = min(df['rel_rx'])
vmax_r = max(df['rel_rx'])

arr = np.array(df['rel_rx']).reshape(n,n)



clevels = np.arange(0, 7.5, 0.5)
contsf = rel_rx.contourf(X, Y, arr, zorder = 0, vmin = vmin_r, vmax = vmax_r,
                     levels = clevels)
conts = rel_rx.contour(X, Y, arr, zorder = 2, vmin = vmin_r, vmax = vmax_r, 
                   colors = 'k', levels = clevels)
rel_rx.clabel(conts, fontsize = 12, zorder = 1)
#ax2 = ax.twinx()
x = np.arange(1,6)
rel_rx.plot(x, x * 30, color = 'w', linewidth = 2, zorder = 10, linestyle = lines) #kero/kdep = 1/30
rel_rx.plot(x, x * 20, color = 'w', linewidth = 2, zorder = 10, linestyle = lines) #kero/kdep = 1/20
rel_rx.plot(x, x * 10, color = 'w', linewidth = 2, zorder = 10, linestyle = lines) #kero/kdep = 1/10
rel_rx.plot(x, x * 5, color = 'w', linewidth = 2, zorder = 10, linestyle = lines) #kero/kdep = 1/5
rel_rx.plot(x, x * 3.33, color = 'w', linewidth = 2, zorder = 10, linestyle = lines) #kero/kdep = 1/3
rel_rx.set_xlim(1, 5)
rel_rx.set_ylim(10, 50)
#plt.tight_layout()
fig.colorbar(contsf, cax = cbar_ax)
cbar_ax.set_ylim(vmin_r, vmax_r)
cbar_ax.set_ylabel('Normalized width')
#ax.set_box_aspect(1) #set square but not with 'equal' because that relies on data coords

rel_rx.set_xlabel(r'$k^*_{\mathrm{ero}}$')
#rel_rx.set_ylabel(r'$k^*_{\mathrm{dep}}$')
rel_rx.get_yaxis().set_ticklabels([])
rel_rx.set_title('F) Relative submergence $R/z_0$ [-]')

#now find a way to annotate each line 
rel_rx.text(0.075, 0.7, r'$k^*_{\mathrm{dep}}=30k^*_{\mathrm{ero}}$', color = 'w',
        transform=rel_rx.transAxes, rotation = 63)
rel_rx.text(0.27, 0.75, r'$k^*_{\mathrm{dep}}=20k^*_{\mathrm{ero}}$', color = 'w',
        transform=rel_rx.transAxes, rotation = 55)
rel_rx.text(0.75, 0.7, r'$k^*_{\mathrm{dep}}=10k^*_{\mathrm{ero}}$', color = 'w',
        transform=rel_rx.transAxes, rotation = 35)
rel_rx.text(0.78, 0.21, r'$k^*_{\mathrm{dep}}=5k^*_{\mathrm{ero}}$', color = 'w',
        transform=rel_rx.transAxes, rotation = 18)
rel_rx.text(0.8, 0.05, r'$k^*_{\mathrm{dep}}=3k^*_{\mathrm{ero}}$', color = 'w',
        transform=rel_rx.transAxes, rotation = 12)

###########################################

fig.savefig('fig_sweep_k_' + run_name +'_hires.png', dpi = 1000)
fig.savefig('fig_sweep_k_' + run_name +'_lores.png', dpi = 200)
