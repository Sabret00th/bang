# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 15:00:17 2016

@author: pgilmore
"""

import pyttsx
import pandas as pd



'''SYS CONFIG'''
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
#related to chained operators and setting to copies of slices
#this is a workaround to errors thrown at runtime
pd.set_option('mode.chained_assignment',None)

profiles = pd.read_csv("mondaysprofiles.csv", encoding='utf-8')    
   
f = open("mondayscomments.txt","r")
mondayscomments = f.read()
f.close()

print mondayscomments

engine = pyttsx.init()
volume = engine.getProperty('volume')
engine.setProperty('volume', 1.00)
engine.say('Stack stack stack it up.')
engine.runAndWait()

