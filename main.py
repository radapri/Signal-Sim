import numpy as np
import matplotlib.pyplot as plt

# Sampling parameters
fs = 1000        # sampling frequency (Hz)
t = np.linspace(0, 1, fs, endpoint=False)  # 1 second duration

# Signals
sine = np.sin(2 * np.pi * 5 * t)             
square = np.sign(np.sin(2 * np.pi * 5 * t))  
triangle = 2 * np.abs(2 * (t * 5 % 1) - 1) - 1  

# Add Gaussian noise to sine wave
noise = np.random.normal(0, 0.3, t.shape)
sine_noisy = sine + noise

# FFT of the noisy sine wave
freq = np.fft.fftfreq(len(t), 1/fs)
fft_sine = np.abs(np.fft.fft(sine_noisy))

# Plot results
plt.figure(figsize=(12,8))

plt.subplot(2,2,1)
plt.plot(t, sine)
plt.title("Sine wave (5 Hz)")

plt.subplot(2,2,2)
plt.plot(t, square)
plt.title("Square wave (5 Hz)")

plt.subplot(2,2,3)
plt.plot(t, triangle)
plt.title("Triangle wave (5 Hz)")

plt.subplot(2,2,4)
plt.plot(freq[:fs//2], fft_sine[:fs//2])
plt.title("FFT - Noisy sine wave")

plt.tight_layout()
plt.savefig("img/signals.png", dpi=300)  # save result to /img folder
plt.show()
