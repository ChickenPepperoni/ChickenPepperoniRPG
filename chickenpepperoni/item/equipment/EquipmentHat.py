from chickenpepperoni.item.equipment.EquipmentBase import EquipmentBase

class EquipmentHat(EquipmentBase):
    def __init__(self, name, type, desc, lvl, stats=(0, 0, 0, 0)):
        super(EquipmentHat, self).__init__(name, type, desc, lvl, stats)
        self.equipSlot = 0