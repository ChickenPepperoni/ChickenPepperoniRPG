from chickenpepperoni.item.ItemBase import ItemBase

class ItemDP(ItemBase):
    def __init__(self, name, desc, lvl, dpGained):
        super(ItemDP, self).__init__(name, desc, lvl)
        self.dpGained = dpGained