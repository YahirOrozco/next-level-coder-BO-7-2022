import pygame
import os
import random
from utils import constants

class Dinosaur():
    def __init__(self):
        #Initializing dino constants
        #Running constants
        self.run_img = constants.RUNNING
        self.rshiel_img = constants.RUNNING_SHIELD
        self.rhammer_img = constants.RUNNING_HAMMER
        #Jump constants
        self.jump_img = constants.JUMPING
        self.j_shield_img = constants.JUMPING_SHIELD
        self.j_hammer = constants.JUMPING_HAMMER
        #Duck constants
        self.duck_img = constants.DUCKING
        self.d_hammer = constants.DUCKING_HAMMER
        self.d_shield = constants.DUCKING_SHIELD
        #Events
        self.dino_duck = False
        self.dino_run = True
        self.dino_jump = False

        self.spet_index = 0 #Initializing the steps to 0 
        self.jump_vel = self.JUMP_VEL
        self.image = self.run_img[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS

    def update():
        pass

    def draw():
        pass