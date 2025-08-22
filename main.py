import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import ttk 

# Signal Generator
def generate_signal():
    fs = 1000        # sampling frequency (Hz)
    t = np.linspace(0, 1, fs, endpoint=False)  # 1 second duration
    freq = freq_var.get()
    amp = amp_var.get()
    signal_type = signal_var.get()
    add_noise = noise_var.get()

    # Signals
    if signal_type == "Sine": 
        signal = amp * np.sin(2 * np.pi * freq * t)
    elif signal_type == "Square":
        signal = amp * np.sign(np.sin(2 * np.pi * freq * t))
    elif signal_type == "Triangle":
        signal = amp * 2 * np.abs(2 * (t * freq % 1) - 1) - 1
    else:
        signal = np.zeros_like(t)

    # Add Gaussian noise to signal
    if add_noise:
        noise = np.random.normal(0, 0.3, t.shape)
        signal += noise

    # FFT 
    freqs = np.fft.fftfreq(len(t), 1/fs)
    fft_vals = np.abs(np.fft.fft(signal))

    # Plot results
    plt.figure(figsize=(10,4))

    plt.subplot(1,2,1)
    plt.plot(t, signal)
    plt.title(f"{signal_type} wave - {freq} Hz")
    plt.xlabel("Time [s]")
    plt.ylabel("Amplitude")

    plt.subplot(1,2,2)
    plt.plot(freqs[:fs//2], fft_vals[:fs//2])
    plt.title("FFT Spectrum")
    plt.xlabel("Frequency [Hz]")
    plt.ylabel("Magnitude")

    plt.tight_layout()
    plt.show()  

# UI with tkinter

root = Tk() 
root.title("Signal Simulator")

# Type of Signal 
ttk.Label(root, text="Signal Type:").grid(row=0, column=0, padx=5, pady=5)
signal_var = StringVar(value="Sine")
signal_menu = ttk.Combobox(root, textvariable=signal_var, values=["Sine", "Square", "Triangle"])
signal_menu.grid(row=0, column=1, padx=5, pady=5)   

# Amount of Frequency 
ttk.Label(root, text="Frequency (Hz):").grid(row=1, column=0, padx=5, pady=5)
freq_var = IntVar(value=5)
freq_entry = ttk.Entry(root, textvariable=freq_var)
freq_entry.grid(row=1, column=1, padx=5, pady=5)

# Amplitude 
ttk.Label(root, text="Amplitude:").grid(row=2, column=0, padx=5, pady=5)
amp_var = IntVar(value=1)

ttk.Scale(root, from_=1, to=5, orient=HORIZONTAL, variable=amp_var).grid(row=2, column=1, padx=5, pady=5)

# Add Noise Option
noise_var = BooleanVar(value=False)
ttk.Checkbutton(root, text="Add Noise", variable=noise_var).grid(column=0, row=3, columnspan=2, pady=5)

# Usage Button
ttk.Button(root, text="Generate Signal", command=generate_signal).grid(column=0, row=4, columnspan=2, pady=10)

# Usage Instructions
ttk.Label(root, text="Instructions:").grid(column=0, row=5, columnspan=2, pady=5)
ttk.Label(root, text="1. Select Signal Type").grid(column=0, row=6, columnspan=2, pady=2)
ttk.Label(root, text="2. Set Frequency and Amplitude").grid(column=0, row=7, columnspan=2, pady=2)
ttk.Label(root, text="3. Check 'Add Noise' if desired").grid(column=0, row=8, columnspan=2, pady=2)
ttk.Label(root, text="4. Click 'Generate Signal'").grid(column=0, row=9, columnspan=2, pady=2)

root.mainloop()
