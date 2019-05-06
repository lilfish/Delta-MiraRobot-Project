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

        easingScripts.easeOutQuart(0, position_x, )



        if (int(my_image.place_info()['x']) < given_x):
            new_x = int(my_image.place_info()['x']) + 1
            new_y = int(my_image.place_info()['y']) 
            my_image.place(x=new_x, y=new_y) 
            # canvas.move(my_image, 5, 0)
            tk.update()
            
        elif (int(my_image.place_info()['x']) > given_x):
            new_x = int(my_image.place_info()['x']) - 1
            new_y = int(my_image.place_info()['y'])
            my_image.place(x=new_x, y=new_y) 
            # canvas.move(my_image, 5, 0)
            tk.update()
            

        if (int(my_image.place_info()['y']) < given_y):
            new_x = int(my_image.place_info()['x'])
            new_y = int(my_image.place_info()['y']) + 1
            my_image.place(x=new_x, y=new_y) 
            # canvas.move(my_image, 5, 0)
            tk.update()
            
        elif (int(my_image.place_info()['y']) > given_y):
            new_x = int(my_image.place_info()['x'])
            new_y = int(my_image.place_info()['y']) - 1
            my_image.place(x=new_x, y=new_y) 
            # canvas.move(my_image, 5, 0)
            tk.update()
            
        print(int(my_image.place_info()['x']))
        print(int(my_image.place_info()['y']))
    else:
        tk.update_idletasks()
        tk.update()
