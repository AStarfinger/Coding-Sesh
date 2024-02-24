import matplotlib.pyplot as plt
import soundfile as sf
import librosa.display
import librosa

def read_wav(file_path):
    """
    Read a WAV file and return the audio data, the sampling rate, tempo, and beat frames.

    Parameters:
    file_path (str): Path to the WAV file.

    Returns:
    tuple: A tuple containing the audio data as a numpy array, the sampling rate, tempo, and beat frames.
    """
    data, samplerate = sf.read(file_path)
    tempo, beat_frames = librosa.beat.beat_track(y=data, sr=samplerate)
    return data, samplerate, tempo, beat_frames

def visualize_waveform(waveform):
    """
    Visualize the waveform of audio data.

    Parameters:
    waveform (numpy.ndarray): Audio waveform data.
    """
    plt.plot(waveform)
    plt.xlabel('Sample')
    plt.ylabel('Amplitude')
    plt.title('Waveform')
    plt.show()

def visualize_spectrogram(spectrogram, samplerate):
    """
    Visualize the spectrogram of audio data.

    Parameters:
    spectrogram (numpy.ndarray): Spectrogram data.
    samplerate (int): Sampling rate of the audio.
    """
    plt.figure(figsize=(10, 4))
    librosa.display.specshow(spectrogram, sr=samplerate, x_axis='time', y_axis='log')
    plt.colorbar(format='%+2.0f dB')
    plt.title('Spectrogram')
    plt.show()

def print_tempo_and_beat_frames(tempo, beat_frames, samplerate):
    """
    Print tempo and beat frames of audio data.

    Parameters:
    tempo (float): Estimated tempo of the audio.
    beat_frames (numpy.ndarray): Indices of beat events.
    samplerate (int): Sampling rate of the audio.
    """
    beat_times = librosa.frames_to_time(beat_frames, sr=samplerate)
    print("Tempo:", tempo)
    print("Beat frames:", beat_frames)
    print("Beat times (seconds):", beat_times)
