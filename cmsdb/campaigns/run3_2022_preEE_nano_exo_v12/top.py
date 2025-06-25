# coding: utf-8                                                                                                                                
"""                                                                                                                                           top quark datasets for the 2022 pre-EE data-taking campaign (EXO nano)                                                                        """

from order import DatasetInfo

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_preEE_nano_exo_v12 import campaign_run3_2022_preEE_nano_exo_v12 as cpn

#                                                                                                                                             # ttbar                                                                                                                                       #                                                                                                                                             

cpn.add_dataset(
    name="tt_sl_powheg",
    id=14791322,
    processes=[procs.tt_sl],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8",
            ],
            n_files=327,
            n_events=20453850,
        ),
    ),
)

cpn.add_dataset(
    name="tt_dl_powheg",
    id=14803719,
    processes=[procs.tt_dl],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8",
            ],
            n_files=274,
            n_events=14181511,
        ),
    ),
)

cpn.add_dataset(
    name="tt_fh_powheg",
    id=14808372,
    processes=[procs.tt_fh],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTto4Q_TuneCP5_13p6TeV_powheg-pythia8",
            ],
            n_files=1117,
            n_events=48006739,
        ),
    ),
)
