import pygame
import numpy as np

import gestion_generation as ggen
import initialisation as init
import display as dis
from constants import BOARD_WIDTH, TOTAL_HEIGH, ROWS, COLS


# Initialiser Pygame
pygame.init()
screen = pygame.display.set_mode((BOARD_WIDTH, TOTAL_HEIGH))
pygame.display.set_caption("Jeu de la Vie")
clock = pygame.time.Clock()

# Créer une grille vide (toutes les cellules mortes)
grid = np.zeros((ROWS, COLS), dtype=int)


# Initialisation aléatoire des cellules vivantes
# random_init(grid)
init.controlled_init(grid)


# Variables de contrôle du jeu
simulation_running = False

# Boucle principale du jeu
running = True
while running:
    screen.fill((0, 0, 0))  # Remplir l'écran de noir
    dis.draw_grid(grid, screen)  # Afficher la grille
    # mettre_a_jour = True

    # Dessiner le bouton
    button_start_rect = dis.draw_start_button(screen)
    button_stop_rect = dis.draw_stop_button(screen)
    button_init_null_rect = dis.draw_initialize_null_button(screen)
    button_init_full_rect = dis.draw_initialize_button(screen)

    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.MOUSEBUTTONUP:
            if button_start_rect.collidepoint(event.pos):  # Vérifier si le clic est sur le bouton
                simulation_running = True  # Lancer la simulation
        
        if event.type == pygame.MOUSEBUTTONUP:
            if button_stop_rect.collidepoint(event.pos):  # Vérifier si le clic est sur le bouton
                simulation_running = False  # Lancer la simulation
        
        if event.type == pygame.MOUSEBUTTONUP:
            if button_init_null_rect.collidepoint(event.pos):  # Vérifier si le clic est sur le bouton
                screen.fill((0, 0, 0))
                pygame.display.flip()  # Mettre à jour l'affichage
                # mettre_a_jour = False
                simulation_running = False

        if event.type == pygame.MOUSEBUTTONUP:
            if button_init_full_rect.collidepoint(event.pos):  # Vérifier si le clic est sur le bouton
                init.controlled_init(grid)
                pygame.display.flip()  # Mettre à jour l'affichage
                # mettre_a_jour = False
                simulation_running = False

    # Si la simulation est lancée, calculer la génération suivante
    if simulation_running:
        grid = ggen.next_generation(grid)

    pygame.display.flip()  # Mettre à jour l'affichage
    clock.tick(5)  # Limiter à 10 images par seconde

pygame.quit()
