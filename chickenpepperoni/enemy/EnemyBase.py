import random

from chickenpepperoni import Globals

class EnemyBase:
    def __init__(self, name, hp, level, attack, defense, exp, elite=False):
        self.name = name
        self.elite = elite
        self.hp = hp
        self.level = level
        self.attack = attack
        self.defense = defense
        self.exp = exp
