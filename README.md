# shobe-scott-macro-rx

Modeling and analysis code for Shobe and Scott (in prep): Modeling the influence of macro-roughness on gravel-bed river morphodynamics

This repository contains all code and input data required to reproduce the modeling and analysis in the above paper.

Note: The model produces much of its output in .npy binaries, which can exceed 400MB each. These files are not included in this repository, but they can be produced by running the model code in this repository.

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
5. figure_8_and_9/
6. figure_10/ 
