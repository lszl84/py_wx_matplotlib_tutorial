import matplotlib.pyplot as plt
import numpy as np

# Parameters
amplitude = 2  # Amplitude
frequency = 2  # Frequency in Hz

# Define the time range
t = np.linspace(0, 2, 1000)  # 2 seconds duration

# Calculate the sine wave
y = amplitude * np.sin(2 * np.pi * frequency * t)

# Plotting the function
plt.figure(figsize=(12, 6))
plt.plot(t, y, label=f'{amplitude} * sin(2π * {frequency}t)')
plt.title('Sine Wave')
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude')
plt.axhline(0, color='black', linewidth=0.5)  # Adds a horizontal line at y=0
plt.axvline(0, color='black', linewidth=0.5)  # Adds a vertical line at t=0
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()
plt.show()

