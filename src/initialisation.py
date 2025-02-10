"""
Fichier contenant les fontions permettant d'initialiser le jeu
"""

import numpy as np

from constantes import LIGNES, COLLONNES

def initialisation_aleatoire(grille : np.ndarray) -> None:
    """
    Initialise de manière aléatoire la grille du jeu

    Entrée :
        grille (np.ndarray) : la grille du jeu

    Aucune sortie
    """
    grille.fill(0)
    for i in range(LIGNES) :
        for j in range(COLLONNES) :
            grille[i, j] = np.random.choice([0, 1])

def initialisation_controlee(grille : np.ndarray) -> None:
    """
    Initialise manuellement la grille du jeu

    Entrée :
        grille (np.ndarray) : la grille du jeu

    Aucune sortie
    """
    grille.fill(0)
    # clignotant
    # grille[2, 2] = 1
    # grille[2, 3] = 1
    # grille[2, 4] = 1

    # grenouille
    # grille[7, 5] = 1
    # grille[7, 6] = 1
    # grille[7, 7] = 1
    # grille[8, 6] = 1
    # grille[8, 7] = 1
    # grille[8, 8] = 1

    # planeur
    # grille [1, 0] = 1
    # grille [2, 1] = 1
    # grille [0, 2] = 1
    # grille [1, 2] = 1
    # grille [2, 2] = 1

    # canon Gosper Glider Gun.
    grille[0, 4] = 1
    grille[0, 5] = 1
    grille[1, 4] = 1
    grille[1, 5] = 1
    grille[10, 4] = 1
    grille[10, 5] = 1
    grille[10, 6] = 1
    grille[11, 3] = 1
    grille[11, 7] = 1
    grille[12, 2] = 1
    grille[12, 8] = 1
    grille[13, 2] = 1
    grille[13, 8] = 1
    grille[14, 5] = 1
    grille[15, 3] = 1
    grille[15, 7] = 1
    grille[16, 4] = 1
    grille[16, 5] = 1
    grille[16, 6] = 1
    grille[17, 5] = 1
    grille[20, 2] = 1
    grille[20, 3] = 1
    grille[20, 4] = 1
    grille[21, 2] = 1
    grille[21, 3] = 1
    grille[21, 4] = 1
    grille[22, 1] = 1
    grille[22, 5] = 1
    grille[24, 0] = 1
    grille[24, 1] = 1
    grille[24, 5] = 1
    grille[24, 6] = 1
    grille[34, 2] = 1
    grille[34, 3] = 1
    grille[35, 2] = 1
    grille[35, 3] = 1
