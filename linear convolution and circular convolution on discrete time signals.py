import numpy as np
import matplotlib.pyplot as plt

# Linear Convolution
def linear_convolution(signal1, signal2):
    return np.convolve(signal1, signal2)

# Circular Convolution (using FFT length = Linear Convolution Length)
def circular_convolution(signal1, signal2):
    fft_length = len(signal1) + len(signal2) - 1

    fft_signal1 = np.fft.fft(signal1, fft_length)
    fft_signal2 = np.fft.fft(signal2, fft_length)

    circular_conv = np.fft.ifft(fft_signal1 * fft_signal2)

    return np.real(circular_conv)

# Input Signals
signal1 = np.array([1, 2, 3, 4, 5])
signal2 = np.array([2, 4, 6, 8, 10])

# Convolutions
linear_conv = linear_convolution(signal1, signal2)
circular_conv = circular_convolution(signal1, signal2)

# Plotting
plt.figure(figsize=(10, 6))

# Linear Convolution
plt.subplot(2, 1, 1)
plt.stem(range(len(linear_conv)), linear_conv)
plt.title("Linear Convolution")
plt.xlabel("Sample")
plt.ylabel("Amplitude")
plt.grid(True)

# Circular Convolution
plt.subplot(2, 1, 2)
plt.stem(range(len(circular_conv)), circular_conv)
plt.title("Circular Convolution")
plt.xlabel("Sample")
plt.ylabel("Amplitude")
plt.grid(True)

plt.tight_layout()
plt.show()

# Display Results
print("Linear Convolution:")
print(linear_conv)

print("\nCircular Convolution:")
print(circular_conv)