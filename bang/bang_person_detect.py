# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 09:02:48 2016


BIG THANKS FOR TUTORIAL
http://www.pyimagesearch.com/2015/11/09/pedestrian-detection-opencv/


@author: pgilmore
"""


# import the necessary packages
from __future__ import print_function
from imutils.object_detection import non_max_suppression
from imutils import paths
import numpy as np
import argparse
import imutils
import cv2
 
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--images", required=True, help="path to images directory")
args = vars(ap.parse_args())
 
# initialize the HOG descriptor/person detector
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())