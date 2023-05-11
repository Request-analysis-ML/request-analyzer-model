import matplotlib.pyplot as plt
import numpy as np

# Generate some data
x = [20, 30, 40, 50, 60, 70]
#y_precision10 = [0.9272, 0.8759, 0.8442, 0.8266, 0.8153, 0.8010]
#y_precision20 = [0.9997, 0.9921, 0.9732, 0.9471, 0.9158, 0.8851]
y_precision30 = [0.9963, 1.0000, 0.9992, 0.9967, 0.9895, 0.9790]
#y_precision40 = [0.0000, 0.9992, 1.0000, 1.0000, 0.9995, 0.9984]
#y_precision50 = [0.8667, 0.9985, 1.0000, 1.0000, 1.0000, 0.9995]
y_precision60 = [0.9592, 0.9918, 0.9991, 1.0000, 1.0000, 1.0000]
#y_precision70 = [0.9338, 0.9630, 0.9968, 1.0000, 1.0000, 1.0000]
#y_precision80 = [0.8516, 0.8923, 0.9201, 0.9694, 0.9926, 0.9991, 1.0000]
 

# Create a figure and axes objects
fig, ax = plt.subplots()

# Plot the data
#ax.plot(x, y_precision10, '#069AF3', label='10-model')
#ax.plot(x, y_precision20, '#030764', label='20-model')
ax.plot(x, y_precision30, '#029386', label='30-model')
#ax.plot(x, y_precision40, '#C875C4', label='40-model')
#ax.plot(x, y_precision50, '#8C000F', label='50-model')
ax.plot(x, y_precision60, '#FF4500', label='60-model')
#ax.plot(x, y_precision70, '#9ACD32', label='70-model')
#ax.plot(x, y_precision80, label='Precision 80')


# Add labels and legend
ax.set_xlabel('Testing sequence length')
ax.set_ylabel('Score')
ax.set_title('Precision comparison (60- and 30-models)')
ax.legend()

plt.xticks(np.arange(20, 71, 10))
# Display the plot
plt.show()