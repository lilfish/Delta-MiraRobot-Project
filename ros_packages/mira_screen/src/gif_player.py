import pyglet 
from pyglet.window import key
from threading import Thread
from gif_protocol import SharedData
from exit_protocol import EnumExitProtocol

import rospy
from std_msgs.msg import Int8

class ExitSignalSub():
    def __init__(self):
        self.pub = rospy.Subscriber('/mira_screen_exit', Int8, self.callback)
        self.exit_signal = False
    def callback(self, data):
        if data.data == int(EnumExitProtocol.SCREEN):
            self.exit_signal = True

class ExitSignalPub():
    def __init__(self):
        self.pub = rospy.Publisher('/mira_screen_exit', Int8, queue_size=10, latch=True)
    def send_signal(self):
        msg = Int8()
        msg.data = int(EnumExitProtocol.SCREEN)
        self.pub.publish(msg)

class GifPlayer(pyglet.window.Window):

    def __init__(self):
        super(GifPlayer, self).__init__(width=405, height=720)
        self.queue_gif = []
        self.queue_index = -1
        self.exit_sub = ExitSignalSub()
        self.change_gif(SharedData.global_dict['final_gif'])
        
    def on_draw(self):
        self.clear()
        self.sprite.draw()
    
    def on_close(self):
        self.exit_sub.exit_signal = True

    def on_key_press(self, symbol, modifiers):
        if symbol == key.ESCAPE:
            self.exit_sub.exit_signal = True

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
        while not self.exit_sub.exit_signal:
            if (not SharedData.global_dict['emotion_handled']):
                if (not SharedData.global_dict['transitioning']):
                    self.change_gif(SharedData.global_dict['final_gif'])
                    SharedData.emotion_handled()
                else:
                    first = True  
                    time_elapsed = 0
                    self.queue_gif = []
                    self.queue_index = 0
                    for i in range(0, len(SharedData.buffer_gifs)):
                        if (first):
                            # print('changing to ', SharedData.buffer_gifs[i])
                            self.change_gif(gif_file=SharedData.buffer_gifs[i])
                            first = False
                        else:
                            time_elapsed += SharedData.buffer_delays[i]
                            # print('scheduling: ', SharedData.buffer_gifs[i], ' after ', SharedData.buffer_delays[i])
                            self.schedule_change_to_gif(gif_file=SharedData.buffer_gifs[i], delay=SharedData.buffer_delays[i])
                    SharedData.transition_handled()
            self.manual_dispatch()
        return True

class GifPlayerThread(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.start()
        
    def run(self):
        gp = GifPlayer()
        gp.run()
        if gp.exit_sub.exit_signal:
            gp.set_visible(visible=False)
            exit_pub = ExitSignalPub()
            exit_pub.send_signal()