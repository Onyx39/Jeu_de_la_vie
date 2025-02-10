"""
Fichier contenant les fonctions permettant d'afficher les éléments du jeu
"""

import pygame
import numpy as np

from constantes import LARGEUR_PLATEAU, HAUTEUR_TOTAL, COLLONNES, LIGNES, TAILLE_CELLULE


def dessiner_grille(grille : np.ndarray, ecran : pygame.display) -> None :
    """
    Dessine la grille dans l'interface PyGame

    Entrées :
        grille (np.ndarray) : la grille de jeu
        ecran (pygame.display) : la fenetre d'affichage de PyGame

    Aucune sortie
    """
    for i in range(LIGNES) :
        for j in range(COLLONNES) :
            color = (0, 255, 0) if grille[i, j] == 1 else (0, 0, 0)
            pygame.draw.rect(ecran, color,
                             (j * TAILLE_CELLULE,
                              i * TAILLE_CELLULE,
                              TAILLE_CELLULE,
                              TAILLE_CELLULE))
            pygame.draw.rect(ecran, (255, 255, 255),
                             (j * TAILLE_CELLULE,
                              i * TAILLE_CELLULE,
                              TAILLE_CELLULE,
                              TAILLE_CELLULE), 1)


def dessiner_bouton_commencer(ecran : pygame.display) -> pygame.Rect :
    """
    Dessine le bouton "Commencer" dans l'interface PyGame

    Entrées :
        ecran (pygame.display) : la fenetre d'affichage de PyGame

    Sortie :
        bouton_rect (pygame.Rect) : le bouton "Commencer"
    """
    bouton_couleur = (0, 255, 0)
    bouton_rect = pygame.Rect((LARGEUR_PLATEAU - 200) // 3 - 50,
                              HAUTEUR_TOTAL - 35, 100, 30)
    pygame.draw.rect(ecran, bouton_couleur, bouton_rect)
    font = pygame.font.Font(None, 25)
    texte = font.render("Commencer", True, (255, 255, 255))
    ecran.blit(texte, ((LARGEUR_PLATEAU - 200) // 3 - texte.get_width() // 2,
                       HAUTEUR_TOTAL - 35 + texte.get_height() // 2))

    return bouton_rect

def dessiner_bouton_arreter(ecran : pygame.display) -> pygame.Rect :
    """
    Dessine le bouton "Arrêter" dans l'interface PyGame

    Entrées :
        ecran (pygame.display) : la fenetre d'affichage de PyGame

    Sortie :
        bouton_rect (pygame.Rect) : le bouton "Arrêter"
    """
    bouton_couleur = (255, 0, 0)
    bouton_rect = pygame.Rect(2*(LARGEUR_PLATEAU - 200) // 3 + 100 - 50,
                              HAUTEUR_TOTAL - 35, 100, 30)
    pygame.draw.rect(ecran, bouton_couleur, bouton_rect)
    font = pygame.font.Font(None, 25)
    texte = font.render("Arrêter", True, (255, 255, 255))
    ecran.blit(texte, (2*(LARGEUR_PLATEAU - 200) // 3 + 100 - texte.get_width() // 2,
                       HAUTEUR_TOTAL - 35 + texte.get_height() // 2))

    return bouton_rect

def dessiner_bouton_init_vide(ecran : pygame.display) -> pygame.Rect :
    """
    Dessine le bouton "Initialisation vide" dans l'interface PyGame

    Entrées :
        ecran (pygame.display) : la fenetre d'affichage de PyGame

    Sortie :
        bouton_rect (pygame.Rect) : le bouton "Initialisation vide"
    """
    bouton_couleur = (125, 125, 125)
    bouton_rect = pygame.Rect(10, HAUTEUR_TOTAL - 35, 100, 30)
    pygame.draw.rect(ecran, bouton_couleur, bouton_rect)
    font = pygame.font.Font(None, 25)
    texte = font.render("Init null", True, (255, 255, 255))
    ecran.blit(texte, (10 + texte.get_width() // 2,
                       HAUTEUR_TOTAL - 35 + texte.get_height() // 2))

    return bouton_rect

def dessiner_bouton_init(ecran : pygame.display) -> pygame.Rect :
    """
    Dessine le bouton "Initialisation controlée" dans l'interface PyGame

    Entrées :
        ecran (pygame.display) : la fenetre d'affichage de PyGame

    Sortie :
        bouton_rect (pygame.Rect) : le bouton "Initialisation controlée"
    """
    bouton_couleur = (125, 125, 125)
    bouton_rect = pygame.Rect(LARGEUR_PLATEAU - 110, HAUTEUR_TOTAL - 35, 100, 30)
    pygame.draw.rect(ecran, bouton_couleur, bouton_rect)
    font = pygame.font.Font(None, 25)
    texte = font.render("Init full", True, (255, 255, 255))
    ecran.blit(texte, (LARGEUR_PLATEAU - 110 + texte.get_width() // 2,
                       HAUTEUR_TOTAL - 35 + texte.get_height() // 2))

    return bouton_rect

def dessiner_bouton_accelerer(ecran : pygame.display) -> pygame.Rect :
    """
    Dessine le bouton "Accélérer" dans l'interface PyGame

    Entrées :
        ecran (pygame.display) : la fenetre d'affichage de PyGame

    Sortie :
        bouton_rect (pygame.Rect) : le bouton "Accélérer"
    """
    bouton_couleur = (125, 125, 0)
    bouton_rect = pygame.Rect(LARGEUR_PLATEAU // 2 - 40, HAUTEUR_TOTAL - 35, 30, 30)
    pygame.draw.rect(ecran, bouton_couleur, bouton_rect)
    font = pygame.font.Font(None, 25)
    texte = font.render("+", True, (255, 255, 255))
    ecran.blit(texte, (LARGEUR_PLATEAU // 2 - 30 + texte.get_width() // 2,
                       HAUTEUR_TOTAL - 35 + texte.get_height() // 2))

    return bouton_rect

def dessiner_bouton_ralentir(ecran : pygame.display) -> pygame.Rect :
    """
    Dessine le bouton "Ralentir" dans l'interface PyGame

    Entrées :
        ecran (pygame.display) : la fenetre d'affichage de PyGame

    Sortie :
        bouton_rect (pygame.Rect) : le bouton "Ralentir"
    """
    bouton_couleur = (0, 125, 125)
    bouton_rect = pygame.Rect(LARGEUR_PLATEAU // 2 + 10, HAUTEUR_TOTAL - 35, 30, 30)
    pygame.draw.rect(ecran, bouton_couleur, bouton_rect)
    font = pygame.font.Font(None, 25)
    texte = font.render("-", True, (255, 255, 255))
    ecran.blit(texte, (LARGEUR_PLATEAU // 2 + 30 - texte.get_width() // 2,
                       HAUTEUR_TOTAL - 35 + texte.get_height() // 2))

    return bouton_rect
