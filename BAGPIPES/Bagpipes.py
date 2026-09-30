# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.5
#   kernelspec:
#     display_name: base
#     language: python
#     name: python3
# ---

# %%

# %%


import bagpipes as pipes
import numpy as np
import matplotlib.pyplot
from bagpipes import model_galaxy 


# %%


model_components = {}
model_components["redshift"] = 0 # Observed redshift (mandatory)
model_components["veldisp"] = 300 # Max age of birth clouds: Gyr
model_components["t_bc"] = 0.01


# Dict containing SFH info
dblplaw = {}
dblplaw["tau"] = 12
dblplaw["alpha"] = 30
dblplaw["beta"] = 0.5
dblplaw["metallicity"] = 0.8
dblplaw["massformed"] = 11
model_components["dblplaw"] = dblplaw

dust = {}
dust["type"] = "Calzetti" #attenuation law
dust["Av"] = 0.2
dust["eta"] = 3
model_components["dust"] = dust

nebular = {}
nebular["logU"] = -3
model_components["nebular"] = nebular


# %%


model_galaxy(model_components, filt_list=None, spec_wavs=None, spec_units='ergscma', phot_units='ergscma', index_list=None)

