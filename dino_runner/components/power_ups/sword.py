from dino_runner.components.power_ups.power_up import PowerUp
from dino_runner.utils.constants import SWORD, SWORD_TYPE

class Sword(PowerUp):
    def __init__(self):
        self.image = SWORD
        self.type = SWORD_TYPE
        super().__init__(self.image, self.type)