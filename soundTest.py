import subprocess as sp


class Sound:
    def __init__(self):
        self.soundFile = ""
        self.isPlaying = False

    def set_sound_file(self, sound_file):
        self.soundFile = sound_file

    def play_sound(self):
        if self.soundFile == "":
            return
        print('play' + self.soundFile)
        sp.call(["mpc", "stop"])
        sp.call(["mpc", "clear"])
        sp.call(["mpc", "update"])
        sp.call(["mpc", "add", self.soundFile])
        sp.call(["mpc", "play"])
