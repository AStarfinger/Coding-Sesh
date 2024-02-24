import matplotlib.pyplot as plt
import soundfile as sf
def read_wav(file_path):
    data, samplerate = sf.read(file_path)
    return data, samplerate


def visualize_waveform(waveform):
    plt.plot(waveform)
    plt.show()

def visualize_spectrogram(spectrogram):
    plt.imshow(spectrogram, aspect='auto', origin='lower')
    plt.show()
