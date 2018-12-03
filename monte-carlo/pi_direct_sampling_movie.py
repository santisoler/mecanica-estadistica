import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle


total_pebbles = 200
np.random.seed(12345)

movie_dir = "_pebbles_movie"
if not os.path.isdir(movie_dir):
    os.makedirs(movie_dir)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
ax1.plot([1, total_pebbles], [np.pi] * 2, '--', color='k')
ax1.set_xlim(0, total_pebbles)
line, = ax1.plot([], [], '-')
circle = Circle((0, 0), radius=1, fill=False, edgecolor="black")
square = Rectangle((-1, -1), 2, 2, fill=False, edgecolor="black")
ax2.add_patch(circle)
ax2.add_patch(square)
ax2.set_xlim(-1.1, 1.1)
ax2.set_ylim(-1.1, 1.1)
ax2.set_aspect("equal")
ax2.set_axis_off()

inside_points = 0
pi_values = []
for current_pebbles in range(1, total_pebbles + 1):
    x, y = np.random.uniform(low=-1, high=1, size=2)
    distance_sq = x**2 + y**2
    if distance_sq < 1:
        color = "C0"
        inside_points += 1
    else:
        color = "C1"
    pi = 4 * inside_points / current_pebbles
    pi_values.append(pi)

    fig.suptitle(r"N = {}, $\pi \simeq$ {:.4f}".format(current_pebbles, pi))
    ax2.scatter(x, y, color=color)
    line.set_xdata(range(1, current_pebbles + 1))
    line.set_ydata(pi_values)
    ax1.set_ylim(0.9 * np.min(pi_values), 1.1 * np.max(pi_values))
    fig.canvas.draw()
    plt.savefig(os.path.join(movie_dir, "fig_{:04d}.png".format(current_pebbles)),
                dpi=100)
