import pygame
import sys
from screencontroller import ScreenController

pygame.init()
sc = ScreenController(screen_width=1920, screen_height=1080, mode=pygame.RESIZABLE)
sc.add_image('giphy.gif', name="Test")
# sc.add_image('puppy.jpg', name="Puppy nr.1", pos_x=0, pos_y=0)

while True:
    sc.update()
    # Handle quit events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == ord('q'):
                pygame.quit()
                sys.exit()
            if event.key == ord('w'):
                print (sc.image_list)
            if event.key == ord('w'):
                target_x, target_y = sc.get_proportional_target([sc.SCREEN_WIDTH/2, sc.SCREEN_WIDTH/2 + 500, sc.SCREEN_HEIGHT/2, sc.SCREEN_HEIGHT/2 + 500])
                print("Computed target: ", target_x, target_y)
                sc.move_image_to("Test", target_x, target_y)