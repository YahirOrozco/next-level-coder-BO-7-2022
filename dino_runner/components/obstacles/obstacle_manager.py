import pygame
import random
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import SMALL_CACTUS, BIRD, LARGE_CACTUS


class ObstacleManager:

    def __init__(self):
        self.obstacles = []

    def update(self, game_speed, game):
        if len(self.obstacles) == 0:
            type = random.randint(0, 2)
            if type == 0:
                self.obstacles.append(Cactus(SMALL_CACTUS))
            elif type == 1:
                self.obstacles.append(Bird(BIRD))
            elif type == 2:
                self.obstacles.append(Cactus(LARGE_CACTUS))

        for obstacle in self.obstacles:
            obstacle.update(game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                if not game.player.shield:
                
                    pygame.time.delay(300)
                    game.playing = False
                    break
                else:
                    self.obstacles.pop()

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def sound(self, game):
        if self.obstacles == BIRD:
            sound_bird = pygame.mixer.Sound("dino_runner/utils/sounds/Bird.mp3")
            pygame.mixer.Sound.play(sound_bird)
        
        
