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
        self.money = 0
        self.rect = pygame.Rect(64, 64, 64, 64)

    def move(self, dx, dy):
        if dx != 0:
            self.move_single_axis(dx, 0)
        if dy != 0:
            self.move_single_axis(0, dy)

    def move_single_axis(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

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





