class EquipmentBase:
    def __init__(self, name, type, desc, lvl, stats=(0, 0, 0, 0)):
        self.name = name
        self.type = type
        self.desc = desc
        self.lvl = lvl
        self.stats = stats