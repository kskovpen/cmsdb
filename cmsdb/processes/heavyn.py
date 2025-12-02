"""
HeavyN process definitions.
"""

__all__ = [

    "heavyn_m12_v10-6_mumu", "heavyn_m14_v10-2_mumu", "heavyn_m4_v10-2_mumu", "heavyn_m4_v10-6_mumu", "heavyn_m8_v10-4_mumu",
]


from order import Process
from scinum import Number

import cmsdb.constants as const
# Naming: mN (2 difigits) | constant 10(power) | 11 for ee 22 for mm

heavyn_m12_v10m6_mm = Process(name="heavyn_m12_v10m6_mm", id=1210622, label=r"$V=10^{-6}$ $m_N=12$ GeV ($\mu \mu$)", xsecs={13.6: Number(2.491e-03)},)
heavyn_m14_v10m2_mm = Process(name="heavyn_m14_v10m2_mm", id=1410222, label=r"$V=10^{-2}$ $m_N=14$ GeV ($\mu \mu$)", xsecs={13.6: Number(2.491e-03)},)
heavyn_m4_v10m2_mm = Process(name="heavyn_m04_v10m2_mm", id=410222, label=r"$V=10^{-2}$ $m_N=4$ GeV ($\mu \mu$)", xsecs={13.6: Number(2.491e-03)},)
heavyn_m4_v10m6_mm = Process(name="heavyn_m04_v10m6_mm", id=410622, label=r"$V=10^{-6}$ $m_N=4$ GeV ($\mu \mu$)", xsecs={13.6: Number(2.491e-03)},)
heavyn_m8_v10m4_mm = Process(name="heavyn_m08_v10m6_mm", id=810422, label=r"$V=10^{-6}$ $m_N=8$ GeV ($\mu \mu$)", xsecs={13.6: Number(2.491e-03)},)