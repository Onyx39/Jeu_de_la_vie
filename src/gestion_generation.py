"""
Fichier contenant les fonctions permettant de déterminer la génération suivante
"""

import numpy as np

from constantes import LIGNES, COLLONNES

def prochaine_generation(grille : np.ndarray) -> np.ndarray :
    """
    Génére la prochaine génération de la grille

    Entrée :
        grille (np.ndarray)  : la grille actuelle

    Sortie :
        nouvelle_grille (np.ndarray) : la grille de la prochaine génération
    """
    nouvelle_grille = np.zeros_like(grille)

    for i in range(LIGNES) :
        for j in range(COLLONNES) :
            total = 0
            # Calcul des voisins seulement si la cellule est dans le tableau
            for di in [-1, 0, 1] :
                for dj in [-1, 0, 1] :
                    if di == 0 and dj == 0 :
                        continue
                    ni, nj = i + di, j + dj
                    if 0 <= ni < LIGNES and 0 <= nj < COLLONNES :
                        total += grille[ni, nj]

            # Application des règles du jeu de la vie
            if grille[i, j] == 1 and (total in (2, 3)) :
                nouvelle_grille[i, j] = 1
            elif grille[i, j] == 0 and total == 3 :
                nouvelle_grille[i, j] = 1

    return nouvelle_grille
