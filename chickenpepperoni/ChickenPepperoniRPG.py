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
                
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            player.move(-4, 0)
        if key[pygame.K_RIGHT]:
            player.move(4, 0)
        if key[pygame.K_UP]:
            player.move(0, -4)
        if key[pygame.K_DOWN]:
            player.move(0, 4)

        player.rect.clamp_ip(screen_rect)
        screen.fill(world.background)
        pygame.draw.rect(screen, (255, 200, 0), player.rect)
        pygame.display.flip()
        clock.tick(60)

if __name__ == '__main__':
    mainLoop()