import random
from dino_runner.components.obstacles.obstacle import Obstacle

class Bird(Obstacle):
    BIRD_HEIGHTS = [250, 290, 320]

    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = random.choice(self.BIRD_HEIGHTS)

    def update(self, game_speed, obstacles):
        self.image = self.image
        self.type = 0 if self.step_index < 5 else 1
        aux_x = self.rect.x
        aux_y = self.rect.y
        self.step_index += 1

        self.rect = self.image[self,type].get_rect()
        self.rect.x = aux_x
        self.rect.y = aux_y
        self.step_index += 1

        if self.step_index >= 10:
            self.step_index = 0
        super().update(game_speed, obstacles)
