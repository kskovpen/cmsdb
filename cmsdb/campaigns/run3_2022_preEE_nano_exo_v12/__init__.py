# coding: utf-8

from order import Campaign


#
# campaign
#

campaign_run3_2022_preEE_nano_exo_v12 = Campaign(
    name="run3_2022_preEE_nano_exo_v12",
    id=320221201,  # 3 2022 12 01(u)
    ecm=13.6,
    bx=25,
    aux={
        "tier": "NanoAOD",
        "run": 3,
        "year": 2022,
        "version": 12,
        "postfix": "",
    },
    tags={"preEE"},
)


# trailing imports to load datasets
import cmsdb.campaigns.run3_2022_preEE_nano_exo_v12.ewk  # noqa
import cmsdb.campaigns.run3_2022_preEE_nano_exo_v12.lrsm  # noqa
