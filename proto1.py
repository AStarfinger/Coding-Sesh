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
from shapeprimitives import *

def play_audio(data, samplerate):
    sd.play(data, samplerate)
    sd.wait()

def main():
    file_path = 'audio.wav'
    data, samplerate = librosa.load(file_path, sr=None)
    onset_env = librosa.onset.onset_strength(y=data, sr=samplerate)
    times = librosa.frames_to_time(np.arange(len(onset_env)), sr=samplerate)
    onsets = times[onset_env > 3.25]  # Threshold onsets
    print(f"{samplerate=}")

    threading.Thread(target=play_audio, args=(data, samplerate), daemon=True).start()

    window_name = 'Visualization'
    cv.namedWindow(window_name)
    start_time = time.time()
    frame_rate_limit = 1/30  # Limit to 30 FPS
    last_frame_time = 0
    shapes = []
    for onset_time in onsets:
        shapes.append(Circle(onset_time, (250, 250)))

    while True:
        current_time = time.time()
        elapsed_time = current_time - start_time

        if current_time - last_frame_time < frame_rate_limit:
            # time.sleep(frame_rate_limit - (current_time - last_frame_time))  # Sleep the remainder of the frame rate limit
            continue

        img = np.zeros((500, 500, 3), dtype=np.uint8)

        for shape in shapes:
            if elapsed_time >= shape.onset_time:
                shape.update()
                shape.draw(img)
                if shape.is_finished():
                    shapes.remove(shape)
                

        cv.imshow(window_name, img)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break

        last_frame_time = time.time()

    cv.destroyAllWindows()


if __name__ == "__main__":
    main()