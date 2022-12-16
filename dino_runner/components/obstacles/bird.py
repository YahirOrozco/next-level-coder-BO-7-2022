import random
from dino_runner.components.obstacles.obstacle import Obstacle

class Bird(Obstacle):
    BIRD_HEIGHTS = [250, 290, 320]

    def __init__(self, image):
        self.type = random.radint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = random.choice(self.BIRD_HEIGHTS)