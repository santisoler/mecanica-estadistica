import os
import random
import numpy as np
import matplotlib.pyplot as plt


GRID_SHAPE = 10
ALLOWED_STEPS = [[1, 0], [-1, 0], [0, 1], [0, -1]]


def new_step(x, y):
    xmax, ymax = GRID_SHAPE - 1, GRID_SHAPE - 1
    delta_x, delta_y = random.choice(ALLOWED_STEPS)
    new_x, new_y = x + delta_x, y + delta_y
    if new_x >= 0 and new_x <= xmax and new_y >= 0 and new_y <= ymax:
        return new_x, new_y
    else:
        return x, y


movie_dir = "markov_discrete"
if not os.path.isdir(movie_dir):
    os.makedirs(movie_dir)

total_steps = 200
x, y = 0, 0

fig = plt.figure()
x_old, y_old = [], []
color = "C0"
for step in range(total_steps):
    x_old.append(x)
    y_old.append(y)
    if step > 0:
        x, y = new_step(x, y)
        if x == x_old[-1] and y == y_old[-1]:
            color = "C1"
        else:
            color = "C0"

    ax = fig.subplots()
    ax.set_xlim(-0.5, GRID_SHAPE - 0.5)
    ax.set_ylim(-0.5, GRID_SHAPE - 0.5)
    ax.set_aspect('equal')
    ax.grid()
    ax.scatter(x_old, y_old, color='C7')
    ax.scatter(x, y, color=color)
    ax.set_xticks(np.arange(-0.5, GRID_SHAPE + 0.5, 1))
    ax.set_yticks(np.arange(-0.5, GRID_SHAPE + 0.5, 1))
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    plt.savefig(os.path.join(movie_dir, "{:04d}.png".format(step)))
    fig.clear()
