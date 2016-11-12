from chickenpepperoni.battle import AttackBase

class AttackMelee(AttackBase):
    def __init__(self, name, type, damage, acc=100, animation=''):
        super(AttackMelee, self).__init__(name, type, damage, acc)
        self.animation = animation