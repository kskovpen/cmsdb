# coding: utf-8

"""
LRSM process definitions.
"""

__all__ = [
    "lrsm_wr4000n20",
]


from order import Process
from scinum import Number

import cmsdb.constants as const

lrsm_wr4000n20 = Process(
    name="lrsm_wr4000n20",
    id=400020,
    label="$W_R$(4000)N(20)",
    xsecs={13.6: Number(0.1)},
)
