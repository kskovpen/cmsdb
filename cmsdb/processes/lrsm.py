# coding: utf-8

"""
LRSM process definitions.
"""

__all__ = [
    "lrsm_wr4000n10", "lrsm_wr4000n20", "lrsm_wr4000n30", "lrsm_wr4000n40", "lrsm_wr4000n50", "lrsm_wr4000n60", "lrsm_wr4000n70", "lrsm_wr4000n80", "lrsm_wr4000n90", "lrsm_wr4000n100",
    "lrsm_wr5000n10", "lrsm_wr5000n20", "lrsm_wr5000n30", "lrsm_wr5000n40", "lrsm_wr5000n50", "lrsm_wr5000n60", "lrsm_wr5000n70", "lrsm_wr5000n80", "lrsm_wr5000n90", "lrsm_wr5000n100",
    "lrsm_wr6000n10", "lrsm_wr6000n20", "lrsm_wr6000n30", "lrsm_wr6000n40", "lrsm_wr6000n50", "lrsm_wr6000n60", "lrsm_wr6000n70", "lrsm_wr6000n80", "lrsm_wr6000n90", "lrsm_wr6000n100",
    "lrsm_wr7000n10", "lrsm_wr7000n20", "lrsm_wr7000n30", "lrsm_wr7000n40", "lrsm_wr7000n50", "lrsm_wr7000n60", "lrsm_wr7000n70", "lrsm_wr7000n80", "lrsm_wr7000n90", "lrsm_wr7000n100",
    "lrsm_wr8000n10", "lrsm_wr8000n20", "lrsm_wr8000n30", "lrsm_wr8000n40", "lrsm_wr8000n50", "lrsm_wr8000n60", "lrsm_wr8000n70", "lrsm_wr8000n80", "lrsm_wr8000n90", "lrsm_wr8000n100",
]

from order import Process
from scinum import Number

import cmsdb.constants as const

# Cross sections are reported per neutrino type assuming the SM N mixing parameters

lrsm_wr4000n10 = Process(name="lrsm_wr4000n10", id=400010, label="$W_R$(4000)N(10)", xsecs={13.6: Number(2.491e-03)},)
lrsm_wr4000n20 = Process(name="lrsm_wr4000n20", id=400020, label="$W_R$(4000)N(20)", xsecs={13.6: Number(2.471e-03)},)
lrsm_wr4000n30 = Process(name="lrsm_wr4000n30", id=400030, label="$W_R$(4000)N(30)", xsecs={13.6: Number(2.453e-03)},)
lrsm_wr4000n40 = Process(name="lrsm_wr4000n40", id=400040, label="$W_R$(4000)N(40)", xsecs={13.6: Number(2.435e-03)},)
lrsm_wr4000n50 = Process(name="lrsm_wr4000n50", id=400050, label="$W_R$(4000)N(50)", xsecs={13.6: Number(2.457e-03)},)
lrsm_wr4000n60 = Process(name="lrsm_wr4000n60", id=400060, label="$W_R$(4000)N(60)", xsecs={13.6: Number(2.450e-03)},)
lrsm_wr4000n70 = Process(name="lrsm_wr4000n70", id=400070, label="$W_R$(4000)N(70)", xsecs={13.6: Number(2.425e-03)},)
lrsm_wr4000n80 = Process(name="lrsm_wr4000n80", id=400080, label="$W_R$(4000)N(80)", xsecs={13.6: Number(2.398e-03)},)
lrsm_wr4000n90 = Process(name="lrsm_wr4000n90", id=400090, label="$W_R$(4000)N(90)", xsecs={13.6: Number(2.400e-03)},)
lrsm_wr4000n100 = Process(name="lrsm_wr4000n100", id=4000100, label="$W_R$(4000)N(100)", xsecs={13.6: Number(2.354e-03)},)

lrsm_wr5000n10 = Process(name="lrsm_wr5000n10", id=500010, label="$W_R$(5000)N(10)", xsecs={13.6: Number(6.778e-04)},)
lrsm_wr5000n20 = Process(name="lrsm_wr5000n20", id=500020, label="$W_R$(5000)N(20)", xsecs={13.6: Number(6.818e-04)},)
lrsm_wr5000n30 = Process(name="lrsm_wr5000n30", id=500030, label="$W_R$(5000)N(30)", xsecs={13.6: Number(6.782e-04)},)
lrsm_wr5000n40 = Process(name="lrsm_wr5000n40", id=500040, label="$W_R$(5000)N(40)", xsecs={13.6: Number(6.650e-04)},)
lrsm_wr5000n50 = Process(name="lrsm_wr5000n50", id=500050, label="$W_R$(5000)N(50)", xsecs={13.6: Number(6.586e-04)},)
lrsm_wr5000n60 = Process(name="lrsm_wr5000n60", id=500060, label="$W_R$(5000)N(60)", xsecs={13.6: Number(6.538e-04)},)
lrsm_wr5000n70 = Process(name="lrsm_wr5000n70", id=500070, label="$W_R$(5000)N(70)", xsecs={13.6: Number(6.487e-04)},)
lrsm_wr5000n80 = Process(name="lrsm_wr5000n80", id=500080, label="$W_R$(5000)N(80)", xsecs={13.6: Number(6.403e-04)},)
lrsm_wr5000n90 = Process(name="lrsm_wr5000n90", id=500090, label="$W_R$(5000)N(90)", xsecs={13.6: Number(6.364e-04)},)
lrsm_wr5000n100 = Process(name="lrsm_wr5000n100", id=5000100, label="$W_R$(5000)N(100)", xsecs={13.6: Number(6.235e-04)},)

lrsm_wr6000n10 = Process(name="lrsm_wr6000n10", id=600010, label="$W_R$(6000)N(10)", xsecs={13.6: Number(2.546e-04)},)
lrsm_wr6000n20 = Process(name="lrsm_wr6000n20", id=600020, label="$W_R$(6000)N(20)", xsecs={13.6: Number(2.559e-04)},)
lrsm_wr6000n30 = Process(name="lrsm_wr6000n30", id=600030, label="$W_R$(6000)N(30)", xsecs={13.6: Number(2.546e-04)},)
lrsm_wr6000n40 = Process(name="lrsm_wr6000n40", id=600040, label="$W_R$(6000)N(40)", xsecs={13.6: Number(2.516e-04)},)
lrsm_wr6000n50 = Process(name="lrsm_wr6000n50", id=600050, label="$W_R$(6000)N(50)", xsecs={13.6: Number(2.469e-04)},)
lrsm_wr6000n60 = Process(name="lrsm_wr6000n60", id=600060, label="$W_R$(6000)N(60)", xsecs={13.6: Number(2.430e-04)},)
lrsm_wr6000n70 = Process(name="lrsm_wr6000n70", id=600070, label="$W_R$(6000)N(70)", xsecs={13.6: Number(2.401e-04)},)
lrsm_wr6000n80 = Process(name="lrsm_wr6000n80", id=600080, label="$W_R$(6000)N(80)", xsecs={13.6: Number(2.374e-04)},)
lrsm_wr6000n90 = Process(name="lrsm_wr6000n90", id=600090, label="$W_R$(6000)N(90)", xsecs={13.6: Number(2.340e-04)},)
lrsm_wr6000n100 = Process(name="lrsm_wr6000n100", id=6000100, label="$W_R$(6000)N(100)", xsecs={13.6: Number(2.309e-04)},)

lrsm_wr7000n10 = Process(name="lrsm_wr7000n10", id=700010, label="$W_R$(7000)N(10)", xsecs={13.6: Number(1.209e-04)},)
lrsm_wr7000n20 = Process(name="lrsm_wr7000n20", id=700020, label="$W_R$(7000)N(20)", xsecs={13.6: Number(1.180e-04)},)
lrsm_wr7000n30 = Process(name="lrsm_wr7000n30", id=700030, label="$W_R$(7000)N(30)", xsecs={13.6: Number(1.175e-04)},)
lrsm_wr7000n40 = Process(name="lrsm_wr7000n40", id=700040, label="$W_R$(7000)N(40)", xsecs={13.6: Number(1.156e-04)},)
lrsm_wr7000n50 = Process(name="lrsm_wr7000n50", id=700050, label="$W_R$(7000)N(50)", xsecs={13.6: Number(1.140e-04)},)
lrsm_wr7000n60 = Process(name="lrsm_wr7000n60", id=700060, label="$W_R$(7000)N(60)", xsecs={13.6: Number(1.128e-04)},)
lrsm_wr7000n70 = Process(name="lrsm_wr7000n70", id=700070, label="$W_R$(7000)N(70)", xsecs={13.6: Number(1.111e-04)},)
lrsm_wr7000n80 = Process(name="lrsm_wr7000n80", id=700080, label="$W_R$(7000)N(80)", xsecs={13.6: Number(1.089e-04)},)
lrsm_wr7000n90 = Process(name="lrsm_wr7000n90", id=700090, label="$W_R$(7000)N(90)", xsecs={13.6: Number(1.078e-04)},)
lrsm_wr7000n100 = Process(name="lrsm_wr7000n100", id=7000100, label="$W_R$(7000)N(100)", xsecs={13.6: Number(1.057e-04)},)

lrsm_wr8000n10 = Process(name="lrsm_wr8000n10", id=800010, label="$W_R$(8000)N(10)", xsecs={13.6: Number(6.279e-05)},)
lrsm_wr8000n20 = Process(name="lrsm_wr8000n20", id=800020, label="$W_R$(8000)N(20)", xsecs={13.6: Number(6.191e-05)},)
lrsm_wr8000n30 = Process(name="lrsm_wr8000n30", id=800030, label="$W_R$(8000)N(30)", xsecs={13.6: Number(6.100e-05)},)
lrsm_wr8000n40 = Process(name="lrsm_wr8000n40", id=800040, label="$W_R$(8000)N(40)", xsecs={13.6: Number(5.983e-05)},)
lrsm_wr8000n50 = Process(name="lrsm_wr8000n50", id=800050, label="$W_R$(8000)N(50)", xsecs={13.6: Number(5.947e-05)},)
lrsm_wr8000n60 = Process(name="lrsm_wr8000n60", id=800060, label="$W_R$(8000)N(60)", xsecs={13.6: Number(5.848e-05)},)
lrsm_wr8000n70 = Process(name="lrsm_wr8000n70", id=800070, label="$W_R$(8000)N(70)", xsecs={13.6: Number(5.776e-05)},)
lrsm_wr8000n80 = Process(name="lrsm_wr8000n80", id=800080, label="$W_R$(8000)N(80)", xsecs={13.6: Number(5.625e-05)},)
lrsm_wr8000n90 = Process(name="lrsm_wr8000n90", id=800090, label="$W_R$(8000)N(90)", xsecs={13.6: Number(5.553e-05)},)
lrsm_wr8000n100 = Process(name="lrsm_wr8000n100", id=8000100, label="$W_R$(8000)N(100)", xsecs={13.6: Number(5.520e-05)},)
