
import numpy as np
import cv2 as cv
from utils import *
def main():
    #load audio.mp3
    audio = read_wav('audio.wav')
    data, samplerate = sf.read('audio.wav')
    # visualize_waveform(data[:,0])


if __name__ == "__main__":
    main()