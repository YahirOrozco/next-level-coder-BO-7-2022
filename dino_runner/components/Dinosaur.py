import pygame
import os
import random

from pygame.sprite import Sprite
from dino_runner.utils.constants import RUNNING, DUCKING, JUMPING

class Dinosaur(Sprite):

    POS_X = 80
    POS_Y = 310
    POS_Y_DUCKING = 350
    JUMP_VEL = 8.5

    def __init__(self):
        #Initializing dino constants
        self.image = RUNNING[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.POS_X
        self.dino_rect.y = self.POS_Y
        self.step_index = 0
        #Setting the initial values of dino
        self.dino_run = True
        self.dino_duck = False
        self.dino_jump = False
        self.jump_vel = self.JUMP_VEL
       
    def update(self, user_input):
       
        if self.dino_jump:
            self.jump()
        if self.dino_duck:
            self.duck()
        else:
            if self.dino_run:
                self.run()

        #Event of duck 
        if user_input[pygame.K_DOWN]and not self.dino_jump:
            self.dino_run = False
            self.dino_duck = True
            self.dino_jump = False
        elif user_input[pygame.K_UP] and not self.dino_jump: #Event of jump
            self.dino_run = False
            self.dino_duck = False
            self.dino_jump = True
        elif not self.dino_jump:    #Event of run
            self.dino_run = True
            self.dino_duck = False
            self.dino_jump = False

         #update of steps
        if self.step_index >= 10:
            self.step_index = 0

    def run(self):
        self.image = RUNNING[0] if self.step_index < 5 else RUNNING[1]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.POS_X
        self.dino_rect.y = self.POS_Y
        self.step_index += 1

    def duck(self):
        self.image = DUCKING[0] if self.step_index < 5 else RUNNING[1]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.POS_X
        self.dino_rect.y = self.POS_Y_DUCKING
        self.step_index +=  1 

    def jump(self):
        self.image = JUMPING
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4 #Salto
            self.jump_vel -= 0.8 #Se baja la velocidad 
        if self.jump_vel < -self.JUMP_VEL:
            self.dino_rect.y = self.POS_Y
            self.dino_jump = False
            self.jump_vel = self.JUMP_VEL

    def draw(self, screen):
        screen.blit(self.image, self.dino_rect)

    def sound(self, game):
        sound_jump = pygame.mixer.Sound("dino_runner/utils/sounds/Jump.mp3")
        sound_duck = pygame.mixer.Sound("dino_runner/utils/sounds/Duck.mp3")
        if self.dino_jump:
            pygame.mixer.Sound.play(sound_jump)
        
        if self.dino_duck:
            pygame.mixer.Sound.play(sound_duck)