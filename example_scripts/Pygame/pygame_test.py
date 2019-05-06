import pygame
from random import randint
import time
import easingScripts
import sys
import os
from sprite import Player

# Initialize the game engine
pygame.init()
# Set the height and width of the screen
width = 1920
height = 1080

# Set screen
screen = pygame.display.set_mode((width,height), pygame.FULLSCREEN)
pygame.display.set_caption("Mira")
black = (0, 0, 0)
background = pygame.Surface(screen.get_size())
background.fill(black)

# Set sprite
sprite = pygame.image.load("giphy.gif")
sprite_rect = sprite.get_rect()
sprite_rect.centerx = (width//2)
sprite_rect.centery = (height//2)
screen.blit(sprite, sprite_rect)

# Set clock
clock = pygame.time.Clock()

given_x = 300
given_y = 200
# Loop until the user clicks the close button.
done = False
while not done:

    for event in pygame.event.get():   # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True   # Flag that we are done so we exit this loop

    # Go ahead and update the screen with what we've drawn.
        clock.tick(30)
    pygame.event.pump()
    # a key has been pressed
    keyinput = pygame.key.get_pressed()
    # press escape key to quit game
    if keyinput[pygame.K_ESCAPE]:
        raise SystemExit
    # optional exit on window corner x click
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
    # check arrow keys
    # move sprite in direction of arrow by 2 pixels
    if keyinput[pygame.K_SPACE]:
        print(sprite_rect.centerx)
        print(sprite_rect.centery)
        given_x = randint(300, 1920-300)
        given_y = randint(200, 1080-200)
        time.sleep(1)
    #########################
    # ANIMATEIONS
    #########################
    while (int(sprite_rect.centerx) != int(given_x)) or (int(sprite_rect.centery) != int(given_y)):
        target_x = float(given_x)   
        target_y = float(given_y)

        position_x = float(sprite_rect.centerx)
        position_y = float(sprite_rect.centery)

        new_x_pos = [99]
        new_y_pos = [99]

        for q in range(0,42):
            p = q + 1
            new_x_pos.append(easingScripts.easeInOutQuint(1, position_x, target_x-position_x, p))
            new_y_pos.append(easingScripts.easeInOutQuint(1, position_y, target_y-position_y, p))
        
        new_x_pos.reverse()
        new_y_pos.reverse()

        for v in range(2,42):
            sprite_rect.centerx = new_x_pos[v]
            sprite_rect.centery = new_y_pos[v]
            clock.tick(120)
            pygame.display.flip()

    #########################
    # ANIMATION END
    #########################
    screen.blit(background, (0,0))
    screen.blit(sprite, sprite_rect)
    # update display
    pygame.display.flip()

# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()
