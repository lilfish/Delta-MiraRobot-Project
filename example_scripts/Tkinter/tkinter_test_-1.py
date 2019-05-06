"""Try displaying a photo of yourself on the canvas using tkinter.
Make sure it’s a GIF image! Can you make it move across the
screen?"""

import time
from tkinter import *
tk = Tk()
w = 500
h = 500
canvas = Canvas(tk, width=w, height=h)
canvas.pack()

my_image = PhotoImage(file='tenor.gif', format="gif -index 0")
my_img = canvas.create_image(0,0, anchor=NW, image=my_image)

while True:
    for x in range(0,60):
        canvas.move(my_img, 5, 0)
        tk.update()
        time.sleep(0.05)

    for x in range(0,60):
        canvas.move(my_img, 0, 5)
        tk.update()
        time.sleep(0.05)
        
    for x in range(0,60):
        canvas.move(my_img, -5, 0)
        tk.update()
        time.sleep(0.05)

    for x in range(0,60):
        canvas.move(my_img, 0, -5)
        tk.update()
        time.sleep(0.05)