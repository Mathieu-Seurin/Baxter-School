#!/usr/bin/python
#coding: utf-8
import time

import numpy as np
import torch

import rospy

from baxter_interface import Limb
from baxter_interface import Gripper
from baxter_interface import CameraController
from baxter_interface import RobotEnable

from sensor_msgs.msg import Image
from std_msgs.msg import Empty

from cv_bridge import CvBridge
#absolute movement or relative => relative, learning how to move without a predifined path

class LearnEnv(object):
    def __init__(self):
        rospy.Subscriber('/environment/reset', Empty, self.reset_callback, queue_size = 1)

        self.rightArm = Limb('right')

        self.bridge = CvBridge()
        self.imageSub = rospy.Subscriber("cameras/head_camera_2/image",Image,self.imageFromCamera)
        self.currentImage = None
        
        self.wave_1 = {'right_s0': 0, 'right_s1': 0}
        self.wave_2 = {'right_s0': -0.5, 'right_s1': -0.5}

    def reset_callback(self):
        self.init()

    def imageFromCamera(self,data):
        self.currentImage = self.bridge.imgmsg_to_cv2(data, "rgb8")

    def run(self):

        rate = rospy.Rate(20)
        while not rospy.is_shutdown():
            self.move()
            rate.sleep()

    def move(self):

        print "move" 
        pos = self.wave_1
        pos['right_s0'] = self.wave_1['right_s0']+0.05 if self.i%200<100 else self.wave_1['right_s0']-0.05
        self.rightArm.move_to_joint_positions(pos,timeout=0.1)
        
    def init(self):
        zero_pos = {'right_s0': 0, 'right_s1': 0, 'right_e0': 0, 'right_e1': 0, 'right_w0': 0, 'right_w1': 0, 'right_w2': 0}
        self.leftArm.set_joint_positions(zero_pos)

        
def main():
    rospy.init_node('Learning')
    baxter = RobotEnable()

    rightArm = Limb('right')
    zero_pos = {'right_s0': 0, 'right_s1': 0, 'right_e0': 0, 'right_e1': 0, 'right_w0': 0, 'right_w1': 0, 'right_w2': 0}
    rightArm.move_to_joint_positions(zero_pos)

    #Un seul bras pour simplifier dans un premier temps.
    rightGripper = Gripper('right')

    time.sleep(5)
    
    # leftArm = Limb('left')
    # left_gripper = Gripper('left')
    

    env = LearnEnv()
    env.run()
    print("Running. Ctrl-c to quit")

if __name__ =='__main__':
    main()