import os
import pygame

from chickenpepperoni import Globals
from chickenpepperoni.player.Player import Player

class Battle:
    def __init__(self, player, enemies, bgm=('m_eboss.ogg'), bg=(255, 255, 255)):
        self.player = player
        self.enemies = enemies
        self.bgm = bgm
        self.bg = bg
        self.expTotal = 0
        self.moneyTotal = 0

    def initBattle(self):
        self.player.setState('frozen')