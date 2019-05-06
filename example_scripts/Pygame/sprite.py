import pygame
import os
import time

ALPHA = (0,255,0)
ani = 4   

class Player(pygame.sprite.Sprite):
    '''
    Spawn a player
    '''
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.movex = 0
        self.movey = 0
        self.frame = 0
        self.images = []
        
        for i in range(1,5):
            img = pygame.image.load('giphy.gif').convert()
            img.convert_alpha()
            img.set_colorkey(ALPHA)
            self.images.append(img)
            self.image = self.images[0]
            self.rect  = self.image.get_rect()
            self.rect.topleft = (0,0)
    
    def update_sprite(self, x_list, y_list):
        self.rect.x = x_list
        self.rect.y = y_list
        