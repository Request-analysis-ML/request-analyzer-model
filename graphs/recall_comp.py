import matplotlib.pyplot as plt
import numpy as np

# Generate some data
x = [10, 20, 30, 40, 50, 60, 70]
y_recall10 = [0.1488, 0.3597, 0.6551, 0.8523, 0.9462, 0.9736, 0.9549]
y_recall20 = [0.0000, 0.4690, 0.7627, 0.9225, 0.9761, 0.9946, 1.0000]
y_recall30 = [0.0000, 0.0809, 0.5246, 0.7530, 0.9010, 0.9691, 0.9791]
y_recall40 = [0.0019, 0.0000, 0.2651, 0.6247, 0.8408, 0.9256, 0.9660]
y_recall50 = [0.0355, 0.0039, 0.2334, 0.5589, 0.8371, 0.9529, 0.9874]
y_recall60 = [0.2044, 0.2811, 0.3528, 0.6609, 0.8662, 0.9747, 0.9984]
y_recall70 = [0.2078, 0.3375, 0.2101, 0.5514, 0.7717, 0.9458, 0.9984]
#y_recall80 = [0.7401, 0.6391, 0.5089, 0.6333, 0.8472, 0.9767, 1.0000]
 

# Create a figure and axes objects
fig, ax = plt.subplots()

# Plot the data
ax.plot(x, y_recall10, '#069AF3', label='10-model')
ax.plot(x, y_recall20, '#030764', label='20-model')
ax.plot(x, y_recall30, '#029386', label='30-model')
ax.plot(x, y_recall40, '#C875C4', label='40-model')
ax.plot(x, y_recall50, '#8C000F', label='50-model')
ax.plot(x, y_recall60, '#FF4500', label='60-model')
ax.plot(x, y_recall70, '#9ACD32', label='70-model')
#ax.plot(x, y_recall80, label='Recall 80')


# Add labels and legend
ax.set_xlabel('Testing sequence length')
ax.set_ylabel('Score')
ax.set_title('Recall scores')
ax.legend()

plt.xticks(np.arange(10, 71, 10))
# Display the plot
plt.show()