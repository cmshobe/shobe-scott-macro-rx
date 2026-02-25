# shobe-scott-macro-rx

Modeling and analysis code for Shobe and Scott (in review): Modeling the influence of macro-roughness on gravel-bed river morphodynamics

This repository contains all code and input data required to reproduce the modeling and analysis in the above paper.

Note 1: The model produces much of its output in .npy binaries, which can be hundreds of MB each. These files are not included in this repository, but they can be produced by running the code in this repository.

### Repository contents
- `figures/`
	- scripts to reproduce all results figures in the paper. To reproduce any result, first run the relevant model driver(s), which will create the model output used by the figure plotting script.
- `inputs/`
	- `sf_sno_q.parquet`: Discharge data from USGS gage \#12144000 used to drive flow in the case study model simulations.
- `results/`
	- folder to hold output from driver scripts.
- `macro_roughness_functions.py`: all model functions; these are called by all driver scripts.
- `sweep_z0_values.py`: driver script that runs the model across many values of $z_0$. Outputs are an `.npy` binary of model results and a `.txt` file of parameters used.
- `sweep_bed_cover_values.py`: driver script that runs the model across many values of $w^\mathrm{bed}_\mathrm{roughness}$. Outputs are an `.npy` binary of model results and a `.txt` file of parameters used.
- `sweep_bank_cover_values.py`: driver script that runs the model across many values of $l^\mathrm{bank}_\mathrm{roughness}$. Outputs are an `.npy` binary of model results and a `.txt` file of parameters used.
- `sweep_k_values.py`: driver script that runs the model across many values of $k^*_\mathrm{ero}$ and $k^*_\mathrm{dep}$. Outputs are an `.npy` binary of model results and a `.txt` file of parameters used.
- `run_trajectory.py`: driver script that runs a single model realization and tracks morphologic evolution through time. 
- `case_study_inversion.py`: driver script that runs the Differential Evolution inversion procedure to find best-fit values for the two key parameters $k^*_\mathrm{ero}$ and $k^*_\mathrm{dep}$. Output from each is a `.csv` file recording the inversion results.
- `case_study_bestfit_run.py`: driver script that runs a single model realization using the best-fit $k^*_\mathrm{ero}$ and $k^*_\mathrm{dep}$ values from the inversion. Outputs are an `.npy` binary of model results and a `.txt` file of parameters used.
