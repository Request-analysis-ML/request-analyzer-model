import matplotlib.pyplot as plt
import numpy as np


# Generate some data
x = [10, 20, 30, 40, 50, 60, 70, 80 ]
y_precision = [0.9980, 0.9997, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000]
y_recall = [0.1488, 0.4690, 0.5246, 0.6247, 0.8371, 0.9747, 0.9984, 1.0000]
y_accuracy = [0.5737, 0.7341, 0.7623, 0.8124, 0.9186, 0.9874, 0.9992, 1.0000]
y_F1 = [0.2589, 0.6384, 0.6881, 0.7690, 0.9113, 0.9873, 0.9992, 1.0000] 


# Create a figure and axes objects
fig, ax = plt.subplots()

# Plot the data
ax.plot(x, y_precision, '#069AF3', label='Precision')
ax.plot(x, y_recall, '#030764', label='Recall')
ax.plot(x, y_accuracy, '#029386', label='Balanced accuracy')
ax.plot(x, y_F1, '#C875C4', label='F1 score')


# Add labels and legend
ax.set_xlabel('Sequence length')
ax.set_ylabel('Score')
ax.set_title('Result: Sequence length comparison')
ax.legend()

"""

# Adjusted result
x = [10, 20, 30, 40, 50, 60]
adj_precision = [1.0000, 0.9995, 0.9992, 0.9996, 1.0000, 1.0000]
prev_precision = [0.8633, 0.9155, 0.9876, 0.9987, 1.0000, 1.0000]
adj_recall = [0.1598, 0.2962, 0.2924, 0.7528, 0.8962, 0.9713]
prev_recall = [0.2777, 0.3793, 0.3045, 0.7007, 0.8730, 0.9579]
adj_F1 = [0.3226, 0.4570, 0.4524, 0.8588, 0.9452, 0.9855] 
prev_F1 = [0.4202, 0.5364, 0.4655, 0.8047, 0.9322, 0.9785]

# Create a figure and axes objects
fig, ax = plt.subplots()

# Plot the data
ax.plot(x, adj_precision, 'b-', label='Adjusted precision')
ax.plot(x, prev_precision, 'b--', label='Previous precision')
ax.plot(x, adj_F1, 'm-', label='Adjusted F1 score')
ax.plot(x, prev_F1, 'm--', label='Previous F1 score')
ax.plot(x, adj_recall, 'g-', label='Adjusted recall')
ax.plot(x, prev_recall, 'g--', label='Previous recall')

# Add labels and legend
ax.set_xlabel('Sequence length')
ax.set_ylabel('Score')
ax.set_title('Result with adjusted features')
ax.legend()
"""


plt.xticks(np.arange(10, 81, 10))
# Display the plot
plt.show()



