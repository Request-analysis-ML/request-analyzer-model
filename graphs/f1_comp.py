import matplotlib.pyplot as plt
import numpy as np

# Generate some data
x = [10, 20, 30, 40, 50, 60]
y_f130 = [0.0000, 0.0000, 0.4131, 0.6876, 0.8484, 0.9290]
y_f140 = [0.0000, 0.0239, 0.4714, 0.8084, 0.9390, 0.9275]
y_f150 = [0.0000, 0.0012, 0.5922, 0.7534, 0.9381, 0.9630]
y_f160 = [0.4202, 0.5364, 0.4655, 0.8047, 0.9322, 0.9785]
 

# Create a figure and axes objects
fig, ax = plt.subplots()

# Plot the data
ax.plot(x, y_f130, label='F1 30')
ax.plot(x, y_f140, label='F1 40')
ax.plot(x, y_f150, label='F1 50')
ax.plot(x, y_f160, label='F1 60')


# Add labels and legend
ax.set_xlabel('Testing sequence length')
ax.set_ylabel('Score')
ax.set_title('F1 scores')
ax.legend()

plt.xticks(np.arange(10, 61, 10))
# Display the plot
plt.show()