import sounddevice as sd
import numpy as np
print(sd.query_devices())

# Set the device to HDMI output
# sd.default.device = 0  # Use the HDMI device index

# Generate a test tone
fs = 44100  # Sample rate
duration = 4  # seconds
frequency = 440  # Hz
t = np.linspace(0, duration, int(fs * duration), False)
note = np.sin(frequency * t * 2 * np.pi)

# Attempt to play the test tone
sd.play(note, fs)
sd.wait()  # Wait for playback to finish
