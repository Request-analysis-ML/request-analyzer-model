import matplotlib.pyplot as plt
import numpy as np

# Generate some data
x = [10, 20, 30, 40, 50, 60, 70]
y_f110 = [0.2589, 0.5184, 0.7496, 0.8482, 0.8824, 0.8874, 0.8708]
y_f120 = [0.0000, 0.6384, 0.8624, 0.9472, 0.9614, 0.9536, 0.9391]
y_f130 = [0.0000, 0.1496, 0.6881, 0.8588, 0.8535, 0.9792, 0.9791]
y_f140 = [0.0037, 0.0000, 0.4190, 0.7690, 0.9135, 0.9611, 0.9819]
y_f150 = [0.0684, 0.0077, 0.4572, 0.7171, 0.9113, 0.9759, 0.9934]
y_f160 = [0.3319, 0.4348, 0.5204, 0.7977, 0.9283, 0.9873, 0.9992]
y_f170 = [0.3304, 0.4958, 0.3450, 0.7101, 0.8711, 0.9721, 0.9991]
#y_f180 = [0.7919, 0.7448, 0.6553, 0.7664, 0.9141, 0.9878, 1.0000]
 

# Create a figure and axes objects
fig, ax = plt.subplots()

# Plot the data
ax.plot(x, y_f110, '#069AF3', label='10-model')
ax.plot(x, y_f120, '#030764', label='20-model')
ax.plot(x, y_f130, '#029386', label='30-model')
ax.plot(x, y_f140, '#C875C4', label='40-model')
ax.plot(x, y_f150, '#8C000F', label='50-model')
ax.plot(x, y_f160, '#FF4500', label='60-model')
ax.plot(x, y_f170, '#9ACD32', label='70-model')
#ax.plot(x, y_f180, label='F1 80')


# Add labels and legend
ax.set_xlabel('Testing sequence length')
ax.set_ylabel('Score')
ax.set_title('F1 scores')
ax.legend()

plt.xticks(np.arange(10, 71, 10))
# Display the plot
plt.show()