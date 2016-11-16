from chickenpepperoni import Globals
from chickenpepperoni.world.WorldBase import WorldBase

class TestWorld(WorldBase):
    def __init__(self, name):
        super(TestWorld, self).__init__(name)
        self.background = Globals.TestWorldBG