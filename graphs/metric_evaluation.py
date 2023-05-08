import matplotlib.pyplot as plt
import numpy as np

"""
# Generate some data
x = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]
y_precision = [0.9986, 0.9983, 0.9997, 1.000, 0.9996, 0.9995, 0.9995, 1.000, 1.000, 1.000, 1.000]
y_recall = [0.2147, 0.2595, 0.5050, 0.5405, 0.5563, 0.6259, 0.5967, 0.7804, 0.8364, 0.8130, 0.9933]
y_accuracy = [0.6066, 0.6286, 0.7521, 0.7703, 0.7776, 0.8126, 0.7977, 0.8902, 0.9182, 0.9065, 0.9967]
y_F1 = [0.3534, 0.4119, 0.6710, 0.7017, 0.7148, 0.7698, 0.7470, 0.8767, 0.9109, 0.8969, 0.9966] 


# Create a figure and axes objects
fig, ax = plt.subplots()

# Plot the data
ax.plot(x, y_precision, label='Precision')
ax.plot(x, y_recall, label='Recall')
ax.plot(x, y_accuracy, label='Balanced accuracy')
ax.plot(x, y_F1, label='F1 score')


# Add labels and legend
ax.set_xlabel('Sequence length')
ax.set_ylabel('Score')
ax.set_title('Result with adjusted features')
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

plt.xticks(np.arange(10, 61, 10))
# Display the plot
plt.show()



