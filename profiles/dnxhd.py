from .common import *

"""
DNxHD
=====

preset              width   height  interlace_flag      quality         Avid profile        Id
VC3_SQ_720p_TR      960     720     progressive         medium          Avid DNxHD 100      1258
VC3_SQ_720p         1280    720     progressive         medium          Avid DNxHD 145      1252
VC3_HQ_720p         1280    720     progressive         high            Avid DNxHD 220      1251
VC3_HQX_720p        1280    720     progressive         high extended   Avid DNxHD 220x     1250
VC3_LB_1080p        1920    1080    progressive         low             Avid DNxHD 36       1253
VC3_SQ_1080p_TR     1440    1080    progressive         medium          Avid DNxHD 100      1259
VC3_SQ_1080p        1920    1080    progressive         medium          Avid DNxHD 145      1237
VC3_HQ_1080p        1920    1080    progressive         high            Avid DNxHD 220      1238
VC3_HQX_1080p       1920    1080    progressive         high extended   Avid DNxHD 220x     1236
VC3_444_1080p       1920    1080    progressive         RGB 4:4:4       Avid DNxHD 444      1256
VC3_SQ_1080i_TR     1440    1080    top_first           medium          Avid DNxHD 100      1243
VC3_SQ_1080i        1920    1080    top_first           medium          Avid DNxHD 145      1244
VC3_HQ_1080i        1920    1080    top_first           high            Avid DNxHD 220      1242
VC3_HQX_1080i       1920    1080    top_first           high extended   Avid DNxHD 220x     1241
VC3_HQ_DCI_2K       2048    1080    progressive         high                                1272
VC3_HQX_DCI_2K      2048    1080    progressive         high extended                       1271
VC3_444_DCI_2K      2048    1080    progressive         RGB 4:4:4                           1270
VC3_HQ_DCI_4K       4096    2160    progressive         high                                1272
VC3_HQX_DCI_4K      4096    2160    progressive         high extended                       1271
VC3_444_DCI_4K      4096    2160    progressive         RGB 4:4:4                           1270
VC3_LB              any     any     progressive         low             Avid DNxHR LB       1274
VC3_SQ              any     any     progressive         medium          Avid DNxHR SQ       1273
VC3_HQ              any     any     progressive         high            Avid DNxHR HQ       1272
VC3_HQX             any     any     progressive         high extended   Avid DNxHR HQX      1271
VC3_444             any     any     progressive         RGB 4:4:4       Avid DNxHR 444      1270

"""

class DNXHD(EncoderFormat):
    name = "DNxHD"

