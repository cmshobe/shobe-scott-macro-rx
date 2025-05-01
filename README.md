# shobe-scott-macro-rx

Modeling and analysis code for Shobe and Scott (in prep): Modeling the influence of macro-roughness on gravel-bed river morphodynamics

This repository contains all code and input data required to reproduce the modeling and analysis in the above paper.

Note 1: The model produces much of its output in .npy binaries, which can exceed 400MB each. These files are not included in this repository, but they can be produced by running the model code in this repository.

Note 2: We plan to refactor the code in this repository into a Python package for greater clarity once the paper is accepted.

### Repository contents

1. figure_4/
	1. `sweep_z0_values.py` and `roughness_function.py`: `sweep_z0_values.py` is a driver script that runs the model (contained in `roughness_function.py`) across many different values of $z_0$. Outputs are an `.npy` binary of model results and a `.txt` file of parameters used.
	2. `make_figure_4.py`: creates Figure 4 in the paper; exports `.png` figure files.
2. figure_5/
	1. `sweep_bed_cover_values.py` and `roughness_function.py`: `sweep_bed_cover_values.py` is a driver script that runs the model (contained in `roughness_function.py`) across many different values of $w^\mathrm{bed}_\mathrm{roughness}$. Outputs are an `.npy` binary of model results and a `.txt` file of parameters used.
	2. `make_figure_5.py`: creates Figure 5 in the paper; exports `.png` figure files.
3. figure_6/
	1. `sweep_bank_cover_values.py` and `roughness_function.py`: `sweep_bank_cover_values.py` is a driver script that runs the model (contained in `roughness_function.py`) across many different values of $l^\mathrm{bank}_\mathrm{roughness}$. Outputs are an `.npy` binary of model results and a `.txt` file of parameters used.
	2. `make_figure_6.py` creates Figure 6 in the paper; exports `.png` figure files.
4. figure_7/
	1. `sweep_z0_values_floodplain.py` and `roughness_function.py`: `sweep_z0_values_floodplain.py` is a driver script that runs the model (contained in `roughness_function.py`) across many different values of $z_0$ with the potential for overbank flow. Outputs are an `.npy` binary of model results and a `.txt` file of parameters used.
	2. `make_figure_7.py` creates Figure 7 in the paper using the output from the no-floodplain case (`figure_4/sweep_z0_values.py`) and the floodplain case (`figure_7/sweep_z0_values_floodplain.py`); exports `.png` figure files.
5. figure_8_and_9/
	1. `run_trajectory_z0_XXX.py`, `run_trajectory_z0_XXX_floodplain.py`, and `roughness_trajectory_function.py`: Each `run_trajectory_z0_XXX.py` script runs the model (contained in `roughness_trajectory_function.py`) for a single value of $z_0$ with the potential for overbank flow turned off. Each `run_trajectory_z0_XXX_floodplain.py` script runs the model for a single value of $z_0$ with the potential for overbank flow turned on.
	2. `make_figure_8.py` and `make_figure_9.py` create Figures 8 and 9, respectively, in the paper using the output from each model run.
6. figure_10/ 
	1. `case_study_inversion_low_z0.py`, `case_study_inversion_high_z0.py`, and `case_study_inversion_function.py`: Each of the two inversion driver scripts runs the Differential Evolution model inversion procedure (contained in `case_study_inversion_function.py`) to find best-fit values for the two key parameters $k^*_{ero}$ and $k^*_{dep}$. Output from each is a `.csv` file recording the inversion results.
	2. `case_study_bestfit_run_low_z0.py`, `case_study_bestfit_run_high_z0.py`, and `case_study_function.py`: Each of the two driver scripts runs a single model realization using the best-fit $k^*_{ero}$ and $k^*_{dep}$ values from the respective inversion. Outputs are an `.npy` binary of model results and a `.txt` file of parameters used.
	3. `nf_sno_q.txt`: Discharge data from USGS gage \#12142000 near Snoqualmie Falls, WA, used to drive flow in the case study model simulations.
	4. `make_figure_10.py` creates Figure 10 in the paper using the output from both inversion records and both best-fit model simularions; exports `.png` figure files. 
