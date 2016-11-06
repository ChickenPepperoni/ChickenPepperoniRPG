import pygame

# Everything relating to the main window
MainWindowW = 1280
MainWindowH = 720

# Everything related to enemy stats
MaxLevel = 50
MaxEnemyLevel = 30
EnemyLevel = "Level %s"
EnemyLevelElite = "Level %s Elite"
MaxEnemyHP = 100000
MaxEnemyAttack = 2000
MaxEnemyDefense = 1000

# Everything relating to the player
DisallowedNames = ['shit flavored hot dog man', 'traphouse lord', 'brendan dolan']
PlayerMovements = {
    pygame.K_LEFT: (-1, 0),
    pygame.K_RIGHT: (1, 0),
    pygame.K_UP: (0, -1),
    pygame.K_DOWN: (0, 1)
}
