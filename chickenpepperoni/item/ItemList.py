from chickenpepperoni.item.ItemHeal import ItemHeal
from chickenpepperoni.item.ItemDP import ItemDP
from chickenpepperoni.item.ItemAttack import ItemAttack

# Healing items
Chicken = ItemHeal('Chicken', "A piece of chicken. Restores 20 HP.", 1, 20)
ChickenClub = ItemHeal('Chicken Club', "A chicken club. Restores 50 HP.", 6, 50)
ChickenBucket = ItemHeal('Bucket of Chicken', "A bucket of chicken - filled to the brim! Restores 120 HP.", 15, 120)

# DP recovery items
SmallDew = ItemDP('Small Dew', "A small, but refreshing cup of Dew. Restores 10 DP.", 1, 10)
MediumDew = ItemDP('Medium Dew', "An average sized cup of Dew. Restores 25 DP.", 4, 25)
LargeDew = ItemDP('Large Dew', "A large cup of Dew! Restores 50 DP.", 12, 50)

# Attack items
ChickenRage = ItemAttack('Chicken Rage', "A flock of raging chickens stampedes an enemy. Deals 15 base damage.", 3, dmgOne=15)
ChickenSwarm = ItemAttack('Chicken Swarm', "Chickens swarm the enemies! Deals 25 base damage to all enemies.", 8, dmgAll=25)