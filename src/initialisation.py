import numpy as np

from constants import ROWS, COLS

# Fonction pour initialiser quelques cellules vivantes
def random_init(grid):
    for i in range(ROWS):
        for j in range(COLS):
            grid[i, j] = np.random.choice([0, 1])  # Cellule morte (0) ou vivante (1)

def controlled_init(grid):
    # clignotant
    # grid[2, 2] = 1
    # grid[2, 3] = 1
    # grid[2, 4] = 1

    # grenouille
    # grid[7, 5] = 1
    # grid[7, 6] = 1
    # grid[7, 7] = 1
    # grid[8, 6] = 1
    # grid[8, 7] = 1
    # grid[8, 8] = 1

    # planeur
    # grid [1, 0] = 1
    # grid [2, 1] = 1
    # grid [0, 2] = 1
    # grid [1, 2] = 1
    # grid [2, 2] = 1

    # canon Gosper Glider Gun.
    grid[0, 4] = 1
    grid[0, 5] = 1
    grid[1, 4] = 1
    grid[1, 5] = 1
    grid[10, 4] = 1
    grid[10, 5] = 1
    grid[10, 6] = 1
    grid[11, 3] = 1
    grid[11, 7] = 1
    grid[12, 2] = 1
    grid[12, 8] = 1
    grid[13, 2] = 1
    grid[13, 8] = 1
    grid[14, 5] = 1
    grid[15, 3] = 1
    grid[15, 7] = 1
    grid[16, 4] = 1
    grid[16, 5] = 1
    grid[16, 6] = 1
    grid[17, 5] = 1
    grid[20, 2] = 1
    grid[20, 3] = 1
    grid[20, 4] = 1
    grid[21, 2] = 1
    grid[21, 3] = 1
    grid[21, 4] = 1
    grid[22, 1] = 1
    grid[22, 5] = 1
    grid[24, 0] = 1
    grid[24, 1] = 1
    grid[24, 5] = 1
    grid[24, 6] = 1
    grid[34, 2] = 1
    grid[34, 3] = 1
    grid[35, 2] = 1
    grid[35, 3] = 1
    # grid[0, 0] = 1