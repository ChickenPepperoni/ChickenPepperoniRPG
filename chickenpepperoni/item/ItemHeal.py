from chickenpepperoni.item.ItemBase import ItemBase

class ItemHeal(ItemBase):
    def __init__(self, name, desc, lvl, hpGained):
        super(ItemHeal, self).__init__(name, desc, lvl)
        self.hpGained = hpGained