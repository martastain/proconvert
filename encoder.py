#!/usr/bin/env python3

import sys

import profiles

from profiles.common import EncoderFormat


def list_available_profiles():
    for encoder_format in EncoderFormat.__subclasses__():
        for profile in encoder_format.profiles:
            print ("{} {}".format(encoder_format.name, profile))

        print ()



r = profiles.AVCINTRA("50 (1080i50)") 
print (r.build())


sys.exit(0)

