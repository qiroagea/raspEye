import wave
import pyaudio


def play_sound(filename="sample.wav"):
    try:
        wf = wave.open(filename, "r")
    except FileNotFoundError:
        print("[Error 404] " + filename)
        return 0

    pa = pyaudio.PyAudio()
    stream = pa.open(
        format=pa.get_format_from_width(wf.getsampwidth()),
        channels=wf.getnchannels(),
        rate=wf.getframerate(),
        output=True
    )

    chunk = 1024
    data = wf.readframes(chunk)
    while data != '':
        stream.write(data)
        data = wf.readframes(chunk)
    stream.close()
    pa.terminate()


if __name__ is "__main__":
    play_sound("./sounds/himeSorry.wav")
