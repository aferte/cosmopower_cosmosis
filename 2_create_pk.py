import cosmosis
import numpy as np
import os 

#based on https://github.com/alessiospuriomancini/cosmopower/blob/main/cosmopower/training/spectra_generation_scripts/2_create_spectra.py
#but calling cosmosis

#set up CSL
csl_dir = os.environ['csl_dir']

#read parameters
input_params = np.load('lhs_cosmo.npz')

#call cosmosis for each of the input params
# block = cosmosis.DataBlock()
# block['cosmological_parameters','omega_m'] = input_params['omega_m']
# block['cosmological_parameters','A_s'] = input_params['A_s']

#run ini file
pipe        = cosmosis.LikelihoodPipeline('pipeline_pk.ini')
input_cosmo = []
pk          = []
pk_k        = []
pk_z        = []
pk_type     = 'matter_power_lin'
for om,a_s in zip(input_params['omega_m'],input_params['A_s']):
    temp_output = pipe.run_parameters([om,a_s])
    input_cosmo.append([om,a_s])
    pk.append(temp_output[pk_type,'p_k'])
    pk_k.append(temp_output[pk_type,'k_h'])
    pk_z.append(temp_output[pk_type,'z'])


np.save('input_cosmo',np.array(input_cosmo))
np.save('matter_pk',np.array(pk))
np.save('matter_pk_k',np.array(pk_k))
np.save('matter_pk_z',np.array(pk_z))

