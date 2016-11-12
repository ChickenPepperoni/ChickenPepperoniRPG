from chickenpepperoni import Globals

class Battle:
    def __init__(self, allies, enemies):
        self.allies = allies
        self.alliesDefeated = {}
        self.enemies = enemies
        self.enemiesDefeated = []
        self.allySlots = len(self.allies)
        self.enemySlots = len(self.enemies)
        self.expCount = 0
        self.moneyCount = 0

    def getNextSlot(self, type):
        maxSlots = Globals.MaxBattleSlots
        if type == Globals.Ally:
            currentSlots = len(self.allies)
        elif type == Globals.Enemy:
            currentSlots = len(self.enemies)
        if currentSlots < maxSlots:
            nextSlot = currentSlots + 1
        else:
            nextSlot = None
        return nextSlot

    def declareDefeat(self, entity):
        if entity in self.allies:
            self.allies.pop(entity, None)
            self.alliesDefeated[entity] = self.getNextSlot(Globals.Ally)
        elif entity in self.enemies:
            self.enemies.pop(entity, None)
            self.enemiesDefeated.append(entity)
            self.expCount += entity.exp
            self.moneyCount += entity.money
            