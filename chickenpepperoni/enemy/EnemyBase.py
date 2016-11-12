import random

from chickenpepperoni import Globals

class EnemyBase:
    def __init__(self, name, hp, level, attack, defense, exp, money, elite=False, boss=False):
        self.name = name
        self.elite = elite
        self.boss = boss
        self.hp = hp
        self.level = level
        self.attack = attack
        self.defense = defense
        self.exp = exp
        self.money = money
