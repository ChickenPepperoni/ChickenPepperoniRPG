import pygame
from chickenpepperoni import Globals

class Player(pygame.sprite.Sprite):
    def __init__(self, name):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.hp = Globals.InitialHP
        self.level = Globals.InitialLevel
        self.attack = Globals.InitialAttack
        self.defense = Globals.InitialDefense
        self.exp = 0
        self.expNeeded = Globals.ExpCurve[self.level - 1]
        self.pos = [0, 0]
        self.image = self.create_test_shape()
        self.rect = self.image.get_rect()
        self.size = self.rect.size

    def update(self):
        self.rect.topleft = self.pos

    def move_char(self, keys_pressed, rect):
        pixels = 2
        for key in keys_pressed.list:
            self.pos[0] = self.pos[0] + Globals.PlayerMovements[key][0] * pixels
            self.pos[1] = self.pos[1] + Globals.PlayerMovements[key][1] * pixels
        self.rect.move(self.pos)
        self.update()

    def create_test_shape(self, size=(32, 32), color=(255, 255, 255)):
        surface = pygame.Surface(size)
        surface.fill(color)
        surface = surface.convert()
        return surface


