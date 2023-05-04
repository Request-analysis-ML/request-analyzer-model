import matplotlib.pyplot as plt
import numpy as np

# Generate some data
x = [10, 20, 30, 40, 50, 60]
y_precision30 = [0.0000, 0.0000, 1.0000, 0.9983, 1.0000, 0.9964]
y_precision40 = [0.0000, 0.9310, 0.9985, 0.9996, 0.9996, 0.9995]
y_precision50 = [0.0000, 0.5714, 0.9972, 0.9995, 1.0000, 1.0000]
y_precision60 = [0.8633, 0.9155, 0.9876, 0.9987, 1.0000, 1.0000]
 

# Create a figure and axes objects
fig, ax = plt.subplots()

# Plot the data
ax.plot(x, y_precision30, label='Precision 30')
ax.plot(x, y_precision40, label='Precision 40')
ax.plot(x, y_precision50, label='Precision 50')
ax.plot(x, y_precision60, label='Precision 60')


# Add labels and legend
ax.set_xlabel('Testing sequence length')
ax.set_ylabel('Score')
ax.set_title('Precision scores')
ax.legend()

plt.xticks(np.arange(10, 61, 10))
# Display the plot
plt.show()