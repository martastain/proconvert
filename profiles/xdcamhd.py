from .common import *

"""
XDCAM HD
========

Tags
----

 - xd54 – 720p24 50Mb/s CBR
 - xd55 – 720p25 50Mb/s CBR
 - xd59 – 720p60 50Mb/s CBR
 - xd5a – 720p50 50Mb/s CBR
 - xd5b – 1080i60 50Mb/s CBR
 - xd5c – 1080i50 50Mb/s CBR
 - xd5d – 1080p24 50Mb/s CBR
 - xd5e – 1080p25 50Mb/s CBR
 - xd5f – 1080p30 50Mb/s CBR

"""

class XDCAMHD(EncoderProfile):
    name = "XDCAM HD"
    profiles = {
            "50-720p24" : {},
            "50-720p25" : {},
            "50-720p60" : {},
            "50-720p50" : {},
            "50-1080i60" : {},
            "50-1080i50" : {},
            "50-1080p24" : {},
            "50-1080p25" : {},
            "50-1080p30" : {},
        }
