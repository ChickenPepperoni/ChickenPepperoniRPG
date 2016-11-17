import sys
import os

import pygame
from pygame.locals import *

from chickenpepperoni import Globals
from chickenpepperoni.player.Player import Player
from chickenpepperoni.world.TestWorld import TestWorld

def mainLoop():
    pygame.mixer.pre_init(44100, -16, 2, 2048)
    pygame.init()
    icon = pygame.image.load_extended('../resources/img/pepperoni.png')
    pygame.display.set_caption('ChickenPepperoni: RPG')
    pygame.display.set_icon(icon)
    music = pygame.mixer.music
    music.load(os.path.join('../resources/bgm/', 'm_grandboss.ogg'))
    music.play(-1)
    screen = pygame.display.set_mode((Globals.MainWindowW, Globals.MainWindowH))
    screen_rect = screen.get_rect()
    player = Player('Jake')
    world = TestWorld('Test World')
    clock = pygame.time.Clock()
    allsprites = pygame.sprite.RenderPlain((player))
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)
                
        player.handle_keys()

        screen.fill(world.background)
        player.draw(screen)
        pygame.display.flip()
        clock.tick(60)

if __name__ == '__main__':
    mainLoop()