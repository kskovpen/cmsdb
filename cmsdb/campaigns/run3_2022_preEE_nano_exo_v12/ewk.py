# coding: utf-8

"""
Electroweak datasets for the 2022 pre-EE data-taking campaign (EXO nano)
"""

from order import DatasetInfo

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_preEE_nano_exo_v12 import campaign_run3_2022_preEE_nano_exo_v12 as cpn

cpn.add_dataset(
    name="w_lnu_4jets_madgraph",
    id=14803995,
    processes=[procs.w_lnu],
    keys=[
        "/WtoLNu-4Jets_TuneCP5_13p6TeV_madgraphMLM-pythia8",  # noqa
    ],
    n_files=1164,
    n_events=84739011,
)
