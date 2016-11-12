class AttackBase:
    def __init__(self, name, type, damage, acc):
        self.name = name
        self.type = type
        self.damage = damage
        self.acc = acc

    def calculateDamage(self, damage, defense):
        if not damage <= defense:
            damage = damage * damage / defense
        else:
            damage = 0
        return damage