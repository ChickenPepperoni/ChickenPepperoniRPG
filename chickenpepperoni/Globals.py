import pygame

# Everything relating to the main window
MainWindowW = 1280
MainWindowH = 720

# Everything relating to the player
PlayerMovements = {
    pygame.K_LEFT: (-1, 0),
    pygame.K_RIGHT: (1, 0),
    pygame.K_UP: (0, -1),
    pygame.K_DOWN: (0, 1)
}