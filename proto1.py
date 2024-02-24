import numpy as np
import cv2 as cv
import librosa
import sounddevice as sd
import time
from utils import *
import threading
import time
import numpy as np
import cv2 as cv
import librosa
import sounddevice as sd

def play_audio(data, samplerate):
    sd.play(data, samplerate)
    sd.wait()

def main():
    file_path = 'audio.wav'
    data, samplerate = librosa.load(file_path, sr=None)
    onset_env = librosa.onset.onset_strength(y=data, sr=samplerate)
    times = librosa.frames_to_time(np.arange(len(onset_env)), sr=samplerate)
    onsets = times[onset_env > 2.45]  # Threshold onsets

    # Start audio in a separate thread
    threading.Thread(target=play_audio, args=(data, samplerate), daemon=True).start()

    window_name = 'Visualization'
    cv.namedWindow(window_name)
    start_time = time.time()

    while True:
        elapsed_time = time.time() - start_time
        img = np.zeros((500, 500, 3), dtype=np.uint8)

        # Check if we're past the first onset time, then draw/grow a circle accordingly
        for onset_time in onsets:
            if elapsed_time >= 5*onset_time:  # If we're at or past an onset time
                radius = int(((elapsed_time - onset_time) % 1) * 50)  # Example growth function
                cv.circle(img, (250, 250), radius, (255, 255, 255), 2)

        cv.imshow(window_name, img)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break

    cv.destroyAllWindows()

if __name__ == "__main__":
    main()