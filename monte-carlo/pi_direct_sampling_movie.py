import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle


plt.tick_params(
    axis=['x', 'y'],   # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom=False,      # ticks along the bottom edge are off
    top=False,         # ticks along the top edge are off
    labelbottom=False) # labels along the bottom edge are off

movie_dir = "pebbles_movie"
if not os.path.isdir(movie_dir):
    os.makedirs(movie_dir)

total_pebbles = 100
x_inside, y_inside = [], []
x_outside, y_outside = [], []

for current_pebbles in range(1, total_pebbles + 1):
    x, y = 2 * np.random.rand(2) - 1
    distance_sq = x**2 + y**2
    if distance_sq <= 1:
        x_inside.append(x)
        y_inside.append(y)
    else:
        x_outside.append(x)
        y_outside.append(y)
    pi = 4 * len(x_inside) / current_pebbles

    fig, ax = plt.subplots(1)
    circle = Circle((0, 0), radius=1, fill=False, edgecolor="black")
    ax.scatter(x_inside, y_inside)
    ax.scatter(x_outside, y_outside)
    ax.add_patch(circle)
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_aspect("equal")
    ax.set_title(r"$\pi \simeq$ {:.4f}".format(pi))
    plt.tight_layout()
    plt.savefig(os.path.join(movie_dir, "fig_{:04d}.png".format(current_pebbles)),
                dpi=100)
    plt.close(fig)
