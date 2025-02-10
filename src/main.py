"""
Fichier principal, exécutable
"""

import pygame
import numpy as np

import gestion_generation as ggen
import initialisation as init
import affichage as aff
from constantes import LARGEUR_PLATEAU, HAUTEUR_PLATEAU, HAUTEUR_TOTAL, COLLONNES, LIGNES


# Initialiser Pygame
pygame.init()
ecran = pygame.display.set_mode((LARGEUR_PLATEAU, HAUTEUR_TOTAL))
pygame.display.set_caption("Jeu de la Vie")
horloge = pygame.time.Clock()

# Créer une grille vide
grille = np.zeros((LIGNES, COLLONNES), dtype=int)

# Initialisation des cellules vivantes
init.initialisation_controlee(grille)

# Variables de contrôle du jeu
SIMULATION_EN_COURS = False
VITESSE_SIMULATION = 5

# Boucle principale du jeu
ACTIVE = True
while ACTIVE:
    ecran.fill((0, 0, 0))
    aff.dessiner_grille(grille, ecran)

    # Dessiner les boutons
    bouton_commencer_rect = aff.dessiner_bouton_commencer(ecran)
    bouton_arreter_rect = aff.dessiner_bouton_arreter(ecran)
    bouton_init_vide_rect = aff.dessiner_bouton_init_vide(ecran)
    bouton_init_rect = aff.dessiner_bouton_init(ecran)
    bouton_accelerer_rect = aff.dessiner_bouton_accelerer(ecran)
    bouton_ralentir_rect = aff.dessiner_bouton_ralentir(ecran)

    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ACTIVE = False

        if event.type == pygame.MOUSEBUTTONUP:
            if bouton_commencer_rect.collidepoint(event.pos) :
                SIMULATION_EN_COURS = True

            elif bouton_arreter_rect.collidepoint(event.pos) :
                SIMULATION_EN_COURS = False

            elif bouton_init_vide_rect.collidepoint(event.pos) :
                grille.fill(0)
                aff.dessiner_grille(grille, ecran)
                SIMULATION_EN_COURS = False

            elif bouton_init_rect.collidepoint(event.pos) :
                init.initialisation_controlee(grille)
                aff.dessiner_grille(grille, ecran)
                SIMULATION_EN_COURS = False

            elif bouton_accelerer_rect.collidepoint(event.pos) :
                VITESSE_SIMULATION += 1

            elif bouton_ralentir_rect.collidepoint(event.pos) :
                VITESSE_SIMULATION -= 1

            # Gérer les clics sur la grille pour changer l'état des cellules
            elif not SIMULATION_EN_COURS :
                LARGEUR_CELLULE = LARGEUR_PLATEAU // COLLONNES
                HAUTEUR_CELLULE = HAUTEUR_PLATEAU // LIGNES
                x, y = event.pos

                colonne = x // LARGEUR_CELLULE
                ligne = y // HAUTEUR_CELLULE

                if grille[ligne, colonne] == 0 :
                    grille[ligne, colonne] = 1
                else :
                    grille[ligne, colonne] = 0

                aff.dessiner_grille(grille, ecran)


    # Si la simulation est lancée, calculer la génération suivante
    if SIMULATION_EN_COURS:
        grille = ggen.prochaine_generation(grille)

    pygame.display.flip()
    horloge.tick(VITESSE_SIMULATION)

pygame.quit()
