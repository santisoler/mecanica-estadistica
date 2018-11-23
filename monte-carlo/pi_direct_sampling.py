import numpy as np


total_pebbles = 100
pebbles_inside_circle = 0
for step in range(total_pebbles):
    x, y = 2 * np.random.rand(2) - 1
    distance_sq = x**2 + y**2
    if distance_sq <= 1:
        pebbles_inside_circle += 1
pi = 4 * pebbles_inside_circle / total_pebbles
print(pi)
