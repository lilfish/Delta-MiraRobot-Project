import time
from tkinter import *
from AnimatedGif import *
import easingScripts

given_x = 820
given_y = 399
tk = Tk()
w = 1920
h = 1080
canvas = Canvas(tk, width=w, height=h)
canvas.pack()

my_image = AnimatedGif(tk, 'giphy.gif', 0.01)
my_image.pack()
my_image.place(x=1920/2, y=1080/2, anchor=CENTER)
my_image.start()
tk.update()

# mainloop()
# my_image = PhotoImage(file='tenor.gif', format="gif -index 0")
# my_img = canvas.create_image(0,0, anchor=NW, image=my_image)
while True:
    if (float(my_image.place_info()['x']) != given_x) or (float(my_image.place_info()['x']) != given_x):
        
        target_x = float(given_x)
        target_y = float(given_y)

        position_x = float(my_image.place_info()['x'])
        position_y = float(my_image.place_info()['y'])

        ease = 0.005
        if (target_x - position_x > 0):
            distance_x = target_x + position_x
            velocity_x = distance_x * ease
            new_pos_x = position_x - velocity_x
        else:   
            distance_x = target_x - position_x
            velocity_x = distance_x * ease
            new_pos_x = position_x + velocity_x

        if (target_y - position_y > 0):
            distance_y = target_y + position_y
            velocity_y = distance_y * ease
            new_pos_y = position_y - velocity_y
        else:
            distance_y = target_y - position_y
            velocity_y = distance_y * ease
            new_pos_y = position_y + velocity_y
        
        print(new_pos_y, new_pos_x)
        print( float(my_image.place_info()['x']), float(my_image.place_info()['y']))
        my_image.place(x=new_pos_x, y=new_pos_y) 
        tk.update()
        time.sleep(0.0001)

    else:
        tk.update_idletasks()
        tk.update()
