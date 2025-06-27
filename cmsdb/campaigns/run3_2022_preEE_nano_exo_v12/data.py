# coding: utf-8

"""
CMS datasets from the 2022 pre-EE data-taking campaign (EXO nano)
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_preEE_nano_exo_v12 import campaign_run3_2022_preEE_nano_exo_v12 as cpn


#
# Muon
#

cpn.add_dataset(
    name="data_singlemu_b",
    id=14784199,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/SingleMuon",
    ],
    n_files=56,
    n_events=4190940,
    aux={
        "era": "B",
    },
)


#
# E/Gamma
#

cpn.add_dataset(
    name="data_egamma_b",
    id=14784198,
    is_data=True,
    processes=[procs.data_egamma],
    keys=[
        "/EGamma",
    ],
    n_files=121,
    n_events=10328232,
    aux={
        "era": "B",
    },
)
