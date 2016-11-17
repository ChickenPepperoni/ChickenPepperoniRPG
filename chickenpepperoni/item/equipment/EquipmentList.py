from chickenpepperoni import Globals
from chickenpepperoni.item.equipment.EquipmentHat import EquipmentHat

'''
Define all the equipment here.

ARGS: ('NAME', TYPE, DESCRIPTION, LEVEL, STATS=(HP, DP, ATK, DEF))
'''

BasicChickenMask = EquipmentHat('Basic Chicken Mask', Globals.TypeHat, "A basic chicken mask.", 1, stats=(0, 0, 0, 0))
AdvancedChickenMask = EquipmentHat('Advanced Chicken Mask', Globals.TypeHat, "An advanced chicken mask.", 4, stats=(2, 1, 2, 1))