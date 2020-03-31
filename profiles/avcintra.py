from .common import *

"""
AVC-Intra
=========

Tags
----

 - ai5p - 50M 720p24/p30/p60
 - ai5q - 50M 720p25/p50
 - ai56 - 50M 1080i60
 - ai55 - 50M 1080i50
 - ai53 - 50M 1080p24/p30
 - ai52 - 50M 1080p25
 - ai1p - 100M 720p24/p30/p60
 - ai1q - 100M 720p25/p50
 - ai16 - 100M 1080i60
 - ai15 - 100M 1080i50
 - ai13 - 100M 1080p24/p30
 - ai12 - 100M 1080p25

Common to 50 and 100
--------------------

  - Frame rates:
        * 1920 × 1080 (23.98p / 25p / 29.97p / 50i / 59.94i)
        * 1280 × 720 (23.98p / 25p / 29.97p / 50p / 59.94p)
  - 10 bit luma and chroma

AVC-Intra 50
------------

 - nominally 50 Mbit/s, size of each frame is fixed
 - CABAC entropy coding only.
 - 1920 × 1080 formats are High 10 Intra Profile, Level 4
 - 1280 × 720 formats are High 10 Intra Profile, Level 3.2
 - 4:2:0 chrominance sampling
 - frames are horizontally scaled by 3/4 (1920x1080 is scaled to 1440x1080. 1280 × 720 is scaled to 960x720)

AVC-Intra 100
-------------
 - nominally 100 Mbit/s, size of each frame is fixed
 - CAVLC entropy coding only.
 - All formats are High 4:2:2 Intra Profile, Level 4.1
 - 4:2:2 chrominance sampling
 - frames are not scaled


```
AVC50=-s 1440x1080 -pix_fmt yuv420p10le -b:v 50M -x264opts "avcintra-class=50:force-cfr=1:colorprim=bt709:transfer=bt709:colormatrix=bt709:interlaced=1"
AVC100=-pix_fmt yuv422p10le -b:v 100M -x264opts "avcintra-class=100:force-cfr=1:colorprim=bt709:transfer=bt709:colormatrix=bt709:interlaced=1"
```


AVC-Intra 300
-------------


 - Level/Profile High 4:2:2 Profile @ Level 5.2
 - GOP I-frame only
 - Chroma Sampling 4:2:2
 - Bit Rate 500 Mbit/s
 - Constant Bit Rate Yes
 - Picture Size (active) 3840 x 2160
 - Aspect Ratio 16:9
 - Frame Rate 50fps
 - Scan Type Progressive
 - Color Matrix BT2020nc
 - Color Range Limited
 - Bit depth 10 bit
 - Timecode in GOP header Not in use

Level 300 is not supported by x264, but this is a dirty hack

```
  "x264-10b.exe" --input-depth 16 --preset medium --profile high422 --keyint 1
        --bitrate 500000 --vbv-maxrate 500000 --vbv-bufsize 500000
        --deblock -1:-1 --overscan show --colormatrix bt709 --range tv
        --transfer bt709 --colorprim bt709 --videoformat component --nal-hrd cbr --output-csp i422
```
"""



class AVCINTRA(EncoderProfile):
    name = "AVC-INTRA"
    profiles = {
            "50-720p24"   : {"class": 50,  "tag": "ai5p", "fields" : False, "r" : FPS_24},
            "50-720p30"   : {"class": 50,  "tag": "ai5p", "fields" : False, "r" : FPS_30},
            "50-720p60"   : {"class": 50,  "tag": "ai5p", "fields" : False, "r" : FPS_60},
            "50-720p25"   : {"class": 50,  "tag": "ai5q", "fields" : False, "r" : FPS_25},
            "50-720p50"   : {"class": 50,  "tag": "ai5q", "fields" : False, "r" : FPS_50},
            "50-1080i60"  : {"class": 50,  "tag": "ai56", "fields" : True,  "r" : FPS_30},
            "50-1080i50"  : {"class": 50,  "tag": "ai55", "fields" : True,  "r" : FPS_25},
            "50-1080p24"  : {"class": 50,  "tag": "ai53", "fields" : False, "r" : FPS_24},
            "50-1080p30"  : {"class": 50,  "tag": "ai53", "fields" : False, "r" : FPS_30},
            "50-1080p25"  : {"class": 50,  "tag": "ai52", "fields" : False, "r" : FPS_25},
            "100-720p24"  : {"class": 100, "tag": "ai1p", "fields" : False, "r" : FPS_24},
            "100-720p30"  : {"class": 100, "tag": "ai1p", "fields" : False, "r" : FPS_30},
            "100-720p60"  : {"class": 100, "tag": "ai1p", "fields" : False, "r" : FPS_60},
            "100-720p25"  : {"class": 100, "tag": "ai1q", "fields" : False, "r" : FPS_25},
            "100-720p50"  : {"class": 100, "tag": "ai1q", "fields" : False, "r" : FPS_50},
            "100-1080i60" : {"class": 100, "tag": "ai16", "fields" : True,  "r" : FPS_30},
            "100-1080i50" : {"class": 100, "tag": "ai15", "fields" : True,  "r" : FPS_25},
            "100-1080p24" : {"class": 100, "tag": "ai13", "fields" : False, "r" : FPS_24},
            "100-1080p30" : {"class": 100, "tag": "ai13", "fields" : False, "r" : FPS_30},
            "100-1080p25" : {"class": 100, "tag": "ai12", "fields" : False, "r" : FPS_25},
        }

    def video(self, **kwargs):
        return [
                "-s", kwargs["s"],
                "-pix_fmt", kwargs["pix_fmt"],
                "-c:v", "libx264",
                "-b:v",  kwargs["b:v"],
                "-g", 1,
                "-top", 1,
                "-flags", "+ildct+ilme",
                "-tune", "psnr",
                "-x264opts", "avcintra-class={}:force-cfr=1:colorprim=bt709:transfer=bt709:colormatrix=bt709:interlaced=1".format(kwargs["class"]),
            ]
