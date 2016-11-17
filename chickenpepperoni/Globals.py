import math
import pygame

# Everything relating to the main window
MainWindowW = 1280
MainWindowH = 720

# Everything relating to worlds
TestWorldBG = (255, 255, 255)

# Everything related to enemy stats
MaxLevel = 50
MaxEnemyLevel = 30
MaxEnemyHP = 100000
MaxEnemyAttack = 2000
MaxEnemyDefense = 1000

# Everything relating to the player
InitialHP = 20
InitialDP = 8
InitialLevel = 1
InitialAttack = 4
InitialDefense = 2

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

TierBeginner = 0
TierNovice = 1
TierIntermediate = 2
TierExpert = 3
TierMaster = 4

PlayerTierList = {
    TierBeginner: (1, 9),
    TierNovice: (10, 19),
    TierIntermediate: (20, 29),
    TierExpert: (30, 39),
    TierMaster: (40, 50)
}

PlayerStates = {
    "idle": 0,
    "walk-left": 1,
    "walk-right": 2,
    "walk-down": 3,
    "walk-up": 4,
    "frozen": 5
}

PlayerMovementSpeed = 4
PlayerSprintSpeed = 10

TypeHat = 0

# Everything related to battles
Ally = 0
Enemy = 1

MaxBattleSlots = 4
