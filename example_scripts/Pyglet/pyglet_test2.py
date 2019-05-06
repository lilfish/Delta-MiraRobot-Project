import pyglet

window = pyglet.window.Window(width=1920,height=1080)
image = pyglet.resource.image('eyes.png')
image.width = 100
image.height = 100

@window.event
def on_draw():
    window.clear()
    image.anchor_x = 1920/2
    image.anchor_y = 1080/2
    image.blit(x, y)

pyglet.app.run()