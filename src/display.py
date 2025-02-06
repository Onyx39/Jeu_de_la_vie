import pygame

from constants import ROWS, COLS, CELL_SIZE, BOARD_WIDTH, BOARD_HEIGHT, TOTAL_HEIGH


# Fonction pour afficher la grille
def draw_grid(grid, screen):
    for i in range(ROWS):
        for j in range(COLS):
            color = (0, 255, 0) if grid[i, j] == 1 else (0, 0, 0)
            pygame.draw.rect(screen, color, (j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(screen, (255, 255, 255), (j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)

# Fonction pour dessiner le bouton
def draw_start_button(screen):
    button_color = (0, 255, 0)
    button_rect = pygame.Rect((BOARD_WIDTH - 200) // 3 - 50, TOTAL_HEIGH - 35, 100, 30)
    pygame.draw.rect(screen, button_color, button_rect)
    font = pygame.font.Font(None, 25)
    text = font.render("Commencer", True, (255, 255, 255))
    screen.blit(text, ((BOARD_WIDTH - 200) // 3 - text.get_width() // 2, TOTAL_HEIGH - 35 + text.get_height() // 2))

    return button_rect

# Fonction pour dessiner le bouton
def draw_stop_button(screen):
    button_color = (255, 0, 0)
    button_rect = pygame.Rect(2*(BOARD_WIDTH - 200) // 3 + 100 - 50, TOTAL_HEIGH - 35, 100, 30)
    pygame.draw.rect(screen, button_color, button_rect)
    font = pygame.font.Font(None, 25)
    text = font.render("Arrêter", True, (255, 255, 255))
    screen.blit(text, (2*(BOARD_WIDTH - 200) // 3 + 100 - text.get_width() // 2, TOTAL_HEIGH - 35 + text.get_height() // 2))

    return button_rect

def draw_initialize_null_button(screen):
    button_color = (125, 125, 125)
    button_rect = pygame.Rect(10, TOTAL_HEIGH - 35, 100, 30)
    pygame.draw.rect(screen, button_color, button_rect)
    font = pygame.font.Font(None, 25)
    text = font.render("Init null", True, (255, 255, 255))
    screen.blit(text, (10 + text.get_width() // 2, TOTAL_HEIGH - 35 + text.get_height() // 2))

    return button_rect

def draw_initialize_button(screen):
    button_color = (125, 125, 125)
    button_rect = pygame.Rect(BOARD_WIDTH - 110, TOTAL_HEIGH - 35, 100, 30)
    pygame.draw.rect(screen, button_color, button_rect)
    font = pygame.font.Font(None, 25)
    text = font.render("Init full", True, (255, 255, 255))
    screen.blit(text, (BOARD_WIDTH - 110 + text.get_width() // 2, TOTAL_HEIGH - 35 + text.get_height() // 2))

    return button_rect