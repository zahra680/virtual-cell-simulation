import numpy as np
from scipy.spatial.distance import euclidean

def simulate_diffusion(positions, cell_radius, max_steps):
    history = [positions.copy()]
    for step in range(max_steps):
        new_positions = positions + np.random.normal(0, 0.3, positions.shape)
        for i in range(len(new_positions)):
            dist = euclidean(new_positions[i], [0, 0])
            if dist >= cell_radius:
                direction = -new_positions[i] / dist
                new_positions[i] += direction * 0.5
        positions = new_positions
        history.append(positions.copy())
    return history