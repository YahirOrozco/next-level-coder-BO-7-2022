from dino_runner.components.power_ups.power_up import PowerUp
from dino_runner.utils.constants import SHOES, SHOES_TYPE

class Shoes(PowerUp):
    def __init__(self):
        self.image = SHOES
        self.type = SHOES_TYPE
        super().__init__(self.image, self.type)

        