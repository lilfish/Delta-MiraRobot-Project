import pygame
import os
import time

import easingScripts

ALPHA = (0,255,0)
ani = 4   

class Image(pygame.sprite.Sprite):

    trajectory_x = []
    trajectory_y = []
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.movex = 0
        self.movey = 0
        self.frame = 0
        self.images = []
        self.animationFin = True
        
    def load_image(self, path):
        img = pygame.image.load(path).convert()
        img.convert_alpha()
        img.set_colorkey(ALPHA)
        self.images.append(img)
        self.image = self.images[0]
        self.rect  = self.image.get_rect()
        self.rect.topleft = (0,0)   

    def build_trajectory_to(self, target_x, target_y, frame_rate):
        current_x = self.rect.x
        current_y = self.rect.y 
            
        for i in range (0, frame_rate):
            p = i + 1
            self.trajectory_x.append(easingScripts.easeInOutQuint(
                1, current_x, target_x - current_x, p
            ))
            self.trajectory_y.append(easingScripts.easeInOutQuint(
                1, current_y, target_y - current_y, p
            ))
        self.trajectory_x.reverse()
        self.trajectory_y.reverse()
        self.animationFin = False
    
    def update(self, fps):
        if (not self.animationFin):
            self.rect.x = self.trajectory_x[self.frame]
            self.rect.y = self.trajectory_y[self.frame]
            self.frame += 1
            if (self.frame == fps):
                self.trajectory_x = []
                self.trajectory_y = []
                self.frame = 0
                self.animationFin = True