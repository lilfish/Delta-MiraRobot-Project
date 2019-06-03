#!/usr/bin/env python

import rospy
from std_msgs.msg import Int8
from screen_manager import ScreenManager

class Listener():
    def __init__(self):
        self.sm = ScreenManager()
        rospy.init_node('mira_screen_listener', anonymous=True)
        rospy.Subscriber("mira_screen_emotion", Int8, self.callback)
        rospy.spin()

    def callback(self, data):
        rospy.loginfo(rospy.get_caller_id() + "Changing emotion to: %s", data.data)
        self.sm.change_to_emotion(data.data)

if __name__ == '__main__':
    listener = Listener()
