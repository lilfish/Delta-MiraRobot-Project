import pyglet 
from pyglet.window import key
from threading import Thread
from gif_protocol import SharedData

class GifPlayer(pyglet.window.Window):

    def __init__(self):
        super(GifPlayer, self).__init__(width=405, height=720)
        self.queue_gif = []
        self.queue_index = -1
        self.alive = True
        self.change_gif(SharedData.global_dict['final_gif'])
        
    def on_draw(self):
        self.clear()
        self.sprite.draw()
    
    def on_close(self):
        self.alive = False

    def on_key_press(self, symbol, modifiers):
        if symbol == key.Q:
            self.alive = False

    def change_gif(self, gif_file=''):
        # print("setting gif to '%s'" % gif_file)
        self.gif_file = gif_file 
        self.animation = pyglet.resource.animation(self.gif_file)
        self.sprite = pyglet.sprite.Sprite(self.animation)
    
    def pyglet_change_cb(self, dt):
        self.change_gif(gif_file=self.queue_gif[self.queue_index])
        self.queue_index = self.queue_index + 1
    
    def schedule_change_to_gif(self, gif_file='', delay=1.0):
        self.queue_gif.append(gif_file)
        pyglet.clock.schedule_once(self.pyglet_change_cb, delay)
        # print('queue: ', self.queue_gif)
    
    def manual_dispatch(self):
        pyglet.clock.tick()
        self.switch_to()
        self.dispatch_events()
        self.dispatch_event('on_draw')
        self.flip()

    def run(self):
        while self.alive:
            if (not SharedData.global_dict['emotion_handled']):
                if (not SharedData.global_dict['transitioning']):
                    self.change_gif(SharedData.global_dict['final_gif'])
                    SharedData.emotion_handled()
                else:
                    first = True  
                    time_elapsed = 0
                    self.queue_gif = []
                    self.queue_index = 0
                    for key, value in SharedData.buffer.items():
                        if (first):
                            # print('changing to ', key)
                            self.change_gif(gif_file=key)
                            first = False
                        else:
                            time_elapsed += value
                            # print('scheduling: ', key, ' after ', time_elapsed)
                            self.schedule_change_to_gif(gif_file=key, delay=time_elapsed)
                    SharedData.transition_handled()
            self.manual_dispatch()
        return True

class GifPlayerThread(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.alive = True
        self.start()
        
    def run(self):
        gp = GifPlayer()
        gp.run()
        if not gp.alive:
            gp.set_visible(visible=False)
            print('thread is dead. exiting...')


    