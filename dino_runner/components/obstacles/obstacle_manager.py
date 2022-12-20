import pygame
import random
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import SMALL_CACTUS, BIRD, LARGE_CACTUS


class ObstacleManager:

    def __init__(self):
        self.obstacles = []
        self.sonidoBird = pygame.mixer.Sound("dino_runner/utils/sounds/Bird.mp3")
        self.sonidEnd = pygame.mixer.Sound("dino_runner/utils/sounds/Ouf.mp3")
        self.sonidoChoque = pygame.mixer.Sound("dino_runner/utils/sounds/Bonk.mp3")

    def update(self, game_speed, game):
        if len(self.obstacles) == 0:
            type = random.randint(0, 2)
            if type == 0:
                self.obstacles.append(Cactus(SMALL_CACTUS))
            elif type == 1:
                self.obstacles.append(Bird(BIRD))
                self.sonidoBird.play()
            elif type == 2:
                self.obstacles.append(Cactus(LARGE_CACTUS))

        for obstacle in self.obstacles:
            obstacle.update(game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                self.sonidoChoque.play(0) #Al tener powerup y chocar, sonido de choque
                if not game.player.shield or not game.player.hammer or not game.player.sword:
                    #Si el jugador colisiona termina el juego
                    self.sonidEnd.play()
                    pygame.time.delay(300)
                    game.playing = False
                    break
                else:
                    self.obstacles.pop()

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

        
        
