import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle


movie_dir = "pebbles_movie"
if not os.path.isdir(movie_dir):
    os.makedirs(movie_dir)

fig, ax = plt.subplots(1)
circle = Circle((0, 0), radius=1, fill=False, edgecolor="black")
square = Rectangle((-1, -1), 2, 2, fill=False, edgecolor="black")
ax.add_patch(circle)
ax.add_patch(square)
ax.set_xlim(-1.1, 1.1)
ax.set_ylim(-1.1, 1.1)
ax.set_aspect("equal")
ax.set_axis_off()

total_pebbles = 100
inside_points = 0
for current_pebbles in range(1, total_pebbles + 1):
    x, y = 2 * np.random.rand(2) - 1
    distance_sq = x**2 + y**2
    if distance_sq <= 1:
        color = "C0"
        inside_points += 1
    else:
        color = "C1"
    pi = 4 * inside_points / current_pebbles

    ax.scatter(x, y, color=color)
    ax.set_title(r"N = {} $\pi \simeq$ {:.4f}".format(current_pebbles, pi))
    plt.savefig(os.path.join(movie_dir, "fig_{:04d}.png".format(current_pebbles)),
                dpi=100)
