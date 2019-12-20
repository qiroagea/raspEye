import subprocess as sp

sp.run(["aplay", "-D", "plughw:0,0", "-N", "./music/groundEsc.flac"])
