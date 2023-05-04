import matplotlib.pyplot as plt
import numpy as np

# Generate some data
x = [10, 20, 30, 40, 50, 60]
y_recall30 = [0.0000, 0.0000, 0.2603, 0.5244, 0.7366, 0.7801]
y_recall40 = [0.0000, 0.0121, 0.3085, 0.6786, 0.8853, 0.8651]
y_recall50 = [0.0000, 0.0006, 0.4211, 0.6045, 0.8834, 0.9288]
y_recall60 = [0.2777, 0.3793, 0.3045, 0.7007, 0.8730, 0.9579]
 

# Create a figure and axes objects
fig, ax = plt.subplots()

# Plot the data
ax.plot(x, y_recall30, label='Recall 30')
ax.plot(x, y_recall40, label='Recall 40')
ax.plot(x, y_recall50, label='Recall 50')
ax.plot(x, y_recall60, label='Recall 60')


# Add labels and legend
ax.set_xlabel('Testing sequence length')
ax.set_ylabel('Score')
ax.set_title('Recall scores')
ax.legend()

plt.xticks(np.arange(10, 61, 10))
# Display the plot
plt.show()