# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 11:41:36 2016

@author: pgilmore
"""

from tkFileDialog import askdirectory
import os
from cv2 import *


filename = raw_input("Type in the file name you want the image saved as, then press Enter.")

print("Now, select the directory that will contain the new image.\n\
Before clicking 'Ok', be sure to hold up your item to the webcam.\n\
Once you select the directory and click 'Ok', the picture will be taken.")

#user identifies direcotyr path that you want the images saved into
dir_path = askdirectory()

# initialize the camera
cam = VideoCapture(1)   # 0 -> index of camera
s, img = cam.read()


if s:    # frame captured without any errors
    #namedWindow("cam-test",CV_WINDOW_AUTOSIZE)
    imshow("Preview Image. Press any key to continue",img)
    waitKey(0)
    destroyWindow("Preview Image. Press any key to continue")
    imwrite(dir_path+"/"+filename+".jpg",img) #save image
    
cam.release()