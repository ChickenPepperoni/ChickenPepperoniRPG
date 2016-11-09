import pygame
from chickenpepperoni import Globals

class Player(pygame.sprite.Sprite):
    def __init__(self, name):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.maxHp = Globals.InitialHP
        self.maxDp = Globals.InitialDP
        self.hp = self.maxHp
        self.dp = self.maxDp
        self.level = Globals.InitialLevel
        self.tier = Globals.PlayerTierList[Globals.TierBeginner]
        self.attack = Globals.InitialAttack
        self.defense = Globals.InitialDefense
        self.exp = 0
        self.expNeeded = Globals.ExpCurve[self.level - 1]
        self.pos = [0, 0]
        self.image = self.create_test_shape(color=(32, 32, 32))
        self.rect = self.image.get_rect()
        self.size = self.rect.size

    def create_test_shape(self, size=(32, 32), color=(255, 255, 255)):
        surface = pygame.Surface(size)
        surface.fill(color)
        surface = surface.convert()
        return surface

    def update(self):
        self.rect.topleft = self.pos

    def move_char(self, keys_pressed, rect):
        pixels = 2
        for key in keys_pressed.list:
            self.pos[0] = self.pos[0] + Globals.PlayerMovements[key][0] * pixels
            self.pos[1] = self.pos[1] + Globals.PlayerMovements[key][1] * pixels
        self.rect.move(self.pos)
        self.update()

    def levelUp(self):
        newLevel = self.level + 1
        if newLevel < Globals.MaxLevel:
            self.level = newLevel
            self.expNeeded = Globals.ExpCurve[self.level - 1]
            if newLevel == Globals.PlayerTierList[self.tier][-1] + 1:
                self.tier += 1
            self.hp = self.maxHp
        elif newLevel == Globals.MaxLevel:
            self.expNeeded = 0
        else:
            self.level = Globals.MaxLevel





