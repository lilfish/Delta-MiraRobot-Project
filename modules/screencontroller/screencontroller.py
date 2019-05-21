import pygame
import time

from sprite import Image 
import easingScripts

BLACK = (23, 23, 23)

class ScreenController:
    # Const
    SCREEN_WIDTH = 1920
    SCREEN_HEIGHT = 1080
    FRAME_RATE = 100
    CLOCK = pygame.time.Clock()
    
    # Properties
    screen = None
    image_list = pygame.sprite.Group()
    image_name = []
    
    def __init__(self, screen_width=1920, screen_height=1080, frame_rate=100, mode=pygame.FULLSCREEN):
        self.SCREEN_HEIGHT = screen_height
        self.SCREEN_WIDTH = screen_width
        self.FRAME_RATE = frame_rate
        self.screen = pygame.display.set_mode([self.SCREEN_WIDTH, self.SCREEN_HEIGHT], mode)
        print("Screen created!")
        print("Screen resolution: ", self.SCREEN_WIDTH, " x ", self.SCREEN_HEIGHT)
        print("Frame rate: ", self.FRAME_RATE)
    
    def add_image(self, path, name, pos_x=0, pos_y=0):
        newImage = Image()
        newImage.load_image(path)
        newImage.rect.x = pos_x
        newImage.rect.y = pos_y
        self.image_list.add(newImage)
        self.image_name.append(name)
        print("Image '%s' added with name '%s'" % (path, name))
    
    def get_proportional_target(self, coordinates, reduction_rate=1):
        '''
            coordinates[0,1,2,3] = ymin, ymax, xmin, xmax
        '''
        midpoint_y = coordinates[0]/reduction_rate + coordinates[1]/reduction_rate
        midpoint_y /= 2
        midpoint_x = coordinates[2]/reduction_rate + coordinates[3]/reduction_rate
        midpoint_x /= 2 
        
        ratio_y = midpoint_y / self.SCREEN_HEIGHT
        ratio_x = midpoint_x / self.SCREEN_WIDTH
        return ratio_x * self.SCREEN_WIDTH, ratio_y * self.SCREEN_HEIGHT
    
    def get_image_from_list (self, name):
        if name in self.image_name:
            index = self.image_name.index(name)
            i = 0
            for image in self.image_list:
                if (i < index):
                    continue
                return image
        return None

    def move_image_to (self, name, target_x, target_y):
        image = self.get_image_from_list (name)
        if (image is not None):
            image.build_trajectory_to(target_x, target_y, self.FRAME_RATE)
            print ("Finished building trajectory for image '%s'" % name)

    def update(self):
        self.screen.fill(BLACK)
        self.image_list.update(self.FRAME_RATE)
        self.image_list.draw(self.screen)
        self.CLOCK.tick(self.FRAME_RATE)
        pygame.display.flip()
    
    