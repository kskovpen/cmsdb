# coding: utf-8

"""
CMS datasets from the 2022 pre-EE data-taking campaign (EXO nano)
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_preEE_nano_exo_v12 import campaign_run3_2022_preEE_nano_exo_v12 as cpn


#
# Muon
#

# COSMICS - not good for Physics

cpn.add_dataset(
    name="data_singlemu_b",
    id=14784199,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "2022B/SingleMuon",
    ],
    n_files=56,
    n_events=4190940,
    aux={
        "era": "B",
    },
)

# PRE-EE

cpn.add_dataset(
    name="data_singlemu_c",
    id=14784105,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "2022C/SingleMuon",
    ],
    n_files=252,
    n_events=20162441, # should it stay the same (?!)
    aux={
        "era": "C",
        "jec_era": "RunCD",
    },
)

#
# E/Gamma
#

# COSMICS - not good for Physics

cpn.add_dataset(
    name="data_egamma_b",
    id=14784198,
    is_data=True,
    processes=[procs.data_egamma],
    keys=[
        "2022B/EGamma",
    ],
    n_files=121,
    n_events=10328232,
    aux={
        "era": "B",
    },
)

# PRE-EE

cpn.add_dataset(
    name="data_egamma_c",
    id=14784141,
    is_data=True,
    processes=[procs.data_egamma],
    keys=[
        "2022C/EGamma",
    ],
    n_files=3354,
    n_events=263689151, #? FIXME: i assume it should be the same as in "non-processed" dataset
    aux={
        "era": "C",
    },
)
