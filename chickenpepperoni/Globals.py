import math
import pygame

# Everything relating to the main window
MainWindowW = 1280
MainWindowH = 720

# Everything related to enemy stats
MaxLevel = 50
MaxEnemyLevel = 30
MaxEnemyHP = 100000
MaxEnemyAttack = 2000
MaxEnemyDefense = 1000

# Everything relating to the player
ExpCurveBase = 4
ExpCurveMult = 2.0

def createExpCurve(base, mult):
    baseValue = base
    valueMultiply = mult
    level = 1
    levelMult = level + 1
    Exp2Level = []
    while len(Exp2Level) < MaxLevel:
        expValue = baseValue + level
        expValue *= levelMult
        Exp2Level.append(expValue)
        level += 1
        levelMult += 1
        try:
            levelStr = str(level)
            if levelStr[1] == '0':
                baseValue = baseValue * valueMultiply
                baseValue = math.ceil(baseValue)
        except:
            pass
    return Exp2Level

ExpCurve = createExpCurve(ExpCurveBase, ExpCurveMult)

PlayerMovements = {
    pygame.K_LEFT: (-1, 0),
    pygame.K_RIGHT: (1, 0),
    pygame.K_UP: (0, -1),
    pygame.K_DOWN: (0, 1)
}
