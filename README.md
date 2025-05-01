# shobe-scott-macro-rx

Modeling and analysis code for Shobe and Scott (in prep): Modeling the influence of macro-roughness on gravel-bed river morphodynamics

This repository contains all code and input data required to reproduce the modeling and analysis in the above paper.

Note: The model produces much of its output in .npy binaries, which can exceed 400MB each. These files are not included in this repository, but they can be produced by running the model code in this repository.

### Repository contents

1. figure_4
	1. `sweep_z0_values.py` and `roughness_function.py`: `sweep_z0_values.py` is a driver script that runs the model (contained in `roughness_function.py`) across many different values of $z_0$. Outpus are an `.npy` binary of model results and a `.txt` file of parameters used.
	2. `make_figure_4.py`: creates Figure 4 in the paper. 
