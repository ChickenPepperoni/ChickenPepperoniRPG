import pygame

class WorldBase:
    def __init__(self):
        self.background = None

    def set_background(self, screen, color = (0, 0, 0)):
        background = pygame.Surface(screen.get_size())
        background.fill(color)
        background = background.convert()
        screen.blit(background, (0, 0))
        return background

