import pyglet
from pyglet.window import Window
from pyglet.window import key
from gif_player_with_transition import GifPlayerWithTransition

gh = GifHolder(gif_file='fast_wink_rotated.gif')
win = pyglet.window.Window(fullscreen=True)

@win.event
def on_key_press(key, modifiers):
    global gh
    print(key)
    if key == 97:
        gh.change_gif('fast_wink_rotated.gif')
    elif key == 100:
        gh.change_gif('to_happy_rotated.gif')



try:
    pyglet.app.run()
except KeyboardInterrupt:
    print("exiting...")
    pyglet.app.exit()
