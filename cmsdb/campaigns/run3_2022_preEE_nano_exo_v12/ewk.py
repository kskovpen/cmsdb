# coding: utf-8

"""
Electroweak datasets for the 2022 pre-EE data-taking campaign (EXO nano)
"""

from order import DatasetInfo

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_preEE_nano_exo_v12 import campaign_run3_2022_preEE_nano_exo_v12 as cpn

cpn.add_dataset(
    name="w_lnu_4j", id=148039954, processes=[procs.w_lnu_4j], keys=["/WtoLNu-4Jets_TuneCP5_13p6TeV_madgraphMLM-pythia8",],
    n_files=1163,
    n_events=87118387,
)

cpn.add_dataset(
    name="ww_pythia", id=14800098, processes=[procs.ww], keys=["/WW_TuneCP5_13p6TeV_pythia8",],
    n_files=231,
    n_events=14819717,
)

cpn.add_dataset(
    name="wz_pythia", id=14803901, processes=[procs.wz], keys=["/WZ_TuneCP5_13p6TeV_pythia8",],
    n_files=139,
    n_events=6931787,
)

cpn.add_dataset(
    name="zz_pythia", id=14587173, processes=[procs.zz], keys=["/ZZ_TuneCP5_13p6TeV_pythia8",],
    n_files=29,
    n_events=1137950,
)

cpn.add_dataset(
    name="dy_2e_mll200to400", id=21200400, processes=[procs.dy_2e_mll200to400], keys=["/DYto2E_MLL-200to400_TuneCP5_13p6TeV_powheg-pythia8",],
    n_files=48,
    n_events=822999,
)

cpn.add_dataset(
    name="dy_2e_mll2500to4000", id=2125004000, processes=[procs.dy_2e_mll2500to4000], keys=["/DYto2E_MLL-2500to4000_TuneCP5_13p6TeV_powheg-pythia8",],
    n_files=7,
    n_events=290480,
)

cpn.add_dataset(
    name="dy_2e_mll4000to6000", id=2140006000, processes=[procs.dy_2e_mll4000to6000], keys=["/DYto2E_MLL-4000to6000_TuneCP5_13p6TeV_powheg-pythia8",],
    n_files=19,
    n_events=283694,
)

cpn.add_dataset(
    name="dy_2mu_mll6000", id=226000, processes=[procs.dy_2mu_mll6000], keys=["/DYto2Mu_MLL-6000_TuneCP5_13p6TeV_powheg-pythia8",],
    n_files=17,
    n_events=137148,
)

cpn.add_dataset(
    name="dy_2mu_mll200to400", id=22200400, processes=[procs.dy_2mu_mll200to400], keys=["/DYto2Mu_MLL-200to400_TuneCP5_13p6TeV_powheg-pythia8",],
    n_files=36,
    n_events=722640,
)

cpn.add_dataset(
    name="dy_2mu_mll4000to6000", id=2240006000, processes=[procs.dy_2mu_mll4000to6000], keys=["/DYto2Mu_MLL-4000to6000_TuneCP5_13p6TeV_powheg-pythia8",],
    n_files=20,
    n_events=249600,
)

cpn.add_dataset(
    name="dy_2mu_mll2500to4000", id=2225004000, processes=[procs.dy_2mu_mll2500to4000], keys=["/DYto2Mu_MLL-2500to4000_TuneCP5_13p6TeV_powheg-pythia8",],
    n_files=12,
    n_events=242418,
)

cpn.add_dataset(
    name="dy_2tau_mll400to800", id=23400800, processes=[procs.dy_2tau_mll400to800], keys=["/DYto2Tau_MLL-400to800_TuneCP5_13p6TeV_powheg-pythia8",],
    n_files=28,
    n_events=812638,
)

cpn.add_dataset(
    name="dy_2tau_mll6000", id=236000, processes=[procs.dy_2tau_mll6000], keys=["/DYto2Tau_MLL-6000_TuneCP5_13p6TeV_powheg-pythia8",],
    n_files=21,
    n_events=146394,
)

cpn.add_dataset(
    name="dy_2tau_mll4000to6000", id=2340006000, processes=[procs.dy_2tau_mll4000to6000], keys=["/DYto2Tau_MLL-4000to6000_TuneCP5_13p6TeV_powheg-pythia8",],
    n_files=16,
    n_events=270437,
)

cpn.add_dataset(
    name="dy_2tau_mll10to50", id=231050, processes=[procs.dy_2tau_mll10to50], keys=["/DYto2Tau_MLL-10to50_TuneCP5_13p6TeV_powheg-pythia8",],
    n_files=31,
    n_events=1271031,
)

cpn.add_dataset(
    name="dy_2tau_mll120to200", id=23120200, processes=[procs.dy_2tau_mll120to200], keys=["/DYto2Tau_MLL-120to200_TuneCP5_13p6TeV_powheg-pythia8",],
    n_files=36,
    n_events=1297968,
)

cpn.add_dataset(
    name="dy_2tau_mll800to1500", id=238001500, processes=[procs.dy_2tau_mll800to1500], keys=["/DYto2Tau_MLL-800to1500_TuneCP5_13p6TeV_powheg-pythia8",],
    n_files=28,
    n_events=571160,
)

cpn.add_dataset(
    name="dy_2e_mll10to50", id=211050, processes=[procs.dy_2e_mll10to50], keys=["/DYto2E_MLL-10to50_TuneCP5_13p6TeV_powheg-pythia8",],
    n_files=33,
    n_events=1127255,
)

cpn.add_dataset(
    name="dy_2e_mll120to200", id=21120200, processes=[procs.dy_2e_mll120to200], keys=["/DYto2E_MLL-120to200_TuneCP5_13p6TeV_powheg-pythia8",],
    n_files=39,
    n_events=1451579,
)

cpn.add_dataset(
    name="dy_2mu_mll800to1500", id=228001500, processes=[procs.dy_2mu_mll800to1500], keys=["/DYto2Mu_MLL-800to1500_TuneCP5_13p6TeV_powheg-pythia8",],
    n_files=25,
    n_events=531380,
)

cpn.add_dataset(
    name="dy_2mu_mll50to120", id=2250120, processes=[procs.dy_2mu_mll50to120], keys=["/DYto2Mu_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8",],
    n_files=65,
    n_events=2696532,
)

cpn.add_dataset(
    name="dy_2e_mll400to800", id=21400800, processes=[procs.dy_2e_mll400to800], keys=["/DYto2E_MLL-400to800_TuneCP5_13p6TeV_powheg-pythia8",],
    n_files=33,
    n_events=616835,
)

cpn.add_dataset(
    name="dy_2mu_mll10to50", id=221050, processes=[procs.dy_2mu_mll10to50], keys=["/DYto2Mu_MLL-10to50_TuneCP5_13p6TeV_powheg-pythia8",],
    n_files=34,
    n_events=1143200,
)

cpn.add_dataset(
    name="dy_2mu_mll120to200", id=22120200, processes=[procs.dy_2mu_mll120to200], keys=["/DYto2Mu_MLL-120to200_TuneCP5_13p6TeV_powheg-pythia8",],
    n_files=56,
    n_events=1399290,
)

cpn.add_dataset(
    name="dy_2mu_mll400to800", id=22400800, processes=[procs.dy_2mu_mll400to800], keys=["/DYto2Mu_MLL-400to800_TuneCP5_13p6TeV_powheg-pythia8",],
    n_files=49,
    n_events=842592,
)

cpn.add_dataset(
    name="dy_2tau_mll200to400", id=23200400, processes=[procs.dy_2tau_mll200to400], keys=["/DYto2Tau_MLL-200to400_TuneCP5_13p6TeV_powheg-pythia8",],
    n_files=29,
    n_events=810260,
)

cpn.add_dataset(
    name="dy_2e_mll6000", id=216000, processes=[procs.dy_2e_mll6000], keys=["/DYto2E_MLL-6000_TuneCP5_13p6TeV_powheg-pythia8",],
    n_files=14,
    n_events=124132,
)

cpn.add_dataset(
    name="dy_2tau_mll1500to2500", id=2315002500, processes=[procs.dy_2tau_mll1500to2500], keys=["/DYto2Tau_MLL-1500to2500_TuneCP5_13p6TeV_powheg-pythia8",],
    n_files=36,
    n_events=538256,
)

cpn.add_dataset(
    name="dy_2tau_mll50to120", id=2350120, processes=[procs.dy_2tau_mll50to120], keys=["/DYto2Tau_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8",],
    n_files=76,
    n_events=2865756,
)

cpn.add_dataset(
    name="dy_2mu_mll1500to2500", id=2215002500, processes=[procs.dy_2mu_mll1500to2500], keys=["/DYto2Mu_MLL-1500to2500_TuneCP5_13p6TeV_powheg-pythia8",],
    n_files=24,
    n_events=566466,
)

cpn.add_dataset(
    name="dy_2e_mll800to1500", id=218001500, processes=[procs.dy_2e_mll800to1500], keys=["/DYto2E_MLL-800to1500_TuneCP5_13p6TeV_powheg-pythia8",],
    n_files=26,
    n_events=571795,
)

cpn.add_dataset(
    name="dy_2e_mll50to120", id=2150120, processes=[procs.dy_2e_mll50to120], keys=["/DYto2E_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8",],
    n_files=86,
    n_events=2642585,
)

cpn.add_dataset(
    name="dy_2tau_mll2500to4000", id=2325004000, processes=[procs.dy_2tau_mll2500to4000], keys=["/DYto2Tau_MLL-2500to4000_TuneCP5_13p6TeV_powheg-pythia8",],
    n_files=17,
    n_events=189130,
)

cpn.add_dataset(
    name="dy_2e_mll1500to2500", id=2115002500, processes=[procs.dy_2e_mll1500to2500], keys=["/DYto2E_MLL-1500to2500_TuneCP5_13p6TeV_powheg-pythia8",],
    n_files=10,
    n_events=497637,
)

