# import matplotlib.pyplot as plt
# import numpy as np
#
# data = {'Turkey': 100,'Brazil': 86.80,        'USA': 71.18,        'Argentina': 67.49,
#         'Singapore': 59.01,        'China': 57.63,
#         'India': 50.55,
#
#         'Canada': 42.63
#         }
#
# N = len(data)
#
# # Compute angles of each bar
# theta = np.linspace(0.0, 2 * np.pi, N, endpoint=False)
# radii = list(data.values())
#
# # Plot the bar plot
# ax = plt.subplot(111, polar=True)
# bars = ax.bar(theta, radii, width=2 * np.pi / N)
#
# # Set the labels
# ax.set_xticks(theta)
# ax.set_xticklabels(list(data.keys()))
#
# # Show plot
# plt.show()


import matplotlib.pyplot as plt
import numpy as np
import random

data = { 'Canada': 42.63,'India': 50.55,'China': 57.63,'Singapore': 59.01,  'Argentina': 67.49,'USA': 71.18,
        'Brazil': 86.80,'Turkey': 100,    }

N = len(data)

# Compute angles of each bar
theta = np.linspace(0.0, 2 * np.pi, N, endpoint=False)
radii = list(data.values())

# Normalize the radii so they are on a scale from 0 to 1
min_radius = min(radii)
normalized_radii = (radii - min_radius) / (max(radii) - min_radius)

# Plot the bar plot
ax = plt.subplot(111, polar=True)
ax.grid(False)

# Plot each bar with a color based on its score
for i in range(N):
    ax.bar(theta[i], radii[i], width=2 * np.pi / N, color=plt.cm.Blues(normalized_radii[i]))

# Set the labels
ax.set_xticks(theta)
ax.set_xticklabels(list(data.keys()))

# Show plot
plt.show()