FPS_24="24000/1001"
FPS_25="25"
FPS_30="30000/1001"
FPS_50="50"
FPS_60="60000/1001"

class EncoderProfile():
    name = "(untitled)"
    profiles = {}

    def __init__(self, *args, **kwargs):
        pass

    def vfilters(self, **kwargs):
        return []

    def afilters(self, **kwargs):
        return []

    def video(self, **kwargs):
        return [
                "-c:v", "copy"
            ]

    def audio(self, **kwargs):
        return [
                "-c:a", "pcm_s16le",
                "-ar",  48000,
            ]
