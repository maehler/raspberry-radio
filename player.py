import numpy as np
import sounddevice as sd
import sys
from urllib.request import urlopen

def play(url):
    f = urlopen(url)

    chunk = f.read(4096)
    bchunk = np.array(list(chunk), dtype=np.int16)

    sd.play(bchunk, 44100)
