import pygame
import os
import random

from pygame.sprite import Sprite
from dino_runner.utils.constants import RUNNING

class Dinosaur(Sprite):
    def __init__(self):
        #Initializing dino constants
        self.image = RUNNING[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect_x = self.POS_X
        self.dino_rect_y = self.POS_Y
        self.step_index = 0
       
    def update(self, userInput):
        self.run()
        #update of steps
        if self.step_index >= 10:
            self.step_index = 0

    def run(self):
        self.image = RUNNING[0] if self.step_index < 5 else RUNNING[1]
        self.dino_rect = self.image.get_rect()
        self.dino_rect_x = self.POS_X
        self.dino_rect_y = self.POS_Y
        self.step_index += 1



    def duck():
        pass   

    def draw(self, screen):
        screen.blit(self.image, self.dino_rect)