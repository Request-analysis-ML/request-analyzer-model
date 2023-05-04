import matplotlib.pyplot as plt
import numpy as np

# Generate some data
x = [10, 20, 30, 40, 50, 60]
y_accuracy30 = [0.4998, 0.4996, 0.6302, 0.7602, 0.8683, 0.9284]
y_accuracy40 = [0.4998, 0.5059, 0.6530, 0.8386, 0.9418, 0.9316]
y_accuracy50 = [0.4983, 0.4992, 0.7079, 0.8016, 0.9417, 0.9644]
y_accuracy60 = [0.5279, 0.6054, 0.6434, 0.8483, 0.9365, 0.9790]
 

# Create a figure and axes objects
fig, ax = plt.subplots()

# Plot the data
ax.plot(x, y_accuracy30, label='Accuracy 30')
ax.plot(x, y_accuracy40, label='Accuracy 40')
ax.plot(x, y_accuracy50, label='Accuracy 50')
ax.plot(x, y_accuracy60, label='Accuracy 60')


# Add labels and legend
ax.set_xlabel('Testing sequence length')
ax.set_ylabel('Score')
ax.set_title('Balanced accuracy scores')
ax.legend()

plt.xticks(np.arange(10, 61, 10))
# Display the plot
plt.show()