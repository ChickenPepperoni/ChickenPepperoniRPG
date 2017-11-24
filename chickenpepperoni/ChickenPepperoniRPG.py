#hi
#revive this
import sys
import os

import pygame
from pygame.locals import *

from chickenpepperoni import Globals
from chickenpepperoni.player.Player import Player
from chickenpepperoni.battle.Battle import Battle
from chickenpepperoni.world.TestWorld import TestWorld

from chickenpepperoni.enemy import EnemyList

def mainLoop():
    pygame.mixer.pre_init(44100, -16, 2, 2048)
    pygame.init()
    icon = pygame.image.load_extended('../resources/img/pepperoni.png')
    pygame.display.set_caption('ChickenPepperoni: RPG')
    pygame.display.set_icon(icon)
    music = pygame.mixer.music
    screen = pygame.display.set_mode((Globals.MainWindowW, Globals.MainWindowH))
    screen_rect = screen.get_rect()
    player = Player('Jake')
    world = TestWorld('Test World')
    clock = pygame.time.Clock()
    allsprites = pygame.sprite.RenderPlain((player))
    if Globals.BattleTest == True:
        battle = Battle(player, [EnemyList.PepperoniMinion, EnemyList.PepperoniMinion])
        battle.initBattle()
        music.load(os.path.join('../resources/bgm/', battle.bgm))
        music.play(-1)
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit(0)
            screen.fill(battle.bg)
            pygame.display.flip()
            clock.tick(60)
    else:
        music.load(os.path.join('../resources/bgm/', 'm_grandboss.ogg'))
        music.play(-1)
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit(0)


                if player.state != Globals.PlayerStates['frozen']:
                    player.handle_keys()
                else:
                    pass

                screen.fill(world.background)
                player.draw(screen)
                pygame.display.flip()
                clock.tick(60)

if __name__ == '__main__':
    mainLoop()
