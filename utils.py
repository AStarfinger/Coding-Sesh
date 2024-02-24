import matplotlib.pyplot as plt
import soundfile as sf
import librosa.display
import librosa
import numpy as np
from scipy.ndimage import gaussian_filter1d

def read_wav(file_path):
    """
    Read a WAV file and return the audio data, the sampling rate, tempo, and beat frames.
    """
    data, samplerate = librosa.load(file_path)
    tempo, beat_frames = librosa.beat.beat_track(y=data, sr=samplerate)
    
    beat_times = librosa.frames_to_time(beat_frames, sr=samplerate)
    
    # Compute the onset envelope
    onset_env = librosa.onset.onset_strength(y=data, sr=samplerate)
    
    # Apply Gaussian smoothing
    sigma = 1  # Standard deviation for Gaussian kernel
    smoothed_onset_env = gaussian_filter1d(onset_env, sigma=sigma)
    
    # Normalize the smoothed onset envelope
    smoothed_onset_env = librosa.util.normalize(smoothed_onset_env)
    
    times = librosa.times_like(onset_env, sr=samplerate)
    smoothed_onset_env = onset_env > 2.35
    plot_onset_envelope(data,onset_env, smoothed_onset_env, times, beat_times)
    
    return data, samplerate

def plot_onset_envelope(data,onset_env, smoothed_onset_env, times, beat_times):
    D = np.abs(librosa.stft(data))
    fig, ax = plt.subplots(nrows=2, sharex=True)
    librosa.display.specshow(librosa.amplitude_to_db(D, ref=np.max),
                             x_axis='time', y_axis='log', ax=ax[0])
    ax[1].plot(times, 2 + onset_env / onset_env.max(), alpha=0.8, label='Original (mel)')
    ax[1].plot(times, 1 + smoothed_onset_env / smoothed_onset_env.max(), alpha=0.8, label='Smoothed (Gaussian)')
    ax[1].vlines(beat_times, 0, 1, alpha=0.5, color='r', linestyle='--', label='Beats')
    ax[1].legend()
    ax[1].set(xlabel='Time')
    plt.show()
    

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


if __name__ == "__main__":
    read_wav('audio.wav')