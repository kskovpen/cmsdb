# coding: utf-8

"""
LRSM process definitions.
"""

__all__ = [
    "lrsm_wr4000n10_ee", "lrsm_wr4000n10_em", "lrsm_wr4000n10_me", "lrsm_wr4000n10_mm",
    "lrsm_wr4000n20_ee", "lrsm_wr4000n20_em", "lrsm_wr4000n20_me", "lrsm_wr4000n20_mm",
    "lrsm_wr4000n30_ee", "lrsm_wr4000n30_em", "lrsm_wr4000n30_me", "lrsm_wr4000n30_mm",
    "lrsm_wr4000n40_ee", "lrsm_wr4000n40_em", "lrsm_wr4000n40_me", "lrsm_wr4000n40_mm",
    "lrsm_wr4000n50_ee", "lrsm_wr4000n50_em", "lrsm_wr4000n50_me", "lrsm_wr4000n50_mm",
    "lrsm_wr4000n60_ee", "lrsm_wr4000n60_em", "lrsm_wr4000n60_me", "lrsm_wr4000n60_mm",
    "lrsm_wr4000n70_ee", "lrsm_wr4000n70_em", "lrsm_wr4000n70_me", "lrsm_wr4000n70_mm",
    "lrsm_wr4000n80_ee", "lrsm_wr4000n80_em", "lrsm_wr4000n80_me", "lrsm_wr4000n80_mm",
    "lrsm_wr4000n90_ee", "lrsm_wr4000n90_em", "lrsm_wr4000n90_me", "lrsm_wr4000n90_mm",
    "lrsm_wr4000n100_ee", "lrsm_wr4000n100_em", "lrsm_wr4000n100_me", "lrsm_wr4000n100_mm",
    "lrsm_wr5000n10_ee", "lrsm_wr5000n10_em", "lrsm_wr5000n10_me", "lrsm_wr5000n10_mm",
    "lrsm_wr5000n20_ee", "lrsm_wr5000n20_em", "lrsm_wr5000n20_me", "lrsm_wr5000n20_mm",
    "lrsm_wr5000n30_ee", "lrsm_wr5000n30_em", "lrsm_wr5000n30_me", "lrsm_wr5000n30_mm",
    "lrsm_wr5000n40_ee", "lrsm_wr5000n40_em", "lrsm_wr5000n40_me", "lrsm_wr5000n40_mm",
    "lrsm_wr5000n50_ee", "lrsm_wr5000n50_em", "lrsm_wr5000n50_me", "lrsm_wr5000n50_mm",
    "lrsm_wr5000n60_ee", "lrsm_wr5000n60_em", "lrsm_wr5000n60_me", "lrsm_wr5000n60_mm",
    "lrsm_wr5000n70_ee", "lrsm_wr5000n70_em", "lrsm_wr5000n70_me", "lrsm_wr5000n70_mm",
    "lrsm_wr5000n80_ee", "lrsm_wr5000n80_em", "lrsm_wr5000n80_me", "lrsm_wr5000n80_mm",
    "lrsm_wr5000n90_ee", "lrsm_wr5000n90_em", "lrsm_wr5000n90_me", "lrsm_wr5000n90_mm",
    "lrsm_wr5000n100_ee", "lrsm_wr5000n100_em", "lrsm_wr5000n100_me", "lrsm_wr5000n100_mm",
    "lrsm_wr6000n10_ee", "lrsm_wr6000n10_em", "lrsm_wr6000n10_me", "lrsm_wr6000n10_mm",
    "lrsm_wr6000n20_ee", "lrsm_wr6000n20_em", "lrsm_wr6000n20_me", "lrsm_wr6000n20_mm",
    "lrsm_wr6000n30_ee", "lrsm_wr6000n30_em", "lrsm_wr6000n30_me", "lrsm_wr6000n30_mm",
    "lrsm_wr6000n40_ee", "lrsm_wr6000n40_em", "lrsm_wr6000n40_me", "lrsm_wr6000n40_mm",
    "lrsm_wr6000n50_ee", "lrsm_wr6000n50_em", "lrsm_wr6000n50_me", "lrsm_wr6000n50_mm",
    "lrsm_wr6000n60_ee", "lrsm_wr6000n60_em", "lrsm_wr6000n60_me", "lrsm_wr6000n60_mm",
    "lrsm_wr6000n70_ee", "lrsm_wr6000n70_em", "lrsm_wr6000n70_me", "lrsm_wr6000n70_mm",
    "lrsm_wr6000n80_ee", "lrsm_wr6000n80_em", "lrsm_wr6000n80_me", "lrsm_wr6000n80_mm",
    "lrsm_wr6000n90_ee", "lrsm_wr6000n90_em", "lrsm_wr6000n90_me", "lrsm_wr6000n90_mm",
    "lrsm_wr6000n100_ee", "lrsm_wr6000n100_em", "lrsm_wr6000n100_me", "lrsm_wr6000n100_mm",
    "lrsm_wr7000n10_ee", "lrsm_wr7000n10_em", "lrsm_wr7000n10_me", "lrsm_wr7000n10_mm",
    "lrsm_wr7000n20_ee", "lrsm_wr7000n20_em", "lrsm_wr7000n20_me", "lrsm_wr7000n20_mm",
    "lrsm_wr7000n30_ee", "lrsm_wr7000n30_em", "lrsm_wr7000n30_me", "lrsm_wr7000n30_mm",
    "lrsm_wr7000n40_ee", "lrsm_wr7000n40_em", "lrsm_wr7000n40_me", "lrsm_wr7000n40_mm",
    "lrsm_wr7000n50_ee", "lrsm_wr7000n50_em", "lrsm_wr7000n50_me", "lrsm_wr7000n50_mm",
    "lrsm_wr7000n60_ee", "lrsm_wr7000n60_em", "lrsm_wr7000n60_me", "lrsm_wr7000n60_mm",
    "lrsm_wr7000n70_ee", "lrsm_wr7000n70_em", "lrsm_wr7000n70_me", "lrsm_wr7000n70_mm",
    "lrsm_wr7000n80_ee", "lrsm_wr7000n80_em", "lrsm_wr7000n80_me", "lrsm_wr7000n80_mm",
    "lrsm_wr7000n90_ee", "lrsm_wr7000n90_em", "lrsm_wr7000n90_me", "lrsm_wr7000n90_mm",
    "lrsm_wr7000n100_ee", "lrsm_wr7000n100_em", "lrsm_wr7000n100_me", "lrsm_wr7000n100_mm",
    "lrsm_wr8000n10_ee", "lrsm_wr8000n10_em", "lrsm_wr8000n10_me", "lrsm_wr8000n10_mm",
    "lrsm_wr8000n20_ee", "lrsm_wr8000n20_em", "lrsm_wr8000n20_me", "lrsm_wr8000n20_mm",
    "lrsm_wr8000n30_ee", "lrsm_wr8000n30_em", "lrsm_wr8000n30_me", "lrsm_wr8000n30_mm",
    "lrsm_wr8000n40_ee", "lrsm_wr8000n40_em", "lrsm_wr8000n40_me", "lrsm_wr8000n40_mm",
    "lrsm_wr8000n50_ee", "lrsm_wr8000n50_em", "lrsm_wr8000n50_me", "lrsm_wr8000n50_mm",
    "lrsm_wr8000n60_ee", "lrsm_wr8000n60_em", "lrsm_wr8000n60_me", "lrsm_wr8000n60_mm",
    "lrsm_wr8000n70_ee", "lrsm_wr8000n70_em", "lrsm_wr8000n70_me", "lrsm_wr8000n70_mm",
    "lrsm_wr8000n80_ee", "lrsm_wr8000n80_em", "lrsm_wr8000n80_me", "lrsm_wr8000n80_mm",
    "lrsm_wr8000n90_ee", "lrsm_wr8000n90_em", "lrsm_wr8000n90_me", "lrsm_wr8000n90_mm",
    "lrsm_wr8000n100_ee", "lrsm_wr8000n100_em", "lrsm_wr8000n100_me", "lrsm_wr8000n100_mm",
]

from order import Process
from scinum import Number

import cmsdb.constants as const

# Cross sections are reported per neutrino type assuming the SM N mixing parameters
# FIXME: make sure the corss section is the right one

# WR(4000)

lrsm_wr4000n10 = Process(name="lrsm_wr4000n10", id=400010, label="$W_R$(4000)N(10)", xsecs={13.6: Number(2.491e-03)},)
lrsm_wr4000n10_ee = lrsm_wr4000n10.add_process(name="lrsm_wr4000n10_ee", id=40001001, xsecs={13.6: Number(2.491e-03)},)
lrsm_wr4000n10_em = lrsm_wr4000n10.add_process(name="lrsm_wr4000n10_em", id=40001002, xsecs={13.6: Number(2.491e-03)},)
lrsm_wr4000n10_me = lrsm_wr4000n10.add_process(name="lrsm_wr4000n10_me", id=40001003, xsecs={13.6: Number(2.491e-03)},)
lrsm_wr4000n10_mm = lrsm_wr4000n10.add_process(name="lrsm_wr4000n10_mm", id=40001004, xsecs={13.6: Number(2.491e-03)},)

lrsm_wr4000n20 = Process(name="lrsm_wr4000n20", id=400020, label="$W_R$(4000)N(20)", xsecs={13.6: Number(2.471e-03)},)
lrsm_wr4000n20_ee = lrsm_wr4000n20.add_process(name="lrsm_wr4000n20_ee", id=40002001, xsecs={13.6: Number(2.471e-03)},)
lrsm_wr4000n20_em = lrsm_wr4000n20.add_process(name="lrsm_wr4000n20_em", id=40002002, xsecs={13.6: Number(2.471e-03)},)
lrsm_wr4000n20_me = lrsm_wr4000n20.add_process(name="lrsm_wr4000n20_me", id=40002003, xsecs={13.6: Number(2.471e-03)},)
lrsm_wr4000n20_mm = lrsm_wr4000n20.add_process(name="lrsm_wr4000n20_mm", id=40002004, xsecs={13.6: Number(2.471e-03)},)

lrsm_wr4000n30 = Process(name="lrsm_wr4000n30", id=400030, label="$W_R$(4000)N(30)", xsecs={13.6: Number(2.453e-03)},)
lrsm_wr4000n30_ee = lrsm_wr4000n30.add_process(name="lrsm_wr4000n30_ee", id=40003001, xsecs={13.6: Number(2.453e-03)},)
lrsm_wr4000n30_em = lrsm_wr4000n30.add_process(name="lrsm_wr4000n30_em", id=40003002, xsecs={13.6: Number(2.453e-03)},)
lrsm_wr4000n30_me = lrsm_wr4000n30.add_process(name="lrsm_wr4000n30_me", id=40003003, xsecs={13.6: Number(2.453e-03)},)
lrsm_wr4000n30_mm = lrsm_wr4000n30.add_process(name="lrsm_wr4000n30_mm", id=40003004, xsecs={13.6: Number(2.453e-03)},)

lrsm_wr4000n40 = Process(name="lrsm_wr4000n40", id=400040, label="$W_R$(4000)N(40)", xsecs={13.6: Number(2.435e-03)},)
lrsm_wr4000n40_ee = lrsm_wr4000n40.add_process(name="lrsm_wr4000n40_ee", id=40004001, xsecs={13.6: Number(2.435e-03)},)
lrsm_wr4000n40_em = lrsm_wr4000n40.add_process(name="lrsm_wr4000n40_em", id=40004002, xsecs={13.6: Number(2.435e-03)},)
lrsm_wr4000n40_me = lrsm_wr4000n40.add_process(name="lrsm_wr4000n40_me", id=40004003, xsecs={13.6: Number(2.435e-03)},)
lrsm_wr4000n40_mm = lrsm_wr4000n40.add_process(name="lrsm_wr4000n40_mm", id=40004004, xsecs={13.6: Number(2.435e-03)},)

lrsm_wr4000n50 = Process(name="lrsm_wr4000n50", id=400050, label="$W_R$(4000)N(50)", xsecs={13.6: Number(2.457e-03)},)
lrsm_wr4000n50_ee = lrsm_wr4000n50.add_process(name="lrsm_wr4000n50_ee", id=40005001, xsecs={13.6: Number(2.457e-03)},)
lrsm_wr4000n50_em = lrsm_wr4000n50.add_process(name="lrsm_wr4000n50_em", id=40005002, xsecs={13.6: Number(2.457e-03)},)
lrsm_wr4000n50_me = lrsm_wr4000n50.add_process(name="lrsm_wr4000n50_me", id=40005003, xsecs={13.6: Number(2.457e-03)},)
lrsm_wr4000n50_mm = lrsm_wr4000n50.add_process(name="lrsm_wr4000n50_mm", id=40005004, xsecs={13.6: Number(2.457e-03)},)

lrsm_wr4000n60 = Process(name="lrsm_wr4000n60", id=400060, label="$W_R$(4000)N(60)", xsecs={13.6: Number(2.450e-03)},)
lrsm_wr4000n60_ee = lrsm_wr4000n60.add_process(name="lrsm_wr4000n60_ee", id=40006001, xsecs={13.6: Number(2.450e-03)},)
lrsm_wr4000n60_em = lrsm_wr4000n60.add_process(name="lrsm_wr4000n60_em", id=40006002, xsecs={13.6: Number(2.450e-03)},)
lrsm_wr4000n60_me = lrsm_wr4000n60.add_process(name="lrsm_wr4000n60_me", id=40006003, xsecs={13.6: Number(2.450e-03)},)
lrsm_wr4000n60_mm = lrsm_wr4000n60.add_process(name="lrsm_wr4000n60_mm", id=40006004, xsecs={13.6: Number(2.450e-03)},)

lrsm_wr4000n70 = Process(name="lrsm_wr4000n70", id=400070, label="$W_R$(4000)N(70)", xsecs={13.6: Number(2.425e-03)},)
lrsm_wr4000n70_ee = lrsm_wr4000n70.add_process(name="lrsm_wr4000n70_ee", id=40007001, xsecs={13.6: Number(2.425e-03)},)
lrsm_wr4000n70_em = lrsm_wr4000n70.add_process(name="lrsm_wr4000n70_em", id=40007002, xsecs={13.6: Number(2.425e-03)},)
lrsm_wr4000n70_me = lrsm_wr4000n70.add_process(name="lrsm_wr4000n70_me", id=40007003, xsecs={13.6: Number(2.425e-03)},)
lrsm_wr4000n70_mm = lrsm_wr4000n70.add_process(name="lrsm_wr4000n70_mm", id=40007004, xsecs={13.6: Number(2.425e-03)},)

lrsm_wr4000n80 = Process(name="lrsm_wr4000n80", id=400080, label="$W_R$(4000)N(80)", xsecs={13.6: Number(2.398e-03)},)
lrsm_wr4000n80_ee = lrsm_wr4000n80.add_process(name="lrsm_wr4000n80_ee", id=40008001, xsecs={13.6: Number(2.398e-03)},)
lrsm_wr4000n80_em = lrsm_wr4000n80.add_process(name="lrsm_wr4000n80_em", id=40008002, xsecs={13.6: Number(2.398e-03)},)
lrsm_wr4000n80_me = lrsm_wr4000n80.add_process(name="lrsm_wr4000n80_me", id=40008003, xsecs={13.6: Number(2.398e-03)},)
lrsm_wr4000n80_mm = lrsm_wr4000n80.add_process(name="lrsm_wr4000n80_mm", id=40008004, xsecs={13.6: Number(2.398e-03)},)

lrsm_wr4000n90 = Process(name="lrsm_wr4000n90", id=400090, label="$W_R$(4000)N(90)", xsecs={13.6: Number(2.400e-03)},)
lrsm_wr4000n90_ee = lrsm_wr4000n90.add_process(name="lrsm_wr4000n90_ee", id=40009001, xsecs={13.6: Number(2.400e-03)},)
lrsm_wr4000n90_em = lrsm_wr4000n90.add_process(name="lrsm_wr4000n90_em", id=40009002, xsecs={13.6: Number(2.400e-03)},)
lrsm_wr4000n90_me = lrsm_wr4000n90.add_process(name="lrsm_wr4000n90_me", id=40009003, xsecs={13.6: Number(2.400e-03)},)
lrsm_wr4000n90_mm = lrsm_wr4000n90.add_process(name="lrsm_wr4000n90_mm", id=40009004, xsecs={13.6: Number(2.400e-03)},)

lrsm_wr4000n100 = Process(name="lrsm_wr4000n100", id=4000100, label="$W_R$(4000)N(100)", xsecs={13.6: Number(2.354e-03)},)
lrsm_wr4000n100_ee = lrsm_wr4000n100.add_process(name="lrsm_wr4000n100_ee", id=400010001, xsecs={13.6: Number(2.354e-03)},)
lrsm_wr4000n100_em = lrsm_wr4000n100.add_process(name="lrsm_wr4000n100_em", id=400010002, xsecs={13.6: Number(2.354e-03)},)
lrsm_wr4000n100_me = lrsm_wr4000n100.add_process(name="lrsm_wr4000n100_me", id=400010003, xsecs={13.6: Number(2.354e-03)},)
lrsm_wr4000n100_mm = lrsm_wr4000n100.add_process(name="lrsm_wr4000n100_mm", id=400010004, xsecs={13.6: Number(2.354e-03)},)


# WR(5000)

lrsm_wr5000n10 = Process(name="lrsm_wr5000n10", id=500010, label="$W_R$(5000)N(10)", xsecs={13.6: Number(6.778e-04)},)
lrsm_wr5000n10_ee = lrsm_wr5000n10.add_process(name="lrsm_wr5000n10_ee", id=50001001, xsecs={13.6: Number(6.778e-04)},)
lrsm_wr5000n10_em = lrsm_wr5000n10.add_process(name="lrsm_wr5000n10_em", id=50001002, xsecs={13.6: Number(6.778e-04)},)
lrsm_wr5000n10_me = lrsm_wr5000n10.add_process(name="lrsm_wr5000n10_me", id=50001003, xsecs={13.6: Number(6.778e-04)},)
lrsm_wr5000n10_mm = lrsm_wr5000n10.add_process(name="lrsm_wr5000n10_mm", id=50001004, xsecs={13.6: Number(6.778e-04)},)

lrsm_wr5000n20 = Process(name="lrsm_wr5000n20", id=500020, label="$W_R$(5000)N(20)", xsecs={13.6: Number(6.818e-04)},)
lrsm_wr5000n20_ee = lrsm_wr5000n20.add_process(name="lrsm_wr5000n20_ee", id=50002001, xsecs={13.6: Number(6.818e-04)},)
lrsm_wr5000n20_em = lrsm_wr5000n20.add_process(name="lrsm_wr5000n20_em", id=50002002, xsecs={13.6: Number(6.818e-04)},)
lrsm_wr5000n20_me = lrsm_wr5000n20.add_process(name="lrsm_wr5000n20_me", id=50002003, xsecs={13.6: Number(6.818e-04)},)
lrsm_wr5000n20_mm = lrsm_wr5000n20.add_process(name="lrsm_wr5000n20_mm", id=50002004, xsecs={13.6: Number(6.818e-04)},)


# lrsm_wr5000n30 = Process(name="lrsm_wr5000n30", id=500030, label="$W_R$(5000)N(30)", xsecs={13.6: Number(6.782e-04)},)
# lrsm_wr5000n40 = Process(name="lrsm_wr5000n40", id=500040, label="$W_R$(5000)N(40)", xsecs={13.6: Number(6.650e-04)},)
# lrsm_wr5000n50 = Process(name="lrsm_wr5000n50", id=500050, label="$W_R$(5000)N(50)", xsecs={13.6: Number(6.586e-04)},)
# lrsm_wr5000n60 = Process(name="lrsm_wr5000n60", id=500060, label="$W_R$(5000)N(60)", xsecs={13.6: Number(6.538e-04)},)
# lrsm_wr5000n70 = Process(name="lrsm_wr5000n70", id=500070, label="$W_R$(5000)N(70)", xsecs={13.6: Number(6.487e-04)},)
# lrsm_wr5000n80 = Process(name="lrsm_wr5000n80", id=500080, label="$W_R$(5000)N(80)", xsecs={13.6: Number(6.403e-04)},)
# lrsm_wr5000n90 = Process(name="lrsm_wr5000n90", id=500090, label="$W_R$(5000)N(90)", xsecs={13.6: Number(6.364e-04)},)
# lrsm_wr5000n100 = Process(name="lrsm_wr5000n100", id=5000100, label="$W_R$(5000)N(100)", xsecs={13.6: Number(6.235e-04)},)
lrsm_wr5000n30 = Process(name="lrsm_wr5000n30", id=500030, label="$W_R$(5000)N(30)", xsecs={13.6: Number(6.782e-04)},)
lrsm_wr5000n30_ee = lrsm_wr5000n30.add_process(name="lrsm_wr5000n30_ee", id=50003001, xsecs={13.6: Number(6.782e-04)})
lrsm_wr5000n30_em = lrsm_wr5000n30.add_process(name="lrsm_wr5000n30_em", id=50003002, xsecs={13.6: Number(6.782e-04)})
lrsm_wr5000n30_me = lrsm_wr5000n30.add_process(name="lrsm_wr5000n30_me", id=50003003, xsecs={13.6: Number(6.782e-04)})
lrsm_wr5000n30_mm = lrsm_wr5000n30.add_process(name="lrsm_wr5000n30_mm", id=50003004, xsecs={13.6: Number(6.782e-04)})

lrsm_wr5000n40 = Process(name="lrsm_wr5000n40", id=500040, label="$W_R$(5000)N(40)", xsecs={13.6: Number(6.650e-04)},)
lrsm_wr5000n40_ee = lrsm_wr5000n40.add_process(name="lrsm_wr5000n40_ee", id=50004001, xsecs={13.6: Number(6.650e-04)})
lrsm_wr5000n40_em = lrsm_wr5000n40.add_process(name="lrsm_wr5000n40_em", id=50004002, xsecs={13.6: Number(6.650e-04)})
lrsm_wr5000n40_me = lrsm_wr5000n40.add_process(name="lrsm_wr5000n40_me", id=50004003, xsecs={13.6: Number(6.650e-04)})
lrsm_wr5000n40_mm = lrsm_wr5000n40.add_process(name="lrsm_wr5000n40_mm", id=50004004, xsecs={13.6: Number(6.650e-04)})

lrsm_wr5000n50 = Process(name="lrsm_wr5000n50", id=500050, label="$W_R$(5000)N(50)", xsecs={13.6: Number(6.586e-04)},)
lrsm_wr5000n50_ee = lrsm_wr5000n50.add_process(name="lrsm_wr5000n50_ee", id=50005001, xsecs={13.6: Number(6.586e-04)})
lrsm_wr5000n50_em = lrsm_wr5000n50.add_process(name="lrsm_wr5000n50_em", id=50005002, xsecs={13.6: Number(6.586e-04)})
lrsm_wr5000n50_me = lrsm_wr5000n50.add_process(name="lrsm_wr5000n50_me", id=50005003, xsecs={13.6: Number(6.586e-04)})
lrsm_wr5000n50_mm = lrsm_wr5000n50.add_process(name="lrsm_wr5000n50_mm", id=50005004, xsecs={13.6: Number(6.586e-04)})

lrsm_wr5000n60 = Process(name="lrsm_wr5000n60", id=500060, label="$W_R$(5000)N(60)", xsecs={13.6: Number(6.538e-04)},)
lrsm_wr5000n60_ee = lrsm_wr5000n60.add_process(name="lrsm_wr5000n60_ee", id=50006001, xsecs={13.6: Number(6.538e-04)})
lrsm_wr5000n60_em = lrsm_wr5000n60.add_process(name="lrsm_wr5000n60_em", id=50006002, xsecs={13.6: Number(6.538e-04)})
lrsm_wr5000n60_me = lrsm_wr5000n60.add_process(name="lrsm_wr5000n60_me", id=50006003, xsecs={13.6: Number(6.538e-04)})
lrsm_wr5000n60_mm = lrsm_wr5000n60.add_process(name="lrsm_wr5000n60_mm", id=50006004, xsecs={13.6: Number(6.538e-04)})

lrsm_wr5000n70 = Process(name="lrsm_wr5000n70", id=500070, label="$W_R$(5000)N(70)", xsecs={13.6: Number(6.487e-04)},)
lrsm_wr5000n70_ee = lrsm_wr5000n70.add_process(name="lrsm_wr5000n70_ee", id=50007001, xsecs={13.6: Number(6.487e-04)})
lrsm_wr5000n70_em = lrsm_wr5000n70.add_process(name="lrsm_wr5000n70_em", id=50007002, xsecs={13.6: Number(6.487e-04)})
lrsm_wr5000n70_me = lrsm_wr5000n70.add_process(name="lrsm_wr5000n70_me", id=50007003, xsecs={13.6: Number(6.487e-04)})
lrsm_wr5000n70_mm = lrsm_wr5000n70.add_process(name="lrsm_wr5000n70_mm", id=50007004, xsecs={13.6: Number(6.487e-04)})

lrsm_wr5000n80 = Process(name="lrsm_wr5000n80", id=500080, label="$W_R$(5000)N(80)", xsecs={13.6: Number(6.403e-04)},)
lrsm_wr5000n80_ee = lrsm_wr5000n80.add_process(name="lrsm_wr5000n80_ee", id=50008001, xsecs={13.6: Number(6.403e-04)})
lrsm_wr5000n80_em = lrsm_wr5000n80.add_process(name="lrsm_wr5000n80_em", id=50008002, xsecs={13.6: Number(6.403e-04)})
lrsm_wr5000n80_me = lrsm_wr5000n80.add_process(name="lrsm_wr5000n80_me", id=50008003, xsecs={13.6: Number(6.403e-04)})
lrsm_wr5000n80_mm = lrsm_wr5000n80.add_process(name="lrsm_wr5000n80_mm", id=50008004, xsecs={13.6: Number(6.403e-04)})

lrsm_wr5000n90 = Process(name="lrsm_wr5000n90", id=500090, label="$W_R$(5000)N(90)", xsecs={13.6: Number(6.364e-04)},)
lrsm_wr5000n90_ee = lrsm_wr5000n90.add_process(name="lrsm_wr5000n90_ee", id=50009001, xsecs={13.6: Number(6.364e-04)})
lrsm_wr5000n90_em = lrsm_wr5000n90.add_process(name="lrsm_wr5000n90_em", id=50009002, xsecs={13.6: Number(6.364e-04)})
lrsm_wr5000n90_me = lrsm_wr5000n90.add_process(name="lrsm_wr5000n90_me", id=50009003, xsecs={13.6: Number(6.364e-04)})
lrsm_wr5000n90_mm = lrsm_wr5000n90.add_process(name="lrsm_wr5000n90_mm", id=50009004, xsecs={13.6: Number(6.364e-04)})

lrsm_wr5000n100 = Process(name="lrsm_wr5000n100", id=5000100, label="$W_R$(5000)N(100)", xsecs={13.6: Number(6.235e-04)},)
lrsm_wr5000n100_ee = lrsm_wr5000n100.add_process(name="lrsm_wr5000n100_ee", id=500010001, xsecs={13.6: Number(6.235e-04)})
lrsm_wr5000n100_em = lrsm_wr5000n100.add_process(name="lrsm_wr5000n100_em", id=500010002, xsecs={13.6: Number(6.235e-04)})
lrsm_wr5000n100_me = lrsm_wr5000n100.add_process(name="lrsm_wr5000n100_me", id=500010003, xsecs={13.6: Number(6.235e-04)})
lrsm_wr5000n100_mm = lrsm_wr5000n100.add_process(name="lrsm_wr5000n100_mm", id=500010004, xsecs={13.6: Number(6.235e-04)})


# lrsm_wr6000n10 = Process(name="lrsm_wr6000n10", id=600010, label="$W_R$(6000)N(10)", xsecs={13.6: Number(2.546e-04)},)
# lrsm_wr6000n20 = Process(name="lrsm_wr6000n20", id=600020, label="$W_R$(6000)N(20)", xsecs={13.6: Number(2.559e-04)},)
# lrsm_wr6000n30 = Process(name="lrsm_wr6000n30", id=600030, label="$W_R$(6000)N(30)", xsecs={13.6: Number(2.546e-04)},)
# lrsm_wr6000n40 = Process(name="lrsm_wr6000n40", id=600040, label="$W_R$(6000)N(40)", xsecs={13.6: Number(2.516e-04)},)
# lrsm_wr6000n50 = Process(name="lrsm_wr6000n50", id=600050, label="$W_R$(6000)N(50)", xsecs={13.6: Number(2.469e-04)},)
# lrsm_wr6000n60 = Process(name="lrsm_wr6000n60", id=600060, label="$W_R$(6000)N(60)", xsecs={13.6: Number(2.430e-04)},)
# lrsm_wr6000n70 = Process(name="lrsm_wr6000n70", id=600070, label="$W_R$(6000)N(70)", xsecs={13.6: Number(2.401e-04)},)
# lrsm_wr6000n80 = Process(name="lrsm_wr6000n80", id=600080, label="$W_R$(6000)N(80)", xsecs={13.6: Number(2.374e-04)},)
# lrsm_wr6000n90 = Process(name="lrsm_wr6000n90", id=600090, label="$W_R$(6000)N(90)", xsecs={13.6: Number(2.340e-04)},)
# lrsm_wr6000n100 = Process(name="lrsm_wr6000n100", id=6000100, label="$W_R$(6000)N(100)", xsecs={13.6: Number(2.309e-04)},)
lrsm_wr6000n10 = Process(name="lrsm_wr6000n10", id=600010, label="$W_R$(6000)N(10)", xsecs={13.6: Number(2.546e-04)},)
lrsm_wr6000n10_ee = lrsm_wr6000n10.add_process(name="lrsm_wr6000n10_ee", id=60001001, xsecs={13.6: Number(2.546e-04)})
lrsm_wr6000n10_em = lrsm_wr6000n10.add_process(name="lrsm_wr6000n10_em", id=60001002, xsecs={13.6: Number(2.546e-04)})
lrsm_wr6000n10_me = lrsm_wr6000n10.add_process(name="lrsm_wr6000n10_me", id=60001003, xsecs={13.6: Number(2.546e-04)})
lrsm_wr6000n10_mm = lrsm_wr6000n10.add_process(name="lrsm_wr6000n10_mm", id=60001004, xsecs={13.6: Number(2.546e-04)})

lrsm_wr6000n20 = Process(name="lrsm_wr6000n20", id=600020, label="$W_R$(6000)N(20)", xsecs={13.6: Number(2.559e-04)},)
lrsm_wr6000n20_ee = lrsm_wr6000n20.add_process(name="lrsm_wr6000n20_ee", id=60002001, xsecs={13.6: Number(2.559e-04)})
lrsm_wr6000n20_em = lrsm_wr6000n20.add_process(name="lrsm_wr6000n20_em", id=60002002, xsecs={13.6: Number(2.559e-04)})
lrsm_wr6000n20_me = lrsm_wr6000n20.add_process(name="lrsm_wr6000n20_me", id=60002003, xsecs={13.6: Number(2.559e-04)})
lrsm_wr6000n20_mm = lrsm_wr6000n20.add_process(name="lrsm_wr6000n20_mm", id=60002004, xsecs={13.6: Number(2.559e-04)})

lrsm_wr6000n30 = Process(name="lrsm_wr6000n30", id=600030, label="$W_R$(6000)N(30)", xsecs={13.6: Number(2.546e-04)},)
lrsm_wr6000n30_ee = lrsm_wr6000n30.add_process(name="lrsm_wr6000n30_ee", id=60003001, xsecs={13.6: Number(2.546e-04)})
lrsm_wr6000n30_em = lrsm_wr6000n30.add_process(name="lrsm_wr6000n30_em", id=60003002, xsecs={13.6: Number(2.546e-04)})
lrsm_wr6000n30_me = lrsm_wr6000n30.add_process(name="lrsm_wr6000n30_me", id=60003003, xsecs={13.6: Number(2.546e-04)})
lrsm_wr6000n30_mm = lrsm_wr6000n30.add_process(name="lrsm_wr6000n30_mm", id=60003004, xsecs={13.6: Number(2.546e-04)})

lrsm_wr6000n40 = Process(name="lrsm_wr6000n40", id=600040, label="$W_R$(6000)N(40)", xsecs={13.6: Number(2.516e-04)},)
lrsm_wr6000n40_ee = lrsm_wr6000n40.add_process(name="lrsm_wr6000n40_ee", id=60004001, xsecs={13.6: Number(2.516e-04)})
lrsm_wr6000n40_em = lrsm_wr6000n40.add_process(name="lrsm_wr6000n40_em", id=60004002, xsecs={13.6: Number(2.516e-04)})
lrsm_wr6000n40_me = lrsm_wr6000n40.add_process(name="lrsm_wr6000n40_me", id=60004003, xsecs={13.6: Number(2.516e-04)})
lrsm_wr6000n40_mm = lrsm_wr6000n40.add_process(name="lrsm_wr6000n40_mm", id=60004004, xsecs={13.6: Number(2.516e-04)})

lrsm_wr6000n50 = Process(name="lrsm_wr6000n50", id=600050, label="$W_R$(6000)N(50)", xsecs={13.6: Number(2.469e-04)},)
lrsm_wr6000n50_ee = lrsm_wr6000n50.add_process(name="lrsm_wr6000n50_ee", id=60005001, xsecs={13.6: Number(2.469e-04)})
lrsm_wr6000n50_em = lrsm_wr6000n50.add_process(name="lrsm_wr6000n50_em", id=60005002, xsecs={13.6: Number(2.469e-04)})
lrsm_wr6000n50_me = lrsm_wr6000n50.add_process(name="lrsm_wr6000n50_me", id=60005003, xsecs={13.6: Number(2.469e-04)})
lrsm_wr6000n50_mm = lrsm_wr6000n50.add_process(name="lrsm_wr6000n50_mm", id=60005004, xsecs={13.6: Number(2.469e-04)})

lrsm_wr6000n60 = Process(name="lrsm_wr6000n60", id=600060, label="$W_R$(6000)N(60)", xsecs={13.6: Number(2.430e-04)},)
lrsm_wr6000n60_ee = lrsm_wr6000n60.add_process(name="lrsm_wr6000n60_ee", id=60006001, xsecs={13.6: Number(2.430e-04)})
lrsm_wr6000n60_em = lrsm_wr6000n60.add_process(name="lrsm_wr6000n60_em", id=60006002, xsecs={13.6: Number(2.430e-04)})
lrsm_wr6000n60_me = lrsm_wr6000n60.add_process(name="lrsm_wr6000n60_me", id=60006003, xsecs={13.6: Number(2.430e-04)})
lrsm_wr6000n60_mm = lrsm_wr6000n60.add_process(name="lrsm_wr6000n60_mm", id=60006004, xsecs={13.6: Number(2.430e-04)})

lrsm_wr6000n70 = Process(name="lrsm_wr6000n70", id=600070, label="$W_R$(6000)N(70)", xsecs={13.6: Number(2.401e-04)},)
lrsm_wr6000n70_ee = lrsm_wr6000n70.add_process(name="lrsm_wr6000n70_ee", id=60007001, xsecs={13.6: Number(2.401e-04)})
lrsm_wr6000n70_em = lrsm_wr6000n70.add_process(name="lrsm_wr6000n70_em", id=60007002, xsecs={13.6: Number(2.401e-04)})
lrsm_wr6000n70_me = lrsm_wr6000n70.add_process(name="lrsm_wr6000n70_me", id=60007003, xsecs={13.6: Number(2.401e-04)})
lrsm_wr6000n70_mm = lrsm_wr6000n70.add_process(name="lrsm_wr6000n70_mm", id=60007004, xsecs={13.6: Number(2.401e-04)})

lrsm_wr6000n80 = Process(name="lrsm_wr6000n80", id=600080, label="$W_R$(6000)N(80)", xsecs={13.6: Number(2.374e-04)},)
lrsm_wr6000n80_ee = lrsm_wr6000n80.add_process(name="lrsm_wr6000n80_ee", id=60008001, xsecs={13.6: Number(2.374e-04)})
lrsm_wr6000n80_em = lrsm_wr6000n80.add_process(name="lrsm_wr6000n80_em", id=60008002, xsecs={13.6: Number(2.374e-04)})
lrsm_wr6000n80_me = lrsm_wr6000n80.add_process(name="lrsm_wr6000n80_me", id=60008003, xsecs={13.6: Number(2.374e-04)})
lrsm_wr6000n80_mm = lrsm_wr6000n80.add_process(name="lrsm_wr6000n80_mm", id=60008004, xsecs={13.6: Number(2.374e-04)})

lrsm_wr6000n90 = Process(name="lrsm_wr6000n90", id=600090, label="$W_R$(6000)N(90)", xsecs={13.6: Number(2.340e-04)},)
lrsm_wr6000n90_ee = lrsm_wr6000n90.add_process(name="lrsm_wr6000n90_ee", id=60009001, xsecs={13.6: Number(2.340e-04)})
lrsm_wr6000n90_em = lrsm_wr6000n90.add_process(name="lrsm_wr6000n90_em", id=60009002, xsecs={13.6: Number(2.340e-04)})
lrsm_wr6000n90_me = lrsm_wr6000n90.add_process(name="lrsm_wr6000n90_me", id=60009003, xsecs={13.6: Number(2.340e-04)})
lrsm_wr6000n90_mm = lrsm_wr6000n90.add_process(name="lrsm_wr6000n90_mm", id=60009004, xsecs={13.6: Number(2.340e-04)})

lrsm_wr6000n100 = Process(name="lrsm_wr6000n100", id=6000100, label="$W_R$(6000)N(100)", xsecs={13.6: Number(2.309e-04)},)
lrsm_wr6000n100_ee = lrsm_wr6000n100.add_process(name="lrsm_wr6000n100_ee", id=600010001, xsecs={13.6: Number(2.309e-04)})
lrsm_wr6000n100_em = lrsm_wr6000n100.add_process(name="lrsm_wr6000n100_em", id=600010002, xsecs={13.6: Number(2.309e-04)})
lrsm_wr6000n100_me = lrsm_wr6000n100.add_process(name="lrsm_wr6000n100_me", id=600010003, xsecs={13.6: Number(2.309e-04)})
lrsm_wr6000n100_mm = lrsm_wr6000n100.add_process(name="lrsm_wr6000n100_mm", id=600010004, xsecs={13.6: Number(2.309e-04)})


# lrsm_wr7000n10 = Process(name="lrsm_wr7000n10", id=700010, label="$W_R$(7000)N(10)", xsecs={13.6: Number(1.209e-04)},)
# lrsm_wr7000n20 = Process(name="lrsm_wr7000n20", id=700020, label="$W_R$(7000)N(20)", xsecs={13.6: Number(1.180e-04)},)
# lrsm_wr7000n30 = Process(name="lrsm_wr7000n30", id=700030, label="$W_R$(7000)N(30)", xsecs={13.6: Number(1.175e-04)},)
# lrsm_wr7000n40 = Process(name="lrsm_wr7000n40", id=700040, label="$W_R$(7000)N(40)", xsecs={13.6: Number(1.156e-04)},)
# lrsm_wr7000n50 = Process(name="lrsm_wr7000n50", id=700050, label="$W_R$(7000)N(50)", xsecs={13.6: Number(1.140e-04)},)
# lrsm_wr7000n60 = Process(name="lrsm_wr7000n60", id=700060, label="$W_R$(7000)N(60)", xsecs={13.6: Number(1.128e-04)},)
# lrsm_wr7000n70 = Process(name="lrsm_wr7000n70", id=700070, label="$W_R$(7000)N(70)", xsecs={13.6: Number(1.111e-04)},)
# lrsm_wr7000n80 = Process(name="lrsm_wr7000n80", id=700080, label="$W_R$(7000)N(80)", xsecs={13.6: Number(1.089e-04)},)
# lrsm_wr7000n90 = Process(name="lrsm_wr7000n90", id=700090, label="$W_R$(7000)N(90)", xsecs={13.6: Number(1.078e-04)},)
# lrsm_wr7000n100 = Process(name="lrsm_wr7000n100", id=7000100, label="$W_R$(7000)N(100)", xsecs={13.6: Number(1.057e-04)},)
lrsm_wr7000n10 = Process(name="lrsm_wr7000n10", id=700010, label="$W_R$(7000)N(10)", xsecs={13.6: Number(1.209e-04)},)
lrsm_wr7000n10_ee = lrsm_wr7000n10.add_process(name="lrsm_wr7000n10_ee", id=70001001, xsecs={13.6: Number(1.209e-04)})
lrsm_wr7000n10_em = lrsm_wr7000n10.add_process(name="lrsm_wr7000n10_em", id=70001002, xsecs={13.6: Number(1.209e-04)})
lrsm_wr7000n10_me = lrsm_wr7000n10.add_process(name="lrsm_wr7000n10_me", id=70001003, xsecs={13.6: Number(1.209e-04)})
lrsm_wr7000n10_mm = lrsm_wr7000n10.add_process(name="lrsm_wr7000n10_mm", id=70001004, xsecs={13.6: Number(1.209e-04)})

lrsm_wr7000n20 = Process(name="lrsm_wr7000n20", id=700020, label="$W_R$(7000)N(20)", xsecs={13.6: Number(1.180e-04)},)
lrsm_wr7000n20_ee = lrsm_wr7000n20.add_process(name="lrsm_wr7000n20_ee", id=70002001, xsecs={13.6: Number(1.180e-04)})
lrsm_wr7000n20_em = lrsm_wr7000n20.add_process(name="lrsm_wr7000n20_em", id=70002002, xsecs={13.6: Number(1.180e-04)})
lrsm_wr7000n20_me = lrsm_wr7000n20.add_process(name="lrsm_wr7000n20_me", id=70002003, xsecs={13.6: Number(1.180e-04)})
lrsm_wr7000n20_mm = lrsm_wr7000n20.add_process(name="lrsm_wr7000n20_mm", id=70002004, xsecs={13.6: Number(1.180e-04)})

lrsm_wr7000n30 = Process(name="lrsm_wr7000n30", id=700030, label="$W_R$(7000)N(30)", xsecs={13.6: Number(1.175e-04)},)
lrsm_wr7000n30_ee = lrsm_wr7000n30.add_process(name="lrsm_wr7000n30_ee", id=70003001, xsecs={13.6: Number(1.175e-04)})
lrsm_wr7000n30_em = lrsm_wr7000n30.add_process(name="lrsm_wr7000n30_em", id=70003002, xsecs={13.6: Number(1.175e-04)})
lrsm_wr7000n30_me = lrsm_wr7000n30.add_process(name="lrsm_wr7000n30_me", id=70003003, xsecs={13.6: Number(1.175e-04)})
lrsm_wr7000n30_mm = lrsm_wr7000n30.add_process(name="lrsm_wr7000n30_mm", id=70003004, xsecs={13.6: Number(1.175e-04)})

lrsm_wr7000n40 = Process(name="lrsm_wr7000n40", id=700040, label="$W_R$(7000)N(40)", xsecs={13.6: Number(1.156e-04)},)
lrsm_wr7000n40_ee = lrsm_wr7000n40.add_process(name="lrsm_wr7000n40_ee", id=70004001, xsecs={13.6: Number(1.156e-04)})
lrsm_wr7000n40_em = lrsm_wr7000n40.add_process(name="lrsm_wr7000n40_em", id=70004002, xsecs={13.6: Number(1.156e-04)})
lrsm_wr7000n40_me = lrsm_wr7000n40.add_process(name="lrsm_wr7000n40_me", id=70004003, xsecs={13.6: Number(1.156e-04)})
lrsm_wr7000n40_mm = lrsm_wr7000n40.add_process(name="lrsm_wr7000n40_mm", id=70004004, xsecs={13.6: Number(1.156e-04)})

lrsm_wr7000n50 = Process(name="lrsm_wr7000n50", id=700050, label="$W_R$(7000)N(50)", xsecs={13.6: Number(1.140e-04)},)
lrsm_wr7000n50_ee = lrsm_wr7000n50.add_process(name="lrsm_wr7000n50_ee", id=70005001, xsecs={13.6: Number(1.140e-04)})
lrsm_wr7000n50_em = lrsm_wr7000n50.add_process(name="lrsm_wr7000n50_em", id=70005002, xsecs={13.6: Number(1.140e-04)})
lrsm_wr7000n50_me = lrsm_wr7000n50.add_process(name="lrsm_wr7000n50_me", id=70005003, xsecs={13.6: Number(1.140e-04)})
lrsm_wr7000n50_mm = lrsm_wr7000n50.add_process(name="lrsm_wr7000n50_mm", id=70005004, xsecs={13.6: Number(1.140e-04)})

lrsm_wr7000n60 = Process(name="lrsm_wr7000n60", id=700060, label="$W_R$(7000)N(60)", xsecs={13.6: Number(1.128e-04)},)
lrsm_wr7000n60_ee = lrsm_wr7000n60.add_process(name="lrsm_wr7000n60_ee", id=70006001, xsecs={13.6: Number(1.128e-04)})
lrsm_wr7000n60_em = lrsm_wr7000n60.add_process(name="lrsm_wr7000n60_em", id=70006002, xsecs={13.6: Number(1.128e-04)})
lrsm_wr7000n60_me = lrsm_wr7000n60.add_process(name="lrsm_wr7000n60_me", id=70006003, xsecs={13.6: Number(1.128e-04)})
lrsm_wr7000n60_mm = lrsm_wr7000n60.add_process(name="lrsm_wr7000n60_mm", id=70006004, xsecs={13.6: Number(1.128e-04)})

lrsm_wr7000n70 = Process(name="lrsm_wr7000n70", id=700070, label="$W_R$(7000)N(70)", xsecs={13.6: Number(1.111e-04)},)
lrsm_wr7000n70_ee = lrsm_wr7000n70.add_process(name="lrsm_wr7000n70_ee", id=70007001, xsecs={13.6: Number(1.111e-04)})
lrsm_wr7000n70_em = lrsm_wr7000n70.add_process(name="lrsm_wr7000n70_em", id=70007002, xsecs={13.6: Number(1.111e-04)})
lrsm_wr7000n70_me = lrsm_wr7000n70.add_process(name="lrsm_wr7000n70_me", id=70007003, xsecs={13.6: Number(1.111e-04)})
lrsm_wr7000n70_mm = lrsm_wr7000n70.add_process(name="lrsm_wr7000n70_mm", id=70007004, xsecs={13.6: Number(1.111e-04)})

lrsm_wr7000n80 = Process(name="lrsm_wr7000n80", id=700080, label="$W_R$(7000)N(80)", xsecs={13.6: Number(1.089e-04)},)
lrsm_wr7000n80_ee = lrsm_wr7000n80.add_process(name="lrsm_wr7000n80_ee", id=70008001, xsecs={13.6: Number(1.089e-04)})
lrsm_wr7000n80_em = lrsm_wr7000n80.add_process(name="lrsm_wr7000n80_em", id=70008002, xsecs={13.6: Number(1.089e-04)})
lrsm_wr7000n80_me = lrsm_wr7000n80.add_process(name="lrsm_wr7000n80_me", id=70008003, xsecs={13.6: Number(1.089e-04)})
lrsm_wr7000n80_mm = lrsm_wr7000n80.add_process(name="lrsm_wr7000n80_mm", id=70008004, xsecs={13.6: Number(1.089e-04)})

lrsm_wr7000n90 = Process(name="lrsm_wr7000n90", id=700090, label="$W_R$(7000)N(90)", xsecs={13.6: Number(1.078e-04)},)
lrsm_wr7000n90_ee = lrsm_wr7000n90.add_process(name="lrsm_wr7000n90_ee", id=70009001, xsecs={13.6: Number(1.078e-04)})
lrsm_wr7000n90_em = lrsm_wr7000n90.add_process(name="lrsm_wr7000n90_em", id=70009002, xsecs={13.6: Number(1.078e-04)})
lrsm_wr7000n90_me = lrsm_wr7000n90.add_process(name="lrsm_wr7000n90_me", id=70009003, xsecs={13.6: Number(1.078e-04)})
lrsm_wr7000n90_mm = lrsm_wr7000n90.add_process(name="lrsm_wr7000n90_mm", id=70009004, xsecs={13.6: Number(1.078e-04)})

lrsm_wr7000n100 = Process(name="lrsm_wr7000n100", id=7000100, label="$W_R$(7000)N(100)", xsecs={13.6: Number(1.057e-04)},)
lrsm_wr7000n100_ee = lrsm_wr7000n100.add_process(name="lrsm_wr7000n100_ee", id=700010001, xsecs={13.6: Number(1.057e-04)})
lrsm_wr7000n100_em = lrsm_wr7000n100.add_process(name="lrsm_wr7000n100_em", id=700010002, xsecs={13.6: Number(1.057e-04)})
lrsm_wr7000n100_me = lrsm_wr7000n100.add_process(name="lrsm_wr7000n100_me", id=700010003, xsecs={13.6: Number(1.057e-04)})
lrsm_wr7000n100_mm = lrsm_wr7000n100.add_process(name="lrsm_wr7000n100_mm", id=700010004, xsecs={13.6: Number(1.057e-04)})


# lrsm_wr8000n10 = Process(name="lrsm_wr8000n10", id=800010, label="$W_R$(8000)N(10)", xsecs={13.6: Number(6.279e-05)},)
# lrsm_wr8000n20 = Process(name="lrsm_wr8000n20", id=800020, label="$W_R$(8000)N(20)", xsecs={13.6: Number(6.191e-05)},)
# lrsm_wr8000n30 = Process(name="lrsm_wr8000n30", id=800030, label="$W_R$(8000)N(30)", xsecs={13.6: Number(6.100e-05)},)
# lrsm_wr8000n40 = Process(name="lrsm_wr8000n40", id=800040, label="$W_R$(8000)N(40)", xsecs={13.6: Number(5.983e-05)},)
# lrsm_wr8000n50 = Process(name="lrsm_wr8000n50", id=800050, label="$W_R$(8000)N(50)", xsecs={13.6: Number(5.947e-05)},)
# lrsm_wr8000n60 = Process(name="lrsm_wr8000n60", id=800060, label="$W_R$(8000)N(60)", xsecs={13.6: Number(5.848e-05)},)
# lrsm_wr8000n70 = Process(name="lrsm_wr8000n70", id=800070, label="$W_R$(8000)N(70)", xsecs={13.6: Number(5.776e-05)},)
# lrsm_wr8000n80 = Process(name="lrsm_wr8000n80", id=800080, label="$W_R$(8000)N(80)", xsecs={13.6: Number(5.625e-05)},)
# lrsm_wr8000n90 = Process(name="lrsm_wr8000n90", id=800090, label="$W_R$(8000)N(90)", xsecs={13.6: Number(5.553e-05)},)
# lrsm_wr8000n100 = Process(name="lrsm_wr8000n100", id=8000100, label="$W_R$(8000)N(100)", xsecs={13.6: Number(5.520e-05)},)
lrsm_wr8000n10 = Process(name="lrsm_wr8000n10", id=800010, label="$W_R$(8000)N(10)", xsecs={13.6: Number(6.279e-05)},)
lrsm_wr8000n10_ee = lrsm_wr8000n10.add_process(name="lrsm_wr8000n10_ee", id=80001001, xsecs={13.6: Number(6.279e-05)})
lrsm_wr8000n10_em = lrsm_wr8000n10.add_process(name="lrsm_wr8000n10_em", id=80001002, xsecs={13.6: Number(6.279e-05)})
lrsm_wr8000n10_me = lrsm_wr8000n10.add_process(name="lrsm_wr8000n10_me", id=80001003, xsecs={13.6: Number(6.279e-05)})
lrsm_wr8000n10_mm = lrsm_wr8000n10.add_process(name="lrsm_wr8000n10_mm", id=80001004, xsecs={13.6: Number(6.279e-05)})

lrsm_wr8000n20 = Process(name="lrsm_wr8000n20", id=800020, label="$W_R$(8000)N(20)", xsecs={13.6: Number(6.191e-05)},)
lrsm_wr8000n20_ee = lrsm_wr8000n20.add_process(name="lrsm_wr8000n20_ee", id=80002001, xsecs={13.6: Number(6.191e-05)})
lrsm_wr8000n20_em = lrsm_wr8000n20.add_process(name="lrsm_wr8000n20_em", id=80002002, xsecs={13.6: Number(6.191e-05)})
lrsm_wr8000n20_me = lrsm_wr8000n20.add_process(name="lrsm_wr8000n20_me", id=80002003, xsecs={13.6: Number(6.191e-05)})
lrsm_wr8000n20_mm = lrsm_wr8000n20.add_process(name="lrsm_wr8000n20_mm", id=80002004, xsecs={13.6: Number(6.191e-05)})

lrsm_wr8000n30 = Process(name="lrsm_wr8000n30", id=800030, label="$W_R$(8000)N(30)", xsecs={13.6: Number(6.100e-05)},)
lrsm_wr8000n30_ee = lrsm_wr8000n30.add_process(name="lrsm_wr8000n30_ee", id=80003001, xsecs={13.6: Number(6.100e-05)})
lrsm_wr8000n30_em = lrsm_wr8000n30.add_process(name="lrsm_wr8000n30_em", id=80003002, xsecs={13.6: Number(6.100e-05)})
lrsm_wr8000n30_me = lrsm_wr8000n30.add_process(name="lrsm_wr8000n30_me", id=80003003, xsecs={13.6: Number(6.100e-05)})
lrsm_wr8000n30_mm = lrsm_wr8000n30.add_process(name="lrsm_wr8000n30_mm", id=80003004, xsecs={13.6: Number(6.100e-05)})

lrsm_wr8000n40 = Process(name="lrsm_wr8000n40", id=800040, label="$W_R$(8000)N(40)", xsecs={13.6: Number(5.983e-05)},)
lrsm_wr8000n40_ee = lrsm_wr8000n40.add_process(name="lrsm_wr8000n40_ee", id=80004001, xsecs={13.6: Number(5.983e-05)})
lrsm_wr8000n40_em = lrsm_wr8000n40.add_process(name="lrsm_wr8000n40_em", id=80004002, xsecs={13.6: Number(5.983e-05)})
lrsm_wr8000n40_me = lrsm_wr8000n40.add_process(name="lrsm_wr8000n40_me", id=80004003, xsecs={13.6: Number(5.983e-05)})
lrsm_wr8000n40_mm = lrsm_wr8000n40.add_process(name="lrsm_wr8000n40_mm", id=80004004, xsecs={13.6: Number(5.983e-05)})

lrsm_wr8000n50 = Process(name="lrsm_wr8000n50", id=800050, label="$W_R$(8000)N(50)", xsecs={13.6: Number(5.947e-05)},)
lrsm_wr8000n50_ee = lrsm_wr8000n50.add_process(name="lrsm_wr8000n50_ee", id=80005001, xsecs={13.6: Number(5.947e-05)})
lrsm_wr8000n50_em = lrsm_wr8000n50.add_process(name="lrsm_wr8000n50_em", id=80005002, xsecs={13.6: Number(5.947e-05)})
lrsm_wr8000n50_me = lrsm_wr8000n50.add_process(name="lrsm_wr8000n50_me", id=80005003, xsecs={13.6: Number(5.947e-05)})
lrsm_wr8000n50_mm = lrsm_wr8000n50.add_process(name="lrsm_wr8000n50_mm", id=80005004, xsecs={13.6: Number(5.947e-05)})

lrsm_wr8000n60 = Process(name="lrsm_wr8000n60", id=800060, label="$W_R$(8000)N(60)", xsecs={13.6: Number(5.848e-05)},)
lrsm_wr8000n60_ee = lrsm_wr8000n60.add_process(name="lrsm_wr8000n60_ee", id=80006001, xsecs={13.6: Number(5.848e-05)})
lrsm_wr8000n60_em = lrsm_wr8000n60.add_process(name="lrsm_wr8000n60_em", id=80006002, xsecs={13.6: Number(5.848e-05)})
lrsm_wr8000n60_me = lrsm_wr8000n60.add_process(name="lrsm_wr8000n60_me", id=80006003, xsecs={13.6: Number(5.848e-05)})
lrsm_wr8000n60_mm = lrsm_wr8000n60.add_process(name="lrsm_wr8000n60_mm", id=80006004, xsecs={13.6: Number(5.848e-05)})

lrsm_wr8000n70 = Process(name="lrsm_wr8000n70", id=800070, label="$W_R$(8000)N(70)", xsecs={13.6: Number(5.776e-05)},)
lrsm_wr8000n70_ee = lrsm_wr8000n70.add_process(name="lrsm_wr8000n70_ee", id=80007001, xsecs={13.6: Number(5.776e-05)})
lrsm_wr8000n70_em = lrsm_wr8000n70.add_process(name="lrsm_wr8000n70_em", id=80007002, xsecs={13.6: Number(5.776e-05)})
lrsm_wr8000n70_me = lrsm_wr8000n70.add_process(name="lrsm_wr8000n70_me", id=80007003, xsecs={13.6: Number(5.776e-05)})
lrsm_wr8000n70_mm = lrsm_wr8000n70.add_process(name="lrsm_wr8000n70_mm", id=80007004, xsecs={13.6: Number(5.776e-05)})

lrsm_wr8000n80 = Process(name="lrsm_wr8000n80", id=800080, label="$W_R$(8000)N(80)", xsecs={13.6: Number(5.625e-05)},)
lrsm_wr8000n80_ee = lrsm_wr8000n80.add_process(name="lrsm_wr8000n80_ee", id=80008001, xsecs={13.6: Number(5.625e-05)})
lrsm_wr8000n80_em = lrsm_wr8000n80.add_process(name="lrsm_wr8000n80_em", id=80008002, xsecs={13.6: Number(5.625e-05)})
lrsm_wr8000n80_me = lrsm_wr8000n80.add_process(name="lrsm_wr8000n80_me", id=80008003, xsecs={13.6: Number(5.625e-05)})
lrsm_wr8000n80_mm = lrsm_wr8000n80.add_process(name="lrsm_wr8000n80_mm", id=80008004, xsecs={13.6: Number(5.625e-05)})

lrsm_wr8000n90 = Process(name="lrsm_wr8000n90", id=800090, label="$W_R$(8000)N(90)", xsecs={13.6: Number(5.553e-05)},)
lrsm_wr8000n90_ee = lrsm_wr8000n90.add_process(name="lrsm_wr8000n90_ee", id=80009001, xsecs={13.6: Number(5.553e-05)})
lrsm_wr8000n90_em = lrsm_wr8000n90.add_process(name="lrsm_wr8000n90_em", id=80009002, xsecs={13.6: Number(5.553e-05)})
lrsm_wr8000n90_me = lrsm_wr8000n90.add_process(name="lrsm_wr8000n90_me", id=80009003, xsecs={13.6: Number(5.553e-05)})
lrsm_wr8000n90_mm = lrsm_wr8000n90.add_process(name="lrsm_wr8000n90_mm", id=80009004, xsecs={13.6: Number(5.553e-05)})

lrsm_wr8000n100 = Process(name="lrsm_wr8000n100", id=8000100, label="$W_R$(8000)N(100)", xsecs={13.6: Number(5.520e-05)},)
lrsm_wr8000n100_ee = lrsm_wr8000n100.add_process(name="lrsm_wr8000n100_ee", id=800010001, xsecs={13.6: Number(5.520e-05)})
lrsm_wr8000n100_em = lrsm_wr8000n100.add_process(name="lrsm_wr8000n100_em", id=800010002, xsecs={13.6: Number(5.520e-05)})
lrsm_wr8000n100_me = lrsm_wr8000n100.add_process(name="lrsm_wr8000n100_me", id=800010003, xsecs={13.6: Number(5.520e-05)})
lrsm_wr8000n100_mm = lrsm_wr8000n100.add_process(name="lrsm_wr8000n100_mm", id=800010004, xsecs={13.6: Number(5.520e-05)})
