import pygame
from random import randint
import time
import easingScripts
import sys
from sprite import Player

worldx = 1920
worldy = 1080

fps = 100        # frame rate
clock = pygame.time.Clock()
pygame.init()
main = True

BLACK = (23, 23, 23)
ALPHA = (0, 255, 0)

world = pygame.display.set_mode([worldx, worldy],pygame.FULLSCREEN)

player = Player()   # spawn player
player.rect.x = 0
player.rect.y = 0
player_list = pygame.sprite.Group()
player_list.add(player)

new_x_pos = []
new_y_pos = []

'''
Main loop
'''
animation_counter = 1
while main == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            main = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z or event.key == ord('z'):
                if new_y_pos == [] and new_x_pos == []:
                    # print(player.movey)
                    print()
                    # print(player.get_size()[1])
                    given_x = randint(0, worldx-player.rect.width)
                    given_y = randint(0, worldy-player.rect.height)
                    if (float(player.rect.x) != float(given_x)) or (float(player.rect.y) != float(given_y)):
                        target_x = float(given_x)
                        target_y = float(given_y)

                        position_x = float(player.rect.x)
                        position_y = float(player.rect.y)
                        for q in range(0, fps):
                            p = q + 1
                            new_x_pos.append(easingScripts.easeInOutQuint(
                                1, position_x, target_x-position_x, p))
                            new_y_pos.append(easingScripts.easeInOutQuint(
                                1, position_y, target_y-position_y, p))

                        new_x_pos.reverse()
                        new_y_pos.reverse()

            if event.key == ord('q'):
                pygame.quit()
                sys.exit()
                main = False

    if (new_x_pos != []) and (new_y_pos != []):
        player.update_sprite(new_x_pos[animation_counter], new_y_pos[animation_counter])
        # pygame.display.update()
        # pygame.time.delay(10)

        animation_counter += 1
        if animation_counter == fps:
            animation_counter = 0
            new_x_pos = []
            new_y_pos = []

    world.fill(BLACK)

    
    player_list.draw(world)  # refresh player position
    pygame.display.flip()
    clock.tick(fps)
