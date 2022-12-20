from dino_runner.components.power_ups.power_up import PowerUp
from dino_runner.utils.constants import WOOD_SHIELD, WOOD_TYPE

class Wood_shield(PowerUp):
    def __init__(self):
        self.image = WOOD_SHIELD
        self.type = WOOD_TYPE
        super().__init__(self.image, self.type)