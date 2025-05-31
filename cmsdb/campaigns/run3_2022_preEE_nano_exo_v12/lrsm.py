# coding: utf-8

"""
LRSM datasets for the 2022 pre-EE data-taking campaign (EXO nano)
"""

from order import DatasetInfo

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_preEE_nano_exo_v12 import campaign_run3_2022_preEE_nano_exo_v12 as cpn

cpn.add_dataset(
    name="lrsm_wr4000n20_ee",
    id=4000201,
    processes=[procs.lrsm_wr4000n20],
    keys=[
        "/lrsm_wr4000n20_ee_nlo_ms",  # noqa
    ],
    n_files=22,
    n_events=22000,
)

cpn.add_dataset(
    name="lrsm_wr4000n20_em",
    id=4000202,
    processes=[procs.lrsm_wr4000n20],
    keys=[
        "/lrsm_wr4000n20_em_nlo_ms",  # noqa
    ],
    n_files=25,
    n_events=25000,
)

cpn.add_dataset(
    name="lrsm_wr4000n20_me",
    id=4000203,
    processes=[procs.lrsm_wr4000n20],
    keys=[
        "/lrsm_wr4000n20_me_nlo_ms",  # noqa
    ],
    n_files=18,
    n_events=18000,
)

cpn.add_dataset(
    name="lrsm_wr4000n20_mm",
    id=4000204,
    processes=[procs.lrsm_wr4000n20],
    keys=[
        "/lrsm_wr4000n20_mm_nlo_ms",  # noqa
    ],
    n_files=23,
    n_events=23000,
)
