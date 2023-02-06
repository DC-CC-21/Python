# import subprocess
# import numpy as np
# import matplotlib.pyplot as plt
# import scipy.io.wavfile as wav
# import scipy.signal as signal

# def convert_file_to_wav():
#     subprocess.call(['ffmpeg', '-i', r'C:\Users\hands\OneDrive\Documents\vs Code\Python2022\fft_test\Concerning Hobbits.m4a', 'output.wav'])



# read, data = wav.read('output.wav')
# left_channel = data[:,0]
# right_channel = data[:,1]

# plt.plot(left_channel)
# plt.xlabel("Sample Index")
# plt.ylabel("Amplitude")
# plt.show()

# sig_fft = np.fft.fft(left_channel)
# magnitude = np.abs(sig_fft)

# # Find peaks in the magnitude
# peaks, _ = signal.find_peaks(magnitude)
# fs = 1000
# print(peaks * fs / len(sig_fft))
# # Get the frequency axis
# # Plot the data
# plt.plot(np.abs(sig_fft))
# plt.show()

import librosa

# Load the audio file
y, sr = librosa.load('./test_file.m4a')

# Extract the notes from the audio file
notes = librosa.effects.harmonic(y)

# Transcribe the notes to MIDI
midi = librosa.hz_to_midi(notes)

# Print the transcribed notes
print(midi)