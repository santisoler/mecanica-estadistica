import numpy as np

total_pebbles = 1000
delta = 0.2

x, y = 1., 1.
pebbles_inside_circle = 0
for step in range(total_pebbles):
    # Generamos desplazamientos aleatorios entre [-delta, delta]
    delta_x, delta_y = np.random.uniform(low=-delta, high=delta, size=2)
    # Aceptamos el nuevo salto si cae dentro del cuadrado
    if np.abs(x + delta_x) < 1 and np.abs(y + delta_y) < 1:
        x, y = x + delta_x, y + delta_y
    distance_sq = x**2 + y**2
    if distance_sq < 1:
        pebbles_inside_circle += 1

pi = 4 * pebbles_inside_circle / total_pebbles
print(pi)
