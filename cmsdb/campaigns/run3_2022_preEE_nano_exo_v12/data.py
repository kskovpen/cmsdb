# coding: utf-8

"""
CMS datasets from the 2022 pre-EE data-taking campaign (EXO nano)
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_preEE_nano_exo_v12 import campaign_run3_2022_preEE_nano_exo_v12 as cpn
from order import DatasetInfo

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
        "SingleMuon/SingleMuon_Run2022B_NanoAODv12_LRSM_260709/260709_102958/0000/",
    ],
    n_files=35,
    n_events=5328210,
    aux={
        "era": "B",
    },
)

# PRE-EE

# NOTE FIXME there is mu and there is singlemu in the other datasets, should both be consdiered? (?!)
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
        "EGamma/EGamma_Run2022B_NanoAODv12_LRSM_260709/260709_102949/0000/",
    ],
    n_files=62,
    n_events=11074301,
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
    info=dict(
        nominal=DatasetInfo(
            keys=[
               "EGamma/2022PreEE_C/nanoaod/",
            ],
            n_files=999,
            n_events=194402,
        ),
    ),
    n_files=1,
    n_events=10000, #? FIXME: i assume it should be the same as in "non-processed" dataset
    aux={
        "era": "C",
        "jec_era": "RunCD",
    },
)
