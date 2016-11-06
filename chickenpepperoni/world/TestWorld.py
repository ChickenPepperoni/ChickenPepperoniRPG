from chickenpepperoni.world import WorldBase

class TestWorld(WorldBase):
    def __init__(self, screen):
        self.background = self.set_background(screen, (255, 255, 255))