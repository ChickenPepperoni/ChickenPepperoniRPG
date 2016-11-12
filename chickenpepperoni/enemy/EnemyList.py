from chickenpepperoni.enemy.EnemyPepperoni import EnemyPepperoni

'''
Define all the enemies here.

ARGS: ('NAME', HP, LEVEL, ATTACK, DEFENSE, EXP, MONEY, ELITE/BOSS=TRUE/FALSE)
'''

# Pepperoni Enemies
PepperoniMinion = EnemyPepperoni('Pepperoni Minion', 10, 1, 2, 0, 3, 2)
PepperoniGuard = EnemyPepperoni('Pepperoni Guard', 15, 1, 3, 0, 5, 3, elite=True)
PepperoniBoss = EnemyPepperoni('The Masked Pepperoni', 50, 3, 7, 2, 30, 20, boss=True)