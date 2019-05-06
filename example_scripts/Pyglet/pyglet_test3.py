import pyglet
import time

animation = pyglet.image.load_animation('tenor.gif')
animation2 = pyglet.image.load_animation('giphy.gif')

sprite = pyglet.sprite.Sprite(img=animation, x=1920//2, y=1080//2)
sprite2 = pyglet.sprite.Sprite(img=animation2, x=1920//2, y=1080//2)

sprites = []
sprites.append(PhotoImage(file = "tenor.gif"))
sprites.append(PhotoImage(file = "giphy.gif"))

sprites = 0

bin = pyglet.image.atlas.TextureBin()
animation.add_to_texture_bin(bin)


window = pyglet.window.Window(width=1920,height=1080)

def update(value):
    print("I'm in a loop...")
    if not (sprite.x > 1200):
        sprite.x = sprite.x + 5
    else:
        window.clear()
        sprite2.draw()

@window.event
def on_draw():
    window.clear()
    sprite.draw()
    
pyglet.clock.schedule_interval(update, 1/120.0)

pyglet.app.run()


