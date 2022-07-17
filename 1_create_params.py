import numpy as np
import pyDOE as pyDOE

#based on https://github.com/alessiospuriomancini/cosmopower/blob/main/cosmopower/training/spectra_generation_scripts/1_create_params.py
n_params = 2
n_samples = 10

# parameter ranges
om      = np.linspace(0.1, 0.9, n_samples)
prim_as = np.linspace(0.5e-09, 5.0e-09, n_samples)

# LHS grid
AllParams = np.vstack([om,prim_as])
lhd = pyDOE.lhs(n_params, samples=n_samples, criterion=None)
idx = (lhd * n_samples).astype(int)


AllCombinations = np.zeros((n_samples, n_params))
for i in range(n_params):
    AllCombinations[:, i] = AllParams[i][idx[:, i]]

# saving
params = {'omega_m': AllCombinations[:, 0],
          'A_s': AllCombinations[:, 1]}
np.savez('lhs_cosmo.npz', **params)