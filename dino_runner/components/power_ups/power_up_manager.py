import random
import pygame
from dino_runner.components.power_ups.shield import Shield
from dino_runner.components.power_ups.sword import Sword
from dino_runner.components.power_ups.hammer import Hammer

class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.when_appears = 0
        self.points = 0
        self.option_numbers = list(range(1, 10))
        self.soundShield = pygame.mixer.Sound("dino_runner/utils/sounds/Shield.mp3")
        self.soundShieldCrack = pygame.mixer.Sound("dino_runner/utils/sounds/CrackShield.mp3")
        self.soundRun = pygame.mixer.Sound("dino_runner/utils/sounds/Run.mp3")

    def reset_power_ups(self, points):
        self.power_ups = []
        self.points = points
        self.when_appears = random.randint(200, 300) + self.points

    def generate_power_ups(self, points):
        self.points = points
        if len(self.power_ups) == 0:
            if self.when_appears == self.points:
                print("generating powerup")
                self.when_appears = random.randint(self.when_appears + 200, 500 + self.when_appears)
                mejora = random.randint(0, 2)
                if mejora == 1:
                    self.power_ups.append(Shield())
                elif mejora == 2:
                    self.power_ups.append(Hammer())
                elif mejora == 0:
                    self.power_ups.append(Sword())
        self.power_ups

    def update(self, points, game_speed, player):
        self.generate_power_ups(points)
        for power_up in self.power_ups:
            power_up.update(game_speed, self.power_ups)
            if player.dino_rect.colliderect(power_up.rect):
                power_up.start_time = pygame.time.get_ticks ()
                player.shield = True
                player.hammer = True
                player.sword = True
                player.type = power_up.type
                if player.shield == True:
                    self.soundShield.play(0)
                else:
                    self.soundShieldCrack.play(0)
                power_up.start_time = pygame.time.get_ticks()
                time_random = random.randrange(5, 8)
                player.shield_time_up = power_up.start_time + (time_random * 1000)
                self.power_ups.remove(power_up)


    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)