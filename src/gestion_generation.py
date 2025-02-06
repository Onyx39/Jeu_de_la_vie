import numpy as np

from constants import ROWS, COLS

def next_generation(grid):
    new_grid = np.zeros_like(grid)

    for i in range(ROWS):
        for j in range(COLS):
            # Calcul des voisins
            total = int((grid[i, (j-1)%COLS] + grid[i, (j+1)%COLS] +  # Ligne précédente et suivante
                         grid[(i-1)%ROWS, j] + grid[(i+1)%ROWS, j] +  # Colonne précédente et suivante
                         grid[(i-1)%ROWS, (j-1)%COLS] + grid[(i-1)%ROWS, (j+1)%COLS] +  # Diagonales
                         grid[(i+1)%ROWS, (j-1)%COLS] + grid[(i+1)%ROWS, (j+1)%COLS]))

            # Application des règles du jeu de la vie
            if grid[i, j] == 1 and (total == 2 or total == 3):
                new_grid[i, j] = 1  # La cellule reste vivante
            elif grid[i, j] == 0 and total == 3:
                new_grid[i, j] = 1  # La cellule devient vivante

    return new_grid