from pygame.sprite import Sprite
from dino_runner.utils.constants import SCREEN_WIDTH

class Obstacle(Sprite):

    #constructor method
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH - 70

    def update(self, game_speed, obstacles):
        self.rect.x -= game_speed
        if self.rect.x < 0:
            obstacles.pop()
        else:
            pass #Por si se llega a quedar sin obstaculos, no se cierre el juego
    
    def draw(self, screen):
        screen.blit(self.image[self.type], self.rect)