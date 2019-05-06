import pygame
from random import randint
import time
import easingScripts
import sys
from sprite import Player
import face_recognition
import cv2
import re

worldx = 1920
worldy = 1080

fps = 100        # frame rate
clock = pygame.time.Clock()
pygame.init()
main = True

video_capture = cv2.VideoCapture(0)


cap_width = video_capture.get(3)
cap_height = video_capture.get(4)
print(cap_width, cap_height)
video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, cap_width)
video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, cap_height)

BLACK = (23, 23, 23)
ALPHA = (0, 255, 0)

world = pygame.display.set_mode([worldx, worldy], pygame.FULLSCREEN)

player = Player()   # spawn player
player.rect.x = 0
player.rect.y = 0
player_list = pygame.sprite.Group()
player_list.add(player)

new_x_pos = []
new_y_pos = []

face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

'''
Main loop
'''
animation_counter = 1
while main == True:
    ret, frame = video_capture.read()
    cv2.imshow('frame', frame)
    # Resize frame of video to 1/4 size for faster face recognition processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_small_frame = small_frame[:, :, ::-1]
    if process_this_frame:
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        for i in range(len(face_locations)):
            something = str(face_locations[i])
            print(something)
            # get facelocations in a procentage.
            something = re.sub('[()]', "", something)
            something = something.replace(" ", "")
            list_something = something.split(",")
            
            avarage_y = (int(list_something[0])*4) + (int(list_something[2])*4) / 2
            avarage_x = (int(list_something[1])*4) + (int(list_something[3])*4) / 2
            
            avarage_procent_y = 100/cap_width*avarage_y
            avarage_procent_x = 100/cap_height*avarage_x
            print(avarage_procent_y, avarage_procent_x)
            new_target_x = avarage_x
            new_target_y = avarage_y

            # if (float(player.rect.x) != float(new_target_x)) or (float(player.rect.y) != float(new_target_y)):
            #             target_x = float(new_target_x)
            #             target_y = float(new_target_y)

            #             position_x = float(player.rect.x)
            #             position_y = float(player.rect.y)
            #             for q in range(0, fps):
            #                 p = q + 1
            #                 new_x_pos.append(easingScripts.easeInOutQuint(
            #                     1, position_x, target_x-position_x, p))
            #                 new_y_pos.append(easingScripts.easeInOutQuint(
            #                     1, position_y, target_y-position_y, p))

            #             new_x_pos.reverse()
            #             new_y_pos.reverse()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            main = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z or event.key == ord('z'):
                if new_y_pos == [] and new_x_pos == []:
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
        player.update_sprite(
            new_x_pos[animation_counter], new_y_pos[animation_counter])
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
