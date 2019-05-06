import time
from tkinter import *
from AnimatedGif import *
import easingScripts
from random import randint
import os

given_x = 300
given_y = 200
tk = Tk()
width_x = 1920
height_y = 1080
canvas = Canvas(tk, width=width_x, height=height_y)
canvas.pack()

video_speed = 0.01

fun_counter = 0

max_x = 300
max_y = 200


my_image = AnimatedGif(tk, 'giphy.gif', video_speed)
my_image.pack(padx=200, pady=200)
my_image.place(x=1920/2, y=1080/2, anchor=CENTER)
my_image.start()
tk.update()

# mainloop()
# my_image = PhotoImage(file='tenor.gif', format="gif -index 0")
# my_img = canvas.create_image(0,0, anchor=NW, image=my_image)
while True:
    if (int(my_image.place_info()['x']) != int(given_x)) or (int(my_image.place_info()['x']) != int(given_x)):
        # if (given_x > (width_x-given_x)): 
        #     target_x = (width_x-given_x)
        # elif (given_x > max_x):
        #     target_x = max_x
        # else:
        target_x = float(given_x)   

        # if(given_y > (height_y-given_y)): 
        #     target_y = (height_y-given_y)
        # elif (given_y > max_y):
        #     target_y = max_y
        # else:
        target_y = float(given_y)
            

        position_x = float(my_image.place_info()['x'])
        position_y = float(my_image.place_info()['y'])

        new_x_pos = [99]
        new_y_pos = [99]
        print("position")
        print(position_x, position_y)
        print("target")
        print(target_x, target_y)
        # print(target_y)

        for q in range(0,42):
            p = q + 1
            new_x_pos.append(easingScripts.easeInOutQuint(1, position_x, target_x-position_x, p))
            new_y_pos.append(easingScripts.easeInOutQuint(1, position_y, target_y-position_y, p))
        
        new_x_pos.reverse()
        new_y_pos.reverse()

        for v in range(2,42):
            my_image.place(x=new_x_pos[v], y=new_y_pos[v])
            tk.update()
            # if (v < 400):
            #     time.sleep(0.0001)
            # elif (v > 950):
            #     time.sleep(video_speed)
            # else:

            time.sleep(video_speed)
        my_image.place(x=target_x, y=target_y)

    

    else:
        tk.update_idletasks()
        tk.update()
        time.sleep(video_speed)
        fun_counter = fun_counter + 1
        if (fun_counter == 25):
            given_x = randint(300, 1920-300)
            given_y = randint(200, 1080-200)
            fun_counter = 0
    
    try:                 
        key = win.getkey()         
        win.clear()                
        win.addstr("Detected key:")
        win.addstr(str(key)) 
    except Exception as e:
        # No input   
        pass         
