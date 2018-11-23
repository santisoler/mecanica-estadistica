import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle


total_pebbles = 100
x_inside, y_inside = [], []
x_outside, y_outside = [], []
for step in range(total_pebbles):
    x, y = 2 * np.random.rand(2) - 1
    distance_sq = x**2 + y**2
    if distance_sq <= 1:
        x_inside.append(x)
        y_inside.append(y)
    else:
        x_outside.append(x)
        y_outside.append(y)
pi = 4 * len(x_inside) / total_pebbles

fig, ax = plt.subplots(1)
circle = Circle((0, 0), radius=1, fill=False, edgecolor="black")
ax.scatter(x_inside, y_inside)
ax.scatter(x_outside, y_outside)
ax.add_patch(circle)
ax.set_aspect("equal")
ax.set_title(r"$\pi \simeq$ {}".format(pi))
plt.show()
