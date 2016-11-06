import sys

import pygame
from pygame.locals import *

from chickenpepperoni import Globals
from chickenpepperoni.player import Player
from chickenpepperoni.world import TestWorld

def mainLoop():
    pygame.init()
    screen = pygame.display.set_mode((Globals.MainWindowW, Globals.MainWindowH))
    player = Player.Player('Jake')
    allsprites = pygame.sprite.RenderPlain((player))
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type == KEYDOWN:
                pass
				# i dont fuckign know how to use pygame
            else:
                pass

if __name__ == '__main__':
    mainLoop()