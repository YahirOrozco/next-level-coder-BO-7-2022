import random
from dino_runner.utils.constants import CLOUD

class Cloud:
    POS_X = [100, 300, 500, 800]
    POS_Y = [50, 90, 100]
    def __init__(self):
        self.image = CLOUD
        self.image_width = self.image.get_width()
        self.x_pos = self.POS_X
        self.y_pos = self.POS_Y
        self.game_speed = 50
    
    def update(self):
        self.x_pos = self.game_speed
        if self.x_pos <= self.image_width:
            self.x_pos = self.image_width + random.choice(self.POS_X)
            self.y_pos = random.choice(self.POS_Y)
    def draw(self, screen):
        screen.blit(self.image, (self.x_pos, self.y_pos))

