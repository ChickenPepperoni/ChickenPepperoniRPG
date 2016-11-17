from chickenpepperoni.item.ItemBase import ItemBase

class ItemAttack(ItemBase):
    def __init__(self, name, desc, lvl, dmgOne=0, dmgAll=0):
        super(ItemAttack, self).__init__(name, desc, lvl)
        self.dmgOne = dmgOne
        self.dmgAll = dmgAll