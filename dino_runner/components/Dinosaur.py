import pygame
import os
import random

from pygame.sprite import Sprite
from dino_runner.utils.constants import (
    RUNNING, DUCKING, JUMPING, 
    RUNNING_SHIELD, DUCKING_SHIELD, JUMPING_SHIELD,
    DEFAULT_TYPE, SHIELD_TYPE, SWORD_TYPE, HAMMER_TYPE,
    DUCKING_HAMMER, RUNNING_HAMMER, JUMPING_HAMMER,
    DUCKING_SWORD, RUNNING_SWORD, JUMPING_SWORD)


class Dinosaur(Sprite):

    POS_X = 80
    POS_Y = 310
    POS_Y_DUCKING = 350
    JUMP_VEL = 8.5

    def __init__(self):
        #Initializing dino constants
        self.duck_img = {DEFAULT_TYPE: DUCKING, SHIELD_TYPE: DUCKING_SHIELD, HAMMER_TYPE: DUCKING_HAMMER, SWORD_TYPE: DUCKING_SWORD}
        self.run_img = {DEFAULT_TYPE: RUNNING, SHIELD_TYPE: RUNNING_SHIELD, HAMMER_TYPE: RUNNING_HAMMER, SWORD_TYPE: RUNNING_SWORD}
        self.jump_img = {DEFAULT_TYPE: JUMPING, SHIELD_TYPE: JUMPING_SHIELD, HAMMER_TYPE: JUMPING_HAMMER, SWORD_TYPE: JUMPING_SWORD}
        self.type = DEFAULT_TYPE
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
        self.setup_state()

        #Initializing dino sounds
        self.sonidoJump = pygame.mixer.Sound("dino_runner/utils/sounds/Boink.mp3")
        self.sonidoDuck = pygame.mixer.Sound("dino_runner/utils/sounds/Duck.mp3")
        
    def setup_state(self):
        self.has_power_up = False
        self.shield = False
        self.shield_time_up = 0
        self.sword = False
        self.sword_time_up = 0
        self.hammer = False
        self.hammer_time_up = 0
       
    def update(self, user_input):
       
        if self.dino_jump:
            self.sonidoJump.play(0)
            self.jump()
        if self.dino_duck:
            self.sonidoDuck.play(0)
            self.duck()
        else:
            if self.dino_run:
                self.run()

        #Event of dinosaur
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
        self.image = self.run_img[self.type][self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.POS_X
        self.dino_rect.y = self.POS_Y
        self.step_index += 1

    def duck(self):
        self.image = self.duck_img[self.type][self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.POS_X
        self.dino_rect.y = self.POS_Y_DUCKING
        self.step_index +=  1 

    def jump(self):
        self.image = self.jump_img[self.type]
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4 #Salto
            self.jump_vel -= 0.8 #Se baja la velocidad 
        if self.jump_vel < -self.JUMP_VEL:
            self.dino_rect.y = self.POS_Y
            self.dino_jump = False
            self.jump_vel = self.JUMP_VEL

    def draw(self, screen):
        screen.blit(self.image, self.dino_rect)

    def check_hammer(self):
        if self.hammer:
            time_to_show = round((self.hammer_time_up - pygame.time.get_ticks()) / 1000, 2)
            if not time_to_show >= 0:
                self.hammer = False
                self.update_to_default(HAMMER_TYPE)

    def check_sword(self):
        if self.sword:
            time_to_show = round((self.sword_time_up - pygame.time.get_ticks())/ 1000, 2)
            if not time_to_show >= 0:
                self.sword = False
                self.update_to_default(SWORD_TYPE)

    def check_invincibility(self):
        if self.shield:
            time_to_show = round((self.shield_time_up - pygame.time.get_ticks()) / 1000, 2)
            if not time_to_show >= 0:
                self.shield = False
                self.update_to_default(SHIELD_TYPE)
    
    def update_to_default(self, current_type):
        if self.type == current_type:
            self.type = DEFAULT_TYPE

    