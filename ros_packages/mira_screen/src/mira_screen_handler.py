#!/usr/bin/env python

import rospy
from std_msgs.msg import Int8
from screen_manager import ScreenManager
from gif_protocol import SharedData
from exit_protocol import EnumExitProtocol

class Listener():
    def __init__(self):
        self.sm = ScreenManager()
        rospy.init_node('mira_screen_listener', anonymous=True)
        rospy.Subscriber("mira_screen_emotion", Int8, self.callback)
        rospy.Subscriber('/mira_screen_exit', Int8, self.exit_callback)
        rospy.spin()
    
    def exit_callback(self, data):
        if data.data == int(EnumExitProtocol.SCREEN):
            rospy.loginfo('Thread has exited...')
            rospy.loginfo('Shutting down ROS...')
            rospy.signal_shutdown('Exit signal received')

    def callback(self, data):
        rospy.loginfo(rospy.get_caller_id() + "Changing emotion to: %s", data.data)
        self.sm.change_to_emotion(data.data)

if __name__ == '__main__':
    listener = Listener()
    
