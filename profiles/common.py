FPS_24="24000/1001"
FPS_25="25"
FPS_30="30000/1001"
FPS_50="50"
FPS_60="60000/1001"

class EncoderFormat():
    name = "(untitled)"
    profiles = {}

    def __init__(self, profile, *args, **kwargs):
        self.profile = self.profiles[profile]

    def build(self):
        cmd = self.video(**self.profile)
        return cmd

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
