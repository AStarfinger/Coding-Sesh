
import numpy as np
import cv2 as cv
from utils import *
def main():
    #load audio.mp3
    data, samplerate = read_wav('audio.wav')
    onset = librosa.onset.onset_strength(data, sr=samplerate)
    onset = onset > 2.25
    
    data, samplerate = sf.read('audio.wav')
    # visualize_waveform(data[:,0])


if __name__ == "__main__":
    main()