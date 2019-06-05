#!/usr/bin/env python

import rospy
from std_msgs.msg import Int8
from sound import SoundPlayer
from exit_protocol import EnumExitProtocol

class Listener():
    def __init__(self):
        self.sp = SoundPlayer(sound_dir='/home/thanh/catkinws/src/mira_sound/data')
        rospy.init_node('mira_sound_listener', anonymous=True)
        rospy.Subscriber("mira_sound_player", Int8, self.callback)
        rospy.Subscriber('/mira_screen_exit', Int8, self.exit_callback)
        rospy.loginfo("Sound handler ready!")
        rospy.spin()
    
    def exit_callback(self, data):
        if (data.data == int(EnumExitProtocol.SOUND)):
            rospy.loginfo('Exit signal [%d] received!' % data.data)
            rospy.signal_shutdown('Exit signal received')

    def callback(self, data):
        if (data.data != -1):
            rospy.loginfo("Received emotion id: %s", (data.data))
            self.sp.change_to_emotion(data.data)
        else:
            rospy.loginfo("Stop playing sound")
            # make it stop

if __name__ == '__main__':
    listener = Listener()
    
