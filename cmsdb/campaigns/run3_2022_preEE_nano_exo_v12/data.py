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
    name="data_mu_b",
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

# July 2026, produced from /SingleMuon/Run2022C-22Sep2023-v1/MINIAOD
# MuonC might have to be added as an extension (or better SingleMuon to Muon since it is smaller)
# dataset=/SingleMuon/Run2022C-22Sep2023-v1/MINIAOD
# dataset=/Muon/Run2022C-22Sep2023-v1/MINIAOD
cpn.add_dataset(
    name="data_mu_c",
    id=14784105,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "SingleMuon/SingleMuon_Run2022C_NanoAODv12_LRSM_260810/260810_105528/0000",
        "Muon/Muon_Run2022C_NanoAODv12_LRSM_260804/260804_163714/0000",
        "Muon/Muon_Run2022C_NanoAODv12_LRSM_260804/260804_163714/0001",
        "Muon/Muon_Run2022C_NanoAODv12_LRSM_260804/260804_163714/0002",
        "Muon/Muon_Run2022C_NanoAODv12_LRSM_260804/260804_163714/0003",
        "Muon/Muon_Run2022C_NanoAODv12_LRSM_260804/260804_163714/0004",
        "Muon/Muon_Run2022C_NanoAODv12_LRSM_260804/260804_163714/0005",
        "Muon/Muon_Run2022C_NanoAODv12_LRSM_260804/260804_163714/0006",
        "Muon/Muon_Run2022C_NanoAODv12_LRSM_260804/260804_163714/0007",
        "Muon/Muon_Run2022C_NanoAODv12_LRSM_260804/260804_163714/0008",
    ],
    n_files=14470,
    n_events=158492134, # 20162441 + 138329693
    aux={
        "era": "C",
        "jec_era": "RunCD",
    },
)

# FIXME 0.4% of files have not been run -- I assume 0.4% events missing
# dataset=/Muon/Run2022D-22Sep2023-v1/MINIAOD
cpn.add_dataset(
    name="data_mu_d",
    id=14784106,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "Muon/Muon_Run2022D_NanoAODv12_LRSM_260727/260804_073609/0000",
        "Muon/Muon_Run2022D_NanoAODv12_LRSM_260727/260804_073609/0001",
        "Muon/Muon_Run2022D_NanoAODv12_LRSM_260727/260804_073609/0002",
        "Muon/Muon_Run2022D_NanoAODv12_LRSM_260727/260804_073609/0003",
    ],
    n_files=3435, 
    n_events=75440027, # --account for the 0.4% missing Total: 75440027 -- i don't know how to manage this...
    aux={
        "era": "D",
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

# dataset=/EGamma/Run2022C-22Sep2023-v1/MINIAOD
cpn.add_dataset(
    name="data_egamma_c",
    id=14784141,
    is_data=True,
    processes=[procs.data_egamma],
    keys=[
        "EGamma/EGamma_Run2022C_NanoAODv12_LRSM_260804/260804_163703/0000",
        "EGamma/EGamma_Run2022C_NanoAODv12_LRSM_260804/260804_163703/0001",
        "EGamma/EGamma_Run2022C_NanoAODv12_LRSM_260804/260804_163703/0002",
        "EGamma/EGamma_Run2022C_NanoAODv12_LRSM_260804/260804_163703/0003",
        "EGamma/EGamma_Run2022C_NanoAODv12_LRSM_260804/260804_163703/0004",
        "EGamma/EGamma_Run2022C_NanoAODv12_LRSM_260804/260804_163703/0005",
        "EGamma/EGamma_Run2022C_NanoAODv12_LRSM_260804/260804_163703/0006",
        "EGamma/EGamma_Run2022C_NanoAODv12_LRSM_260804/260804_163703/0007",
        "EGamma/EGamma_Run2022C_NanoAODv12_LRSM_260804/260804_163703/0008",
        "EGamma/EGamma_Run2022C_NanoAODv12_LRSM_260804/260804_163703/0009",
    ],
    n_files=12817,
    n_events=263549470,
    aux={
        "era": "C",
        "jec_era": "RunCD",
    },
)

#dataset=/EGamma/Run2022D-22Sep2023-v1/MINIAOD
cpn.add_dataset(
    name="data_egamma_d",
    id=14784142,
    is_data=True,
    keys=[
        "EGamma/EGamma_Run2022D_NanoAODv12_LRSM_260727/260803_073326/0000",
        "EGamma/EGamma_Run2022D_NanoAODv12_LRSM_260727/260803_073326/0001",
        "EGamma/EGamma_Run2022D_NanoAODv12_LRSM_260727/260803_073326/0002",
        "EGamma/EGamma_Run2022D_NanoAODv12_LRSM_260727/260803_073326/0003",
        "EGamma/EGamma_Run2022D_NanoAODv12_LRSM_260727/260803_073326/0004",
        "EGamma/EGamma_Run2022D_NanoAODv12_LRSM_260727/260803_073326/0005",
    ],
    n_files=5468,
    n_events=89134996,
    aux={
        "era": "D",
        "jec_era": "RunCD",
    },
)