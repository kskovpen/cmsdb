# coding: utf-8

"""
LRSM datasets for the 2022 pre-EE data-taking campaign (EXO nano)
"""

from order import DatasetInfo

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_preEE_nano_exo_v12 import campaign_run3_2022_preEE_nano_exo_v12 as cpn

# WR(4000)

cpn.add_dataset(name="lrsm_wr4000n10_ee", id=4000101, processes=[procs.lrsm_wr4000n10_ee], keys=["/lrsm_wr4000n10_ee_nlo_ms",], n_files=22, n_events=22000,)
cpn.add_dataset(name="lrsm_wr4000n10_em", id=4000102, processes=[procs.lrsm_wr4000n10_em], keys=["/lrsm_wr4000n10_em_nlo_ms",], n_files=24, n_events=24000,)
cpn.add_dataset(name="lrsm_wr4000n10_me", id=4000103, processes=[procs.lrsm_wr4000n10_me], keys=["/lrsm_wr4000n10_me_nlo_ms",], n_files=23, n_events=23000,)
cpn.add_dataset(name="lrsm_wr4000n10_mm", id=4000104, processes=[procs.lrsm_wr4000n10_mm], keys=["/lrsm_wr4000n10_mm_nlo_ms",], n_files=23, n_events=23000,)

cpn.add_dataset(name="lrsm_wr4000n20_ee", id=4000201, processes=[procs.lrsm_wr4000n20_ee], keys=["/lrsm_wr4000n20_ee_nlo_ms",], n_files=24, n_events=24000,)
cpn.add_dataset(name="lrsm_wr4000n20_em", id=4000202, processes=[procs.lrsm_wr4000n20_em], keys=["/lrsm_wr4000n20_em_nlo_ms",], n_files=25, n_events=25000,)
cpn.add_dataset(name="lrsm_wr4000n20_me", id=4000203, processes=[procs.lrsm_wr4000n20_me], keys=["/lrsm_wr4000n20_me_nlo_ms",], n_files=18, n_events=18000,)
cpn.add_dataset(name="lrsm_wr4000n20_mm", id=4000204, processes=[procs.lrsm_wr4000n20_mm], keys=["/lrsm_wr4000n20_mm_nlo_ms",], n_files=23, n_events=23000,)

cpn.add_dataset(name="lrsm_wr4000n30_ee", id=4000301, processes=[procs.lrsm_wr4000n30_ee], keys=["/lrsm_wr4000n30_ee_nlo_ms",], n_files=23, n_events=23000,)
cpn.add_dataset(name="lrsm_wr4000n30_em", id=4000302, processes=[procs.lrsm_wr4000n30_em], keys=["/lrsm_wr4000n30_em_nlo_ms",], n_files=24, n_events=24000,)
cpn.add_dataset(name="lrsm_wr4000n30_me", id=4000303, processes=[procs.lrsm_wr4000n30_me], keys=["/lrsm_wr4000n30_me_nlo_ms",], n_files=23, n_events=23000,)
cpn.add_dataset(name="lrsm_wr4000n30_mm", id=4000304, processes=[procs.lrsm_wr4000n30_mm], keys=["/lrsm_wr4000n30_mm_nlo_ms",], n_files=23, n_events=23000,)

cpn.add_dataset(name="lrsm_wr4000n40_ee", id=4000401, processes=[procs.lrsm_wr4000n40_ee], keys=["/lrsm_wr4000n40_ee_nlo_ms",], n_files=23, n_events=23000,)
cpn.add_dataset(name="lrsm_wr4000n40_em", id=4000402, processes=[procs.lrsm_wr4000n40_em], keys=["/lrsm_wr4000n40_em_nlo_ms",], n_files=25, n_events=25000,)
cpn.add_dataset(name="lrsm_wr4000n40_me", id=4000403, processes=[procs.lrsm_wr4000n40_me], keys=["/lrsm_wr4000n40_me_nlo_ms",], n_files=23, n_events=23000,)
cpn.add_dataset(name="lrsm_wr4000n40_mm", id=4000404, processes=[procs.lrsm_wr4000n40_mm], keys=["/lrsm_wr4000n40_mm_nlo_ms",], n_files=23, n_events=23000,)

cpn.add_dataset(name="lrsm_wr4000n50_ee", id=4000501, processes=[procs.lrsm_wr4000n50_ee], keys=["/lrsm_wr4000n50_ee_nlo_ms",], n_files=22, n_events=22000,)
cpn.add_dataset(name="lrsm_wr4000n50_em", id=4000502, processes=[procs.lrsm_wr4000n50_em], keys=["/lrsm_wr4000n50_em_nlo_ms",], n_files=23, n_events=23000,)
cpn.add_dataset(name="lrsm_wr4000n50_me", id=4000503, processes=[procs.lrsm_wr4000n50_me], keys=["/lrsm_wr4000n50_me_nlo_ms",], n_files=21, n_events=21000,)
cpn.add_dataset(name="lrsm_wr4000n50_mm", id=4000504, processes=[procs.lrsm_wr4000n50_mm], keys=["/lrsm_wr4000n50_mm_nlo_ms",], n_files=23, n_events=23000,)

cpn.add_dataset(name="lrsm_wr4000n60_ee", id=4000601, processes=[procs.lrsm_wr4000n60_ee], keys=["/lrsm_wr4000n60_ee_nlo_ms",], n_files=24, n_events=24000,)
cpn.add_dataset(name="lrsm_wr4000n60_em", id=4000602, processes=[procs.lrsm_wr4000n60_em], keys=["/lrsm_wr4000n60_em_nlo_ms",], n_files=23, n_events=23000,)
cpn.add_dataset(name="lrsm_wr4000n60_me", id=4000603, processes=[procs.lrsm_wr4000n60_me], keys=["/lrsm_wr4000n60_me_nlo_ms",], n_files=23, n_events=23000,)
cpn.add_dataset(name="lrsm_wr4000n60_mm", id=4000604, processes=[procs.lrsm_wr4000n60_mm], keys=["/lrsm_wr4000n60_mm_nlo_ms",], n_files=24, n_events=24000,)

cpn.add_dataset(name="lrsm_wr4000n70_ee", id=4000701, processes=[procs.lrsm_wr4000n70_ee], keys=["/lrsm_wr4000n70_ee_nlo_ms",], n_files=24, n_events=24000,)
cpn.add_dataset(name="lrsm_wr4000n70_em", id=4000702, processes=[procs.lrsm_wr4000n70_em], keys=["/lrsm_wr4000n70_em_nlo_ms",], n_files=22, n_events=22000,)
cpn.add_dataset(name="lrsm_wr4000n70_me", id=4000703, processes=[procs.lrsm_wr4000n70_me], keys=["/lrsm_wr4000n70_me_nlo_ms",], n_files=23, n_events=23000,)
cpn.add_dataset(name="lrsm_wr4000n70_mm", id=4000704, processes=[procs.lrsm_wr4000n70_mm], keys=["/lrsm_wr4000n70_mm_nlo_ms",], n_files=25, n_events=25000,)

cpn.add_dataset(name="lrsm_wr4000n80_ee", id=4000801, processes=[procs.lrsm_wr4000n80_ee], keys=["/lrsm_wr4000n80_ee_nlo_ms",], n_files=24, n_events=24000,)
cpn.add_dataset(name="lrsm_wr4000n80_em", id=4000802, processes=[procs.lrsm_wr4000n80_em], keys=["/lrsm_wr4000n80_em_nlo_ms",], n_files=22, n_events=22000,)
cpn.add_dataset(name="lrsm_wr4000n80_me", id=4000803, processes=[procs.lrsm_wr4000n80_me], keys=["/lrsm_wr4000n80_me_nlo_ms",], n_files=23, n_events=23000,)
cpn.add_dataset(name="lrsm_wr4000n80_mm", id=4000804, processes=[procs.lrsm_wr4000n80_mm], keys=["/lrsm_wr4000n80_mm_nlo_ms",], n_files=24, n_events=24000,)

cpn.add_dataset(name="lrsm_wr4000n90_ee", id=4000901, processes=[procs.lrsm_wr4000n90_ee], keys=["/lrsm_wr4000n90_ee_nlo_ms",], n_files=24, n_events=24000,)
cpn.add_dataset(name="lrsm_wr4000n90_em", id=4000902, processes=[procs.lrsm_wr4000n90_em], keys=["/lrsm_wr4000n90_em_nlo_ms",], n_files=23, n_events=23000,)
cpn.add_dataset(name="lrsm_wr4000n90_me", id=4000903, processes=[procs.lrsm_wr4000n90_me], keys=["/lrsm_wr4000n90_me_nlo_ms",], n_files=22, n_events=22000,)
cpn.add_dataset(name="lrsm_wr4000n90_mm", id=4000904, processes=[procs.lrsm_wr4000n90_mm], keys=["/lrsm_wr4000n90_mm_nlo_ms",], n_files=23, n_events=23000,)

cpn.add_dataset(name="lrsm_wr4000n100_ee", id=40001001, processes=[procs.lrsm_wr4000n100_ee], keys=["/lrsm_wr4000n100_ee_nlo_ms",], n_files=24, n_events=24000,)
cpn.add_dataset(name="lrsm_wr4000n100_em", id=40001002, processes=[procs.lrsm_wr4000n100_em], keys=["/lrsm_wr4000n100_em_nlo_ms",], n_files=0, n_events=0,)
cpn.add_dataset(name="lrsm_wr4000n100_me", id=40001003, processes=[procs.lrsm_wr4000n100_me], keys=["/lrsm_wr4000n100_me_nlo_ms",], n_files=23, n_events=23000,)
cpn.add_dataset(name="lrsm_wr4000n100_mm", id=40001004, processes=[procs.lrsm_wr4000n100_mm], keys=["/lrsm_wr4000n100_mm_nlo_ms",], n_files=24, n_events=24000,)

# WR(5000)

cpn.add_dataset(name="lrsm_wr5000n10_ee", id=5000101, processes=[procs.lrsm_wr5000n10_ee], keys=["/lrsm_wr5000n10_ee_nlo_ms",], n_files=22, n_events=22000,)
cpn.add_dataset(name="lrsm_wr5000n10_em", id=5000102, processes=[procs.lrsm_wr5000n10_em], keys=["/lrsm_wr5000n10_em_nlo_ms",], n_files=24, n_events=24000,)
cpn.add_dataset(name="lrsm_wr5000n10_me", id=5000103, processes=[procs.lrsm_wr5000n10_me], keys=["/lrsm_wr5000n10_me_nlo_ms",], n_files=21, n_events=21000,)
cpn.add_dataset(name="lrsm_wr5000n10_mm", id=5000104, processes=[procs.lrsm_wr5000n10_mm], keys=["/lrsm_wr5000n10_mm_nlo_ms",], n_files=23, n_events=23000,)

cpn.add_dataset(name="lrsm_wr5000n20_ee", id=5000201, processes=[procs.lrsm_wr5000n20_ee], keys=["/lrsm_wr5000n20_ee_nlo_ms",], n_files=25, n_events=25000,)
cpn.add_dataset(name="lrsm_wr5000n20_em", id=5000202, processes=[procs.lrsm_wr5000n20_em], keys=["/lrsm_wr5000n20_em_nlo_ms",], n_files=25, n_events=25000,)
cpn.add_dataset(name="lrsm_wr5000n20_me", id=5000203, processes=[procs.lrsm_wr5000n20_me], keys=["/lrsm_wr5000n20_me_nlo_ms",], n_files=25, n_events=25000,)
cpn.add_dataset(name="lrsm_wr5000n20_mm", id=5000204, processes=[procs.lrsm_wr5000n20_mm], keys=["/lrsm_wr5000n20_mm_nlo_ms",], n_files=24, n_events=24000,)

cpn.add_dataset(name="lrsm_wr5000n30_ee", id=5000301, processes=[procs.lrsm_wr5000n30_ee], keys=["/lrsm_wr5000n30_ee_nlo_ms",], n_files=25, n_events=25000,)
cpn.add_dataset(name="lrsm_wr5000n30_em", id=5000302, processes=[procs.lrsm_wr5000n30_em], keys=["/lrsm_wr5000n30_em_nlo_ms",], n_files=25, n_events=25000,)
cpn.add_dataset(name="lrsm_wr5000n30_me", id=5000303, processes=[procs.lrsm_wr5000n30_me], keys=["/lrsm_wr5000n30_me_nlo_ms",], n_files=25, n_events=25000,)
cpn.add_dataset(name="lrsm_wr5000n30_mm", id=5000304, processes=[procs.lrsm_wr5000n30_mm], keys=["/lrsm_wr5000n30_mm_nlo_ms",], n_files=24, n_events=24000,)

cpn.add_dataset(name="lrsm_wr5000n40_ee", id=5000401, processes=[procs.lrsm_wr5000n40_ee], keys=["/lrsm_wr5000n40_ee_nlo_ms",], n_files=25, n_events=25000,)
cpn.add_dataset(name="lrsm_wr5000n40_em", id=5000402, processes=[procs.lrsm_wr5000n40_em], keys=["/lrsm_wr5000n40_em_nlo_ms",], n_files=25, n_events=25000,)
cpn.add_dataset(name="lrsm_wr5000n40_me", id=5000403, processes=[procs.lrsm_wr5000n40_me], keys=["/lrsm_wr5000n40_me_nlo_ms",], n_files=25, n_events=25000,)
cpn.add_dataset(name="lrsm_wr5000n40_mm", id=5000404, processes=[procs.lrsm_wr5000n40_mm], keys=["/lrsm_wr5000n40_mm_nlo_ms",], n_files=25, n_events=25000,)

cpn.add_dataset(name="lrsm_wr5000n50_ee", id=5000501, processes=[procs.lrsm_wr5000n50_ee], keys=["/lrsm_wr5000n50_ee_nlo_ms",], n_files=25, n_events=25000,)
cpn.add_dataset(name="lrsm_wr5000n50_em", id=5000502, processes=[procs.lrsm_wr5000n50_em], keys=["/lrsm_wr5000n50_em_nlo_ms",], n_files=24, n_events=24000,)
cpn.add_dataset(name="lrsm_wr5000n50_me", id=5000503, processes=[procs.lrsm_wr5000n50_me], keys=["/lrsm_wr5000n50_me_nlo_ms",], n_files=25, n_events=25000,)
cpn.add_dataset(name="lrsm_wr5000n50_mm", id=5000504, processes=[procs.lrsm_wr5000n50_mm], keys=["/lrsm_wr5000n50_mm_nlo_ms",], n_files=23, n_events=23000,)

cpn.add_dataset(name="lrsm_wr5000n60_ee", id=5000601, processes=[procs.lrsm_wr5000n60_ee], keys=["/lrsm_wr5000n60_ee_nlo_ms",], n_files=25, n_events=25000,)
cpn.add_dataset(name="lrsm_wr5000n60_em", id=5000602, processes=[procs.lrsm_wr5000n60_em], keys=["/lrsm_wr5000n60_em_nlo_ms",], n_files=24, n_events=24000,)
cpn.add_dataset(name="lrsm_wr5000n60_me", id=5000603, processes=[procs.lrsm_wr5000n60_me], keys=["/lrsm_wr5000n60_me_nlo_ms",], n_files=25, n_events=25000,)
cpn.add_dataset(name="lrsm_wr5000n60_mm", id=5000604, processes=[procs.lrsm_wr5000n60_mm], keys=["/lrsm_wr5000n60_mm_nlo_ms",], n_files=25, n_events=25000,)

cpn.add_dataset(name="lrsm_wr5000n70_ee", id=5000701, processes=[procs.lrsm_wr5000n70_ee], keys=["/lrsm_wr5000n70_ee_nlo_ms",], n_files=25, n_events=25000,)
cpn.add_dataset(name="lrsm_wr5000n70_em", id=5000702, processes=[procs.lrsm_wr5000n70_em], keys=["/lrsm_wr5000n70_em_nlo_ms",], n_files=25, n_events=25000,)
cpn.add_dataset(name="lrsm_wr5000n70_me", id=5000703, processes=[procs.lrsm_wr5000n70_me], keys=["/lrsm_wr5000n70_me_nlo_ms",], n_files=25, n_events=25000,)
cpn.add_dataset(name="lrsm_wr5000n70_mm", id=5000704, processes=[procs.lrsm_wr5000n70_mm], keys=["/lrsm_wr5000n70_mm_nlo_ms",], n_files=25, n_events=25000,)

cpn.add_dataset(name="lrsm_wr5000n80_ee", id=5000801, processes=[procs.lrsm_wr5000n80_ee], keys=["/lrsm_wr5000n80_ee_nlo_ms",], n_files=25, n_events=25000,)
cpn.add_dataset(name="lrsm_wr5000n80_em", id=5000802, processes=[procs.lrsm_wr5000n80_em], keys=["/lrsm_wr5000n80_em_nlo_ms",], n_files=25, n_events=25000,)
cpn.add_dataset(name="lrsm_wr5000n80_me", id=5000803, processes=[procs.lrsm_wr5000n80_me], keys=["/lrsm_wr5000n80_me_nlo_ms",], n_files=25, n_events=25000,)
cpn.add_dataset(name="lrsm_wr5000n80_mm", id=5000804, processes=[procs.lrsm_wr5000n80_mm], keys=["/lrsm_wr5000n80_mm_nlo_ms",], n_files=25, n_events=25000,)

cpn.add_dataset(name="lrsm_wr5000n90_ee", id=5000901, processes=[procs.lrsm_wr5000n90_ee], keys=["/lrsm_wr5000n90_ee_nlo_ms",], n_files=25, n_events=25000,)
cpn.add_dataset(name="lrsm_wr5000n90_em", id=5000902, processes=[procs.lrsm_wr5000n90_em], keys=["/lrsm_wr5000n90_em_nlo_ms",], n_files=25, n_events=25000,)
cpn.add_dataset(name="lrsm_wr5000n90_me", id=5000903, processes=[procs.lrsm_wr5000n90_me], keys=["/lrsm_wr5000n90_me_nlo_ms",], n_files=25, n_events=25000,)
cpn.add_dataset(name="lrsm_wr5000n90_mm", id=5000904, processes=[procs.lrsm_wr5000n90_mm], keys=["/lrsm_wr5000n90_mm_nlo_ms",], n_files=25, n_events=25000,)

cpn.add_dataset(name="lrsm_wr5000n100_ee", id=50001001, processes=[procs.lrsm_wr5000n100_ee], keys=["/lrsm_wr5000n100_ee_nlo_ms",], n_files=25, n_events=25000,)
cpn.add_dataset(name="lrsm_wr5000n100_em", id=50001002, processes=[procs.lrsm_wr5000n100_em], keys=["/lrsm_wr5000n100_em_nlo_ms",], n_files=25, n_events=25000,)
cpn.add_dataset(name="lrsm_wr5000n100_me", id=50001003, processes=[procs.lrsm_wr5000n100_me], keys=["/lrsm_wr5000n100_me_nlo_ms",], n_files=24, n_events=24000,)
cpn.add_dataset(name="lrsm_wr5000n100_mm", id=50001004, processes=[procs.lrsm_wr5000n100_mm], keys=["/lrsm_wr5000n100_mm_nlo_ms",], n_files=25, n_events=25000,)

# WR(6000)

cpn.add_dataset(name="lrsm_wr6000n10_ee", id=6000101, processes=[procs.lrsm_wr6000n10_ee], keys=["/lrsm_wr6000n10_ee_nlo_ms",], n_files=25, n_events=25000,)
cpn.add_dataset(name="lrsm_wr6000n10_em", id=6000102, processes=[procs.lrsm_wr6000n10_em], keys=["/lrsm_wr6000n10_em_nlo_ms",], n_files=24, n_events=24000,)
cpn.add_dataset(name="lrsm_wr6000n10_me", id=6000103, processes=[procs.lrsm_wr6000n10_me], keys=["/lrsm_wr6000n10_me_nlo_ms",], n_files=25, n_events=25000,)
cpn.add_dataset(name="lrsm_wr6000n10_mm", id=6000104, processes=[procs.lrsm_wr6000n10_mm], keys=["/lrsm_wr6000n10_mm_nlo_ms",], n_files=25, n_events=25000,)

cpn.add_dataset(name="lrsm_wr6000n20_ee", id=6000201, processes=[procs.lrsm_wr6000n20_ee], keys=["/lrsm_wr6000n20_ee_nlo_ms",], n_files=25, n_events=25000,)
cpn.add_dataset(name="lrsm_wr6000n20_em", id=6000202, processes=[procs.lrsm_wr6000n20_em], keys=["/lrsm_wr6000n20_em_nlo_ms",], n_files=24, n_events=24000,)
cpn.add_dataset(name="lrsm_wr6000n20_me", id=6000203, processes=[procs.lrsm_wr6000n20_me], keys=["/lrsm_wr6000n20_me_nlo_ms",], n_files=24, n_events=24000,)
cpn.add_dataset(name="lrsm_wr6000n20_mm", id=6000204, processes=[procs.lrsm_wr6000n20_mm], keys=["/lrsm_wr6000n20_mm_nlo_ms",], n_files=24, n_events=24000,)

cpn.add_dataset(name="lrsm_wr6000n30_ee", id=6000301, processes=[procs.lrsm_wr6000n30_ee], keys=["/lrsm_wr6000n30_ee_nlo_ms",], n_files=25, n_events=25000,)
cpn.add_dataset(name="lrsm_wr6000n30_em", id=6000302, processes=[procs.lrsm_wr6000n30_em], keys=["/lrsm_wr6000n30_em_nlo_ms",], n_files=24, n_events=24000,)
cpn.add_dataset(name="lrsm_wr6000n30_me", id=6000303, processes=[procs.lrsm_wr6000n30_me], keys=["/lrsm_wr6000n30_me_nlo_ms",], n_files=25, n_events=25000,)
cpn.add_dataset(name="lrsm_wr6000n30_mm", id=6000304, processes=[procs.lrsm_wr6000n30_mm], keys=["/lrsm_wr6000n30_mm_nlo_ms",], n_files=25, n_events=25000,)

cpn.add_dataset(name="lrsm_wr6000n40_ee", id=6000401, processes=[procs.lrsm_wr6000n40_ee], keys=["/lrsm_wr6000n40_ee_nlo_ms",], n_files=24, n_events=24000,)
cpn.add_dataset(name="lrsm_wr6000n40_em", id=6000402, processes=[procs.lrsm_wr6000n40_em], keys=["/lrsm_wr6000n40_em_nlo_ms",], n_files=25, n_events=25000,)
cpn.add_dataset(name="lrsm_wr6000n40_me", id=6000403, processes=[procs.lrsm_wr6000n40_me], keys=["/lrsm_wr6000n40_me_nlo_ms",], n_files=25, n_events=25000,)
cpn.add_dataset(name="lrsm_wr6000n40_mm", id=6000404, processes=[procs.lrsm_wr6000n40_mm], keys=["/lrsm_wr6000n40_mm_nlo_ms",], n_files=25, n_events=25000,)

cpn.add_dataset(name="lrsm_wr6000n50_ee", id=6000501, processes=[procs.lrsm_wr6000n50_ee], keys=["/lrsm_wr6000n50_ee_nlo_ms",], n_files=25, n_events=25000,)
cpn.add_dataset(name="lrsm_wr6000n50_em", id=6000502, processes=[procs.lrsm_wr6000n50_em], keys=["/lrsm_wr6000n50_em_nlo_ms",], n_files=24, n_events=24000,)
cpn.add_dataset(name="lrsm_wr6000n50_me", id=6000503, processes=[procs.lrsm_wr6000n50_me], keys=["/lrsm_wr6000n50_me_nlo_ms",], n_files=25, n_events=25000,)
cpn.add_dataset(name="lrsm_wr6000n50_mm", id=6000504, processes=[procs.lrsm_wr6000n50_mm], keys=["/lrsm_wr6000n50_mm_nlo_ms",], n_files=24, n_events=24000,)

cpn.add_dataset(name="lrsm_wr6000n60_ee", id=6000601, processes=[procs.lrsm_wr6000n60_ee], keys=["/lrsm_wr6000n60_ee_nlo_ms",], n_files=25, n_events=25000,)
cpn.add_dataset(name="lrsm_wr6000n60_em", id=6000602, processes=[procs.lrsm_wr6000n60_em], keys=["/lrsm_wr6000n60_em_nlo_ms",], n_files=25, n_events=25000,)
cpn.add_dataset(name="lrsm_wr6000n60_me", id=6000603, processes=[procs.lrsm_wr6000n60_me], keys=["/lrsm_wr6000n60_me_nlo_ms",], n_files=25, n_events=25000,)
cpn.add_dataset(name="lrsm_wr6000n60_mm", id=6000604, processes=[procs.lrsm_wr6000n60_mm], keys=["/lrsm_wr6000n60_mm_nlo_ms",], n_files=24, n_events=24000,)

cpn.add_dataset(name="lrsm_wr6000n70_ee", id=6000701, processes=[procs.lrsm_wr6000n70_ee], keys=["/lrsm_wr6000n70_ee_nlo_ms",], n_files=25, n_events=25000,)
cpn.add_dataset(name="lrsm_wr6000n70_em", id=6000702, processes=[procs.lrsm_wr6000n70_em], keys=["/lrsm_wr6000n70_em_nlo_ms",], n_files=25, n_events=25000,)
cpn.add_dataset(name="lrsm_wr6000n70_me", id=6000703, processes=[procs.lrsm_wr6000n70_me], keys=["/lrsm_wr6000n70_me_nlo_ms",], n_files=25, n_events=25000,)
cpn.add_dataset(name="lrsm_wr6000n70_mm", id=6000704, processes=[procs.lrsm_wr6000n70_mm], keys=["/lrsm_wr6000n70_mm_nlo_ms",], n_files=25, n_events=25000,)

cpn.add_dataset(name="lrsm_wr6000n80_ee", id=6000801, processes=[procs.lrsm_wr6000n80_ee], keys=["/lrsm_wr6000n80_ee_nlo_ms",], n_files=25, n_events=25000,)
cpn.add_dataset(name="lrsm_wr6000n80_em", id=6000802, processes=[procs.lrsm_wr6000n80_em], keys=["/lrsm_wr6000n80_em_nlo_ms",], n_files=24, n_events=24000,)
cpn.add_dataset(name="lrsm_wr6000n80_me", id=6000803, processes=[procs.lrsm_wr6000n80_me], keys=["/lrsm_wr6000n80_me_nlo_ms",], n_files=25, n_events=25000,)
cpn.add_dataset(name="lrsm_wr6000n80_mm", id=6000804, processes=[procs.lrsm_wr6000n80_mm], keys=["/lrsm_wr6000n80_mm_nlo_ms",], n_files=24, n_events=24000,)

cpn.add_dataset(name="lrsm_wr6000n90_ee", id=6000901, processes=[procs.lrsm_wr6000n90_ee], keys=["/lrsm_wr6000n90_ee_nlo_ms",], n_files=25, n_events=25000,)
cpn.add_dataset(name="lrsm_wr6000n90_em", id=6000902, processes=[procs.lrsm_wr6000n90_em], keys=["/lrsm_wr6000n90_em_nlo_ms",], n_files=25, n_events=25000,)
cpn.add_dataset(name="lrsm_wr6000n90_me", id=6000903, processes=[procs.lrsm_wr6000n90_me], keys=["/lrsm_wr6000n90_me_nlo_ms",], n_files=25, n_events=25000,)
cpn.add_dataset(name="lrsm_wr6000n90_mm", id=6000904, processes=[procs.lrsm_wr6000n90_mm], keys=["/lrsm_wr6000n90_mm_nlo_ms",], n_files=25, n_events=25000,)

cpn.add_dataset(name="lrsm_wr6000n100_ee", id=60001001, processes=[procs.lrsm_wr6000n100_ee], keys=["/lrsm_wr6000n100_ee_nlo_ms",], n_files=25, n_events=25000,)
cpn.add_dataset(name="lrsm_wr6000n100_em", id=60001002, processes=[procs.lrsm_wr6000n100_em], keys=["/lrsm_wr6000n100_em_nlo_ms",], n_files=25, n_events=25000,)
cpn.add_dataset(name="lrsm_wr6000n100_me", id=60001003, processes=[procs.lrsm_wr6000n100_me], keys=["/lrsm_wr6000n100_me_nlo_ms",], n_files=25, n_events=25000,)
cpn.add_dataset(name="lrsm_wr6000n100_mm", id=60001004, processes=[procs.lrsm_wr6000n100_mm], keys=["/lrsm_wr6000n100_mm_nlo_ms",], n_files=25, n_events=25000,)

# WR(7000)

cpn.add_dataset(name="lrsm_wr7000n10_ee", id=7000101, processes=[procs.lrsm_wr7000n10_ee], keys=["/lrsm_wr7000n10_ee_nlo_ms",], n_files=24, n_events=24000,)
cpn.add_dataset(name="lrsm_wr7000n10_em", id=7000102, processes=[procs.lrsm_wr7000n10_em], keys=["/lrsm_wr7000n10_em_nlo_ms",], n_files=25, n_events=25000,)
cpn.add_dataset(name="lrsm_wr7000n10_me", id=7000103, processes=[procs.lrsm_wr7000n10_me], keys=["/lrsm_wr7000n10_me_nlo_ms",], n_files=23, n_events=23000,)
cpn.add_dataset(name="lrsm_wr7000n10_mm", id=7000104, processes=[procs.lrsm_wr7000n10_mm], keys=["/lrsm_wr7000n10_mm_nlo_ms",], n_files=25, n_events=25000,)

cpn.add_dataset(name="lrsm_wr7000n20_ee", id=7000201, processes=[procs.lrsm_wr7000n20_ee], keys=["/lrsm_wr7000n20_ee_nlo_ms",], n_files=24, n_events=24000,)
cpn.add_dataset(name="lrsm_wr7000n20_em", id=7000202, processes=[procs.lrsm_wr7000n20_em], keys=["/lrsm_wr7000n20_em_nlo_ms",], n_files=23, n_events=23000,)
cpn.add_dataset(name="lrsm_wr7000n20_me", id=7000203, processes=[procs.lrsm_wr7000n20_me], keys=["/lrsm_wr7000n20_me_nlo_ms",], n_files=25, n_events=25000,)
cpn.add_dataset(name="lrsm_wr7000n20_mm", id=7000204, processes=[procs.lrsm_wr7000n20_mm], keys=["/lrsm_wr7000n20_mm_nlo_ms",], n_files=24, n_events=24000,)

cpn.add_dataset(name="lrsm_wr7000n30_ee", id=7000301, processes=[procs.lrsm_wr7000n30_ee], keys=["/lrsm_wr7000n30_ee_nlo_ms",], n_files=25, n_events=25000,)
cpn.add_dataset(name="lrsm_wr7000n30_em", id=7000302, processes=[procs.lrsm_wr7000n30_em], keys=["/lrsm_wr7000n30_em_nlo_ms",], n_files=25, n_events=25000,)
cpn.add_dataset(name="lrsm_wr7000n30_me", id=7000303, processes=[procs.lrsm_wr7000n30_me], keys=["/lrsm_wr7000n30_me_nlo_ms",], n_files=25, n_events=25000,)
cpn.add_dataset(name="lrsm_wr7000n30_mm", id=7000304, processes=[procs.lrsm_wr7000n30_mm], keys=["/lrsm_wr7000n30_mm_nlo_ms",], n_files=24, n_events=24000,)

cpn.add_dataset(name="lrsm_wr7000n40_ee", id=7000401, processes=[procs.lrsm_wr7000n40_ee], keys=["/lrsm_wr7000n40_ee_nlo_ms",], n_files=25, n_events=25000,)
cpn.add_dataset(name="lrsm_wr7000n40_em", id=7000402, processes=[procs.lrsm_wr7000n40_em], keys=["/lrsm_wr7000n40_em_nlo_ms",], n_files=25, n_events=25000,)
cpn.add_dataset(name="lrsm_wr7000n40_me", id=7000403, processes=[procs.lrsm_wr7000n40_me], keys=["/lrsm_wr7000n40_me_nlo_ms",], n_files=24, n_events=24000,)
cpn.add_dataset(name="lrsm_wr7000n40_mm", id=7000404, processes=[procs.lrsm_wr7000n40_mm], keys=["/lrsm_wr7000n40_mm_nlo_ms",], n_files=25, n_events=25000,)

cpn.add_dataset(name="lrsm_wr7000n50_ee", id=7000501, processes=[procs.lrsm_wr7000n50_ee], keys=["/lrsm_wr7000n50_ee_nlo_ms",], n_files=25, n_events=25000,)
cpn.add_dataset(name="lrsm_wr7000n50_em", id=7000502, processes=[procs.lrsm_wr7000n50_em], keys=["/lrsm_wr7000n50_em_nlo_ms",], n_files=25, n_events=25000,)
cpn.add_dataset(name="lrsm_wr7000n50_me", id=7000503, processes=[procs.lrsm_wr7000n50_me], keys=["/lrsm_wr7000n50_me_nlo_ms",], n_files=25, n_events=25000,)
cpn.add_dataset(name="lrsm_wr7000n50_mm", id=7000504, processes=[procs.lrsm_wr7000n50_mm], keys=["/lrsm_wr7000n50_mm_nlo_ms",], n_files=24, n_events=24000,)

cpn.add_dataset(name="lrsm_wr7000n60_ee", id=7000601, processes=[procs.lrsm_wr7000n60_ee], keys=["/lrsm_wr7000n60_ee_nlo_ms",], n_files=25, n_events=25000,)
cpn.add_dataset(name="lrsm_wr7000n60_em", id=7000602, processes=[procs.lrsm_wr7000n60_em], keys=["/lrsm_wr7000n60_em_nlo_ms",], n_files=25, n_events=25000,)
cpn.add_dataset(name="lrsm_wr7000n60_me", id=7000603, processes=[procs.lrsm_wr7000n60_me], keys=["/lrsm_wr7000n60_me_nlo_ms",], n_files=25, n_events=25000,)
cpn.add_dataset(name="lrsm_wr7000n60_mm", id=7000604, processes=[procs.lrsm_wr7000n60_mm], keys=["/lrsm_wr7000n60_mm_nlo_ms",], n_files=25, n_events=25000,)

cpn.add_dataset(name="lrsm_wr7000n70_ee", id=7000701, processes=[procs.lrsm_wr7000n70_ee], keys=["/lrsm_wr7000n70_ee_nlo_ms",], n_files=25, n_events=25000,)
cpn.add_dataset(name="lrsm_wr7000n70_em", id=7000702, processes=[procs.lrsm_wr7000n70_em], keys=["/lrsm_wr7000n70_em_nlo_ms",], n_files=25, n_events=25000,)
cpn.add_dataset(name="lrsm_wr7000n70_me", id=7000703, processes=[procs.lrsm_wr7000n70_me], keys=["/lrsm_wr7000n70_me_nlo_ms",], n_files=25, n_events=25000,)
cpn.add_dataset(name="lrsm_wr7000n70_mm", id=7000704, processes=[procs.lrsm_wr7000n70_mm], keys=["/lrsm_wr7000n70_mm_nlo_ms",], n_files=25, n_events=25000,)

cpn.add_dataset(name="lrsm_wr7000n80_ee", id=7000801, processes=[procs.lrsm_wr7000n80_ee], keys=["/lrsm_wr7000n80_ee_nlo_ms",], n_files=25, n_events=25000,)
cpn.add_dataset(name="lrsm_wr7000n80_em", id=7000802, processes=[procs.lrsm_wr7000n80_em], keys=["/lrsm_wr7000n80_em_nlo_ms",], n_files=25, n_events=25000,)
cpn.add_dataset(name="lrsm_wr7000n80_me", id=7000803, processes=[procs.lrsm_wr7000n80_me], keys=["/lrsm_wr7000n80_me_nlo_ms",], n_files=25, n_events=25000,)
cpn.add_dataset(name="lrsm_wr7000n80_mm", id=7000804, processes=[procs.lrsm_wr7000n80_mm], keys=["/lrsm_wr7000n80_mm_nlo_ms",], n_files=25, n_events=25000,)

cpn.add_dataset(name="lrsm_wr7000n90_ee", id=7000901, processes=[procs.lrsm_wr7000n90_ee], keys=["/lrsm_wr7000n90_ee_nlo_ms",], n_files=25, n_events=25000,)
cpn.add_dataset(name="lrsm_wr7000n90_em", id=7000902, processes=[procs.lrsm_wr7000n90_em], keys=["/lrsm_wr7000n90_em_nlo_ms",], n_files=25, n_events=25000,)
cpn.add_dataset(name="lrsm_wr7000n90_me", id=7000903, processes=[procs.lrsm_wr7000n90_me], keys=["/lrsm_wr7000n90_me_nlo_ms",], n_files=25, n_events=25000,)
cpn.add_dataset(name="lrsm_wr7000n90_mm", id=7000904, processes=[procs.lrsm_wr7000n90_mm], keys=["/lrsm_wr7000n90_mm_nlo_ms",], n_files=25, n_events=25000,)

cpn.add_dataset(name="lrsm_wr7000n100_ee", id=70001001, processes=[procs.lrsm_wr7000n100_ee], keys=["/lrsm_wr7000n100_ee_nlo_ms",], n_files=25, n_events=25000,)
cpn.add_dataset(name="lrsm_wr7000n100_em", id=70001002, processes=[procs.lrsm_wr7000n100_em], keys=["/lrsm_wr7000n100_em_nlo_ms",], n_files=25, n_events=25000,)
cpn.add_dataset(name="lrsm_wr7000n100_me", id=70001003, processes=[procs.lrsm_wr7000n100_me], keys=["/lrsm_wr7000n100_me_nlo_ms",], n_files=25, n_events=25000,)
cpn.add_dataset(name="lrsm_wr7000n100_mm", id=70001004, processes=[procs.lrsm_wr7000n100_mm], keys=["/lrsm_wr7000n100_mm_nlo_ms",], n_files=24, n_events=24000,)

# WR(8000)

cpn.add_dataset(name="lrsm_wr8000n10_ee", id=8000101, processes=[procs.lrsm_wr8000n10_ee], keys=["/lrsm_wr8000n10_ee_nlo_ms",], n_files=25, n_events=25000,)
cpn.add_dataset(name="lrsm_wr8000n10_em", id=8000102, processes=[procs.lrsm_wr8000n10_em], keys=["/lrsm_wr8000n10_em_nlo_ms",], n_files=25, n_events=25000,)
cpn.add_dataset(name="lrsm_wr8000n10_me", id=8000103, processes=[procs.lrsm_wr8000n10_me], keys=["/lrsm_wr8000n10_me_nlo_ms",], n_files=25, n_events=25000,)
cpn.add_dataset(name="lrsm_wr8000n10_mm", id=8000104, processes=[procs.lrsm_wr8000n10_mm], keys=["/lrsm_wr8000n10_mm_nlo_ms",], n_files=25, n_events=25000,)

cpn.add_dataset(name="lrsm_wr8000n20_ee", id=8000201, processes=[procs.lrsm_wr8000n20_ee], keys=["/lrsm_wr8000n20_ee_nlo_ms",], n_files=25, n_events=25000,)
cpn.add_dataset(name="lrsm_wr8000n20_em", id=8000202, processes=[procs.lrsm_wr8000n20_em], keys=["/lrsm_wr8000n20_em_nlo_ms",], n_files=24, n_events=24000,)
cpn.add_dataset(name="lrsm_wr8000n20_me", id=8000203, processes=[procs.lrsm_wr8000n20_me], keys=["/lrsm_wr8000n20_me_nlo_ms",], n_files=25, n_events=25000,)
cpn.add_dataset(name="lrsm_wr8000n20_mm", id=8000204, processes=[procs.lrsm_wr8000n20_mm], keys=["/lrsm_wr8000n20_mm_nlo_ms",], n_files=24, n_events=24000,)

cpn.add_dataset(name="lrsm_wr8000n30_ee", id=8000301, processes=[procs.lrsm_wr8000n30_ee], keys=["/lrsm_wr8000n30_ee_nlo_ms",], n_files=25, n_events=25000,)
cpn.add_dataset(name="lrsm_wr8000n30_em", id=8000302, processes=[procs.lrsm_wr8000n30_em], keys=["/lrsm_wr8000n30_em_nlo_ms",], n_files=25, n_events=25000,)
cpn.add_dataset(name="lrsm_wr8000n30_me", id=8000303, processes=[procs.lrsm_wr8000n30_me], keys=["/lrsm_wr8000n30_me_nlo_ms",], n_files=24, n_events=24000,)
cpn.add_dataset(name="lrsm_wr8000n30_mm", id=8000304, processes=[procs.lrsm_wr8000n30_mm], keys=["/lrsm_wr8000n30_mm_nlo_ms",], n_files=25, n_events=25000,)

cpn.add_dataset(name="lrsm_wr8000n40_ee", id=8000401, processes=[procs.lrsm_wr8000n40_ee], keys=["/lrsm_wr8000n40_ee_nlo_ms",], n_files=25, n_events=25000,)
cpn.add_dataset(name="lrsm_wr8000n40_em", id=8000402, processes=[procs.lrsm_wr8000n40_em], keys=["/lrsm_wr8000n40_em_nlo_ms",], n_files=25, n_events=25000,)
cpn.add_dataset(name="lrsm_wr8000n40_me", id=8000403, processes=[procs.lrsm_wr8000n40_me], keys=["/lrsm_wr8000n40_me_nlo_ms",], n_files=25, n_events=25000,)
cpn.add_dataset(name="lrsm_wr8000n40_mm", id=8000404, processes=[procs.lrsm_wr8000n40_mm], keys=["/lrsm_wr8000n40_mm_nlo_ms",], n_files=25, n_events=25000,)

cpn.add_dataset(name="lrsm_wr8000n50_ee", id=8000501, processes=[procs.lrsm_wr8000n50_ee], keys=["/lrsm_wr8000n50_ee_nlo_ms",], n_files=25, n_events=25000,)
cpn.add_dataset(name="lrsm_wr8000n50_em", id=8000502, processes=[procs.lrsm_wr8000n50_em], keys=["/lrsm_wr8000n50_em_nlo_ms",], n_files=25, n_events=25000,)
cpn.add_dataset(name="lrsm_wr8000n50_me", id=8000503, processes=[procs.lrsm_wr8000n50_me], keys=["/lrsm_wr8000n50_me_nlo_ms",], n_files=25, n_events=25000,)
cpn.add_dataset(name="lrsm_wr8000n50_mm", id=8000504, processes=[procs.lrsm_wr8000n50_mm], keys=["/lrsm_wr8000n50_mm_nlo_ms",], n_files=25, n_events=25000,)

cpn.add_dataset(name="lrsm_wr8000n60_ee", id=8000601, processes=[procs.lrsm_wr8000n60_ee], keys=["/lrsm_wr8000n60_ee_nlo_ms",], n_files=25, n_events=25000,)
cpn.add_dataset(name="lrsm_wr8000n60_em", id=8000602, processes=[procs.lrsm_wr8000n60_em], keys=["/lrsm_wr8000n60_em_nlo_ms",], n_files=25, n_events=25000,)
cpn.add_dataset(name="lrsm_wr8000n60_me", id=8000603, processes=[procs.lrsm_wr8000n60_me], keys=["/lrsm_wr8000n60_me_nlo_ms",], n_files=25, n_events=25000,)
cpn.add_dataset(name="lrsm_wr8000n60_mm", id=8000604, processes=[procs.lrsm_wr8000n60_mm], keys=["/lrsm_wr8000n60_mm_nlo_ms",], n_files=25, n_events=25000,)

cpn.add_dataset(name="lrsm_wr8000n70_ee", id=8000701, processes=[procs.lrsm_wr8000n70_ee], keys=["/lrsm_wr8000n70_ee_nlo_ms",], n_files=25, n_events=25000,)
cpn.add_dataset(name="lrsm_wr8000n70_em", id=8000702, processes=[procs.lrsm_wr8000n70_em], keys=["/lrsm_wr8000n70_em_nlo_ms",], n_files=25, n_events=25000,)
cpn.add_dataset(name="lrsm_wr8000n70_me", id=8000703, processes=[procs.lrsm_wr8000n70_me], keys=["/lrsm_wr8000n70_me_nlo_ms",], n_files=25, n_events=25000,)
cpn.add_dataset(name="lrsm_wr8000n70_mm", id=8000704, processes=[procs.lrsm_wr8000n70_mm], keys=["/lrsm_wr8000n70_mm_nlo_ms",], n_files=25, n_events=25000,)

cpn.add_dataset(name="lrsm_wr8000n80_ee", id=8000801, processes=[procs.lrsm_wr8000n80_ee], keys=["/lrsm_wr8000n80_ee_nlo_ms",], n_files=25, n_events=25000,)
cpn.add_dataset(name="lrsm_wr8000n80_em", id=8000802, processes=[procs.lrsm_wr8000n80_em], keys=["/lrsm_wr8000n80_em_nlo_ms",], n_files=25, n_events=25000,)
cpn.add_dataset(name="lrsm_wr8000n80_me", id=8000803, processes=[procs.lrsm_wr8000n80_me], keys=["/lrsm_wr8000n80_me_nlo_ms",], n_files=25, n_events=25000,)
cpn.add_dataset(name="lrsm_wr8000n80_mm", id=8000804, processes=[procs.lrsm_wr8000n80_mm], keys=["/lrsm_wr8000n80_mm_nlo_ms",], n_files=25, n_events=25000,)

cpn.add_dataset(name="lrsm_wr8000n90_ee", id=8000901, processes=[procs.lrsm_wr8000n90_ee], keys=["/lrsm_wr8000n90_ee_nlo_ms",], n_files=25, n_events=25000,)
cpn.add_dataset(name="lrsm_wr8000n90_em", id=8000902, processes=[procs.lrsm_wr8000n90_em], keys=["/lrsm_wr8000n90_em_nlo_ms",], n_files=25, n_events=25000,)
cpn.add_dataset(name="lrsm_wr8000n90_me", id=8000903, processes=[procs.lrsm_wr8000n90_me], keys=["/lrsm_wr8000n90_me_nlo_ms",], n_files=25, n_events=25000,)
cpn.add_dataset(name="lrsm_wr8000n90_mm", id=8000904, processes=[procs.lrsm_wr8000n90_mm], keys=["/lrsm_wr8000n90_mm_nlo_ms",], n_files=25, n_events=25000,)

cpn.add_dataset(name="lrsm_wr8000n100_ee", id=80001001, processes=[procs.lrsm_wr8000n100_ee], keys=["/lrsm_wr8000n100_ee_nlo_ms",], n_files=25, n_events=25000,)
cpn.add_dataset(name="lrsm_wr8000n100_em", id=80001002, processes=[procs.lrsm_wr8000n100_em], keys=["/lrsm_wr8000n100_em_nlo_ms",], n_files=24, n_events=24000,)
cpn.add_dataset(name="lrsm_wr8000n100_me", id=80001003, processes=[procs.lrsm_wr8000n100_me], keys=["/lrsm_wr8000n100_me_nlo_ms",], n_files=25, n_events=25000,)
cpn.add_dataset(name="lrsm_wr8000n100_mm", id=80001004, processes=[procs.lrsm_wr8000n100_mm], keys=["/lrsm_wr8000n100_mm_nlo_ms",], n_files=25, n_events=25000,)
