from chickenpepperoni.enemy import EnemyBase

class EnemyPepperoni(EnemyBase):
    def __init__(self, name, hp, level, attack, defense, exp, money, elite=False, boss=False):
        super(EnemyPepperoni, self).__init__(name, hp, level, attack, defense, exp, money, elite=False, boss=False)