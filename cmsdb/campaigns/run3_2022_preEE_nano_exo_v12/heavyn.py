"""
HeavyN datasets for the 2022 pre-EE data-taking campaign (EXO nano)
"""

from order import DatasetInfo

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_preEE_nano_exo_v12 import campaign_run3_2022_preEE_nano_exo_v12 as cpn

# heavyn_m12_v10-6_mumu
# heavyn_m14_v10-2_mumu
# heavyn_m4_v10-2_mumu
# heavyn_m4_v10-6_mumu
# heavyn_m8_v10-4_mumu

cpn.add_dataset(name="heavyn_m12_v10m6_mm", id=1210622, processes=[procs.heavyn_m12_v10m6_mm], keys=["/heavyn_m12_v10-6_mumu",], n_files=25, n_events=25000,)
cpn.add_dataset(name="heavyn_m14_v10m2_mm", id=1410222, processes=[procs.heavyn_m14_v10m2_mm], keys=["/heavyn_m14_v10-2_mumu",], n_files=25, n_events=25000,)
cpn.add_dataset(name="heavyn_m4_v10m2_mm", id=410222, processes=[procs.heavyn_m4_v10m2_mm], keys=["/heavyn_m4_v10-2_mumu",], n_files=24, n_events=24000,)
cpn.add_dataset(name="heavyn_m4_v10m6_mm", id=410622, processes=[procs.heavyn_m4_v10m6_mm], keys=["/heavyn_m4_v10-6_mumu",], n_files=25, n_events=25000,)
cpn.add_dataset(name="heavyn_m8_v10m4_mm", id=810422, processes=[procs.heavyn_m8_v10m4_mm], keys=["/heavyn_m8_v10-4_mumu",], n_files=25, n_events=25000,)