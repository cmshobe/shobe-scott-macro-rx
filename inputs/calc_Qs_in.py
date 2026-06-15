#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 11:46:50 2026

@author: charlesshobe
"""

import numpy as np
import pandas as pd

#bring in Q data and trim to date bounds
Q_time_series = pd.read_parquet('inputs/sf_sno_Q.parquet')
Q_time_series_np = Q_time_series['Q (cms)'].to_numpy()

Q_time_series['Qs_in (m3/s)'] = 0.05 * 1.9e-6 * Q_time_series['Q (cms)'] ** 2

#do annual load calculations from time series:
years = [2019, 2020, 2021, 2022, 2023, 2024]
total_loads_m3_peryr = np.zeros(6)
iter = 0
for year in years:
    Qs_year_clip = Q_time_series[Q_time_series['datetime'].dt.year == year]
    Qs_integrated = Qs_year_clip['Qs_in (m3/s)'].sum() * 60 * 15
    total_loads_m3_peryr[iter] = Qs_integrated
    iter += 1
    
#now convert m3/yr to tons:
rock_density = 2650 #2650 kg/m3 rock density
kg_per_metric_ton = 1000 #1000 kg per metric ton
total_loads_tons = total_loads_m3_peryr * rock_density / kg_per_metric_ton
avg_load_tons = np.average(total_loads_tons)