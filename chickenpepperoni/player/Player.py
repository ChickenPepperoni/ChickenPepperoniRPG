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
        self.image = pygame.image.load_extended('../resources/img/pepperoni.png')
        self.x = 0
        self.y = 0

    def handle_keys(self):
        key = pygame.key.get_pressed()
        dist = Globals.PlayerMovementSpeed
        if key[pygame.K_DOWN]:
            self.y += dist
        elif key[pygame.K_UP]:
            self.y -= dist
        if key[pygame.K_RIGHT]:
            self.x += dist
        elif key[pygame.K_LEFT]:
            self.x -= dist

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

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





