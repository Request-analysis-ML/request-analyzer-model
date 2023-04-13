import matplotlib.pyplot as plt
import numpy as np

# Generate some data
x = [15, 25, 35, 45, 55, 65]
y_precision = [0.9981, 0.9946, 1.000, 1.000, 1.000, 1.000]
y_recall = [0.2309, 0.6406, 0.6423, 0.6633, 0.7984, 1.000]
y_accuracy = [0.3406, 0.4837, 0.7065, 0.7254, 0.9377, 1.000]
y_F1 = [0.3750, 0.7793, 0.7822, 0.7976, 0.8879, 1.000] 

# Create a figure and axes objects
fig, ax = plt.subplots()

# Plot the data
ax.plot(x, y_precision, label='Precision')
ax.plot(x, y_recall, label='Recall')
ax.plot(x, y_accuracy, label='Accuracy')
ax.plot(x, y_F1, label='F1 score')


# Add labels and legend
ax.set_xlabel('Batch size')
ax.set_ylabel('Score [%]')
ax.set_title('Results')
ax.legend()

plt.xticks(np.arange(15, 56, 10))
# Display the plot
plt.show()



