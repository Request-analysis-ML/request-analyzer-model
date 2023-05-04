import matplotlib.pyplot as plt
import numpy as np

# Generate some data
x = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]
y_precision = [0.9986, 0.9983, 0.9997, 1.000, 0.9996, 0.9995, 0.9995, 1.000, 1.000, 1.000, 1.000]
y_recall = [0.2147, 0.2595, 0.5050, 0.5405, 0.5563, 0.6259, 0.5967, 0.7804, 0.8364, 0.8130, 0.9933]
y_accuracy = [0.3454, 0.3844, 0.5899, 0.6205, 0.6346, 0.6975, 0.6699, 0.8209, 0.8669, 0.8483, 0.9946]
y_F1 = [0.3534, 0.4119, 0.6710, 0.7017, 0.7148, 0.7698, 0.7470, 0.8767, 0.9109, 0.8969, 0.9966] 

# Create a figure and axes objects
fig, ax = plt.subplots()

# Plot the data
ax.plot(x, y_precision, label='Precision')
ax.plot(x, y_recall, label='Recall')
ax.plot(x, y_accuracy, label='Accuracy')
ax.plot(x, y_F1, label='F1 score')


# Add labels and legend
ax.set_xlabel('Sequence length')
ax.set_ylabel('Score')
ax.set_title('Results')
ax.legend()

plt.xticks(np.arange(10, 61, 5))
# Display the plot
plt.show()



