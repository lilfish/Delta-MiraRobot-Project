import pyglet
from pyglet.window import key
import time

animation_eyes = pyglet.image.load_animation("tenor.gif")
animation_angry = pyglet.image.load_animation("tenor.gif")
animSprite = pyglet.sprite.Sprite(animation_eyes)
animSpriteAngry = pyglet.sprite.Sprite(animation_angry)

w = animSprite.width
h = animSprite.height 

window = pyglet.window.Window(width=w, height=h)
keys = key.KeyStateHandler()
window.push_handlers(keys)

r,g,b,alpha = 0.5,0.5,0.8,0.5

pyglet.gl.glClearColor(r,g,b,alpha)

animSprite.draw()
pyglet.app.run()

while True:
    def test():
        animSprite = pyglet.sprite.Sprite(animation_angry)
        animSprite.draw()
        
    def test2():
        animSprite = pyglet.sprite.Sprite(animation_eyes)
        animSprite.draw()


    @window.event
    
    def on_draw():
        if keys[key.SPACE]:
            test()
        
        if keys[key.A]:
            test2()
        
    
    


    