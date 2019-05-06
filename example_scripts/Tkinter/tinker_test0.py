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

while True:
    print("k")
    for p in range(0,60):
        new_x = int(my_image.place_info()['x']) + 5
        new_y = my_image.place_info()['y'] 
        my_image.place(x=new_x, y=new_y) 
        # canvas.move(my_image, 5, 0)
        tk.update()
        time.sleep(0.01)

    for p in range(0,60):
        new_x = int(my_image.place_info()['x'])
        new_y = int(my_image.place_info()['y']) + 5
        my_image.place(x=new_x, y=new_y) 
        # canvas.move(my_image, 5, 0)
        tk.update()
        time.sleep(0.01)

        
    for p in range(0,60):
        new_x = int(my_image.place_info()['x']) - 5
        new_y = int(my_image.place_info()['y']) 
        my_image.place(x=new_x, y=new_y) 
        # canvas.move(my_image, 5, 0)
        tk.update()
        time.sleep(0.01)

    for p in range(0,60):
        new_x = int(my_image.place_info()['x'])
        new_y = int(my_image.place_info()['y']) - 5
        my_image.place(x=new_x, y=new_y) 
        # canvas.move(my_image, 5, 0)
        tk.update()
        time.sleep(0.01)

    my_image.destroy()
    my_image = AnimatedGif(tk, 'tenor.gif', 0.01)
    my_image.place(x=1920/2, y=1080/2, anchor=CENTER)
    my_image.start()
