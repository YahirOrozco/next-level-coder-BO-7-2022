import pygame
import os
import random

from pygame.sprite import Sprite
from utils.constants import RUNNING

class Dinosaur(Sprite):
    def __init__(self):
        #Initializing dino constants
        self.image = RUNNING[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect_x = 80
        self.dino_rect_y = 310
       
    def update(self, userInput):
        #update of dino
        pass


    def duck():
        pass   

    def draw(self, screen):
        screen.blit(self.image, self.dino_rect)