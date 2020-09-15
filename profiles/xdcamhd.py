__all__ = ["XDCAMHD"]

from .common import *

"""
XDCAM HD
========

Tags
----

### Class 18

### Class 25

### Class 35

### Class 50

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

CLASS_50 = {
    "b:v" : "50M"
}



class XDCAMHD(EncoderFormat):
    name = "XDCAM HD"
    profiles = {
            "50 (720p24)" :  {"tag" : "xd54", "fields" : 0},
            "50 (720p25)" :  {"tag" : "xd55", "fields" : 0},
            "50 (720p60)" :  {"tag" : "xd59", "fields" : 0},
            "50 (720p50)" :  {"tag" : "xd5a", "fields" : 0},
            "50 (1080i60)" : {"tag" : "xd5b", "fields" : 1},
            "50 (1080i50)" : {"tag" : "xd5c", "fields" : 1},
            "50 (1080p24)" : {"tag" : "xd5d", "fields" : 0},
            "50 (1080p25)" : {"tag" : "xd5e", "fields" : 0},
            "50 (1080p30)" : {"tag" : "xd5f", "fields" : 0},
        }
