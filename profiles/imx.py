from .common import *

"""
MPEG IMX
========
"""


class IMX(EncoderProfile):
    name = "MPEG IMX"
    container = "mxf"
    profiles = {
            "pal-30"  : {"s" : "720:576:1", "pad" : "720:608:0:32", "tag" : "mx3p", "b" : "30000k", "rc" : "1200000", "buf" : "1200000"},
            "pal-40"  : {"s" : "720:576:1", "pad" : "720:608:0:32", "tag" : "mx4p", "b" : "40000k", "rc" : "1600000", "buf" : "1600000"},
            "pal-50"  : {"s" : "720:576:1", "pad" : "720:608:0:32", "tag" : "mx5p", "b" : "50000k", "rc" : "2000000", "buf" : "2000000"},
            "ntsc-30" : {"s" : "720:486:1", "pad" : "720:512:0:26", "tag" : "mx3n", "b" : "30000k", "rc" : "1200000", "buf" : "1200000"},
            "ntsc-40" : {"s" : "720:486:1", "pad" : "720:512:0:26", "tag" : "mx4n", "b" : "40000k", "rc" : "1600000", "buf" : "1600000"},
            "ntsc-50" : {"s" : "720:486:1", "pad" : "720:512:0:26", "tag" : "mx5n", "b" : "50000k", "rc" : "2000000", "buf" : "2000000"},
        }

    def filters(self, **kwargs):
        return [
                "scale={}".format(kwargs["s"]),
                "pad={}:black".format(kwargs["pad"])
            ]

    def video(self, **kwargs):
        return [
                "-filter:v", "scale={},pad={}:black".format(kwargs["s"], kwargs["pad"])
                "-pix_fmt", "yuv422p",
                "-c:v", "mpeg2video",
                "-b:v", kwargs["b"],
                "-minrate", kwargs["b"],
                "-maxrate", kwargs["b"]
                "-rc_init_occupancy", kwargs["rc"],
                "-bufsize", kwargs["buf"],
                "-intra",
                "-flags", "+ildct+ilme+low_delay",
                "-intra_vlc", 1,
                "-non_linear_quant", 1,
                "-ps", 1,
                "-qmin", 1,
                "-qmax", 3,
                "-top", 1,
                "-dc", 10,
                "-rc_buf_aggressivity", 0.25,
                "-bsf:v", "imxdump",
                "-tag:v", kwargs["tag"]
            ]
