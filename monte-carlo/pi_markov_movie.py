import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle


movie_dir = "markov_pi_movie"
if not os.path.isdir(movie_dir):
    os.makedirs(movie_dir)


total_pebbles = 100
delta = 0.4
x, y = 0., 0.
np.random.seed(1234)

fig, ax = plt.subplots()
circle = Circle((0, 0), radius=1, fill=False, edgecolor="black")
square = Rectangle((-1, -1), 2, 2, fill=False, edgecolor="black")
ax.add_patch(circle)
ax.add_patch(square)
ax.set_xlim(-1.1, 1.1)
ax.set_ylim(-1.1, 1.1)
ax.set_aspect('equal')
ax.set_axis_off()
arrow = ax.arrow(x, y, 0, 0)

pebbles_inside_circle = 0
for step in range(total_pebbles):
    x_old, y_old = x, y
    # Generamos desplazamientos aleatorios entre [-delta, delta]
    delta_x, delta_y = np.random.uniform(low=-delta, high=delta, size=2)
    # Aceptamos el nuevo salto si cae dentro del cuadrado
    if np.abs(x + delta_x) < 1 and np.abs(y + delta_y) < 1:
        x, y = x + delta_x, y + delta_y
    distance_sq = x**2 + y**2
    if distance_sq < 1:
        pebbles_inside_circle += 1
        color = "C0"
    else:
        color = "C1"

    # Plot arrow and new scatter point
    try:
        arrow.remove()
    except:
        arrow = None
    if x != x_old and y != y_old and step != 0:
        arrow = ax.arrow(x_old, y_old, (x - x_old), (y - y_old),
                         color="C7", width=0.01, length_includes_head=True)
    ax.scatter(x, y, color=color)
    plt.savefig(os.path.join(movie_dir, "{:04d}.png".format(step)))

pi = 4 * pebbles_inside_circle / total_pebbles
print(pi)
