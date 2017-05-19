# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 15:00:17 2016

@author: pgilmore
"""

import pyttsx
import pandas as pd
import time



'''SYS CONFIG'''
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
#related to chained operators and setting to copies of slices
#this is a workaround to errors thrown at runtime
pd.set_option('mode.chained_assignment',None)


'''LOAD IN CONTENT FILES THAT RESIDE IN BANG'S DIRECTORY'''
'''A copy-paste .csv of Profiles Complete Tab save as the static
file "mondaysprofiles.csv"

any additional commments written into a static text file
"mondayscomments.txt"
'''


profiles = pd.read_csv("mondaysprofiles.csv", encoding='utf-8')    
   
f = open("mondayscomments.txt","r")
mondayscomments = f.read()
f.close()

'''USE LOGIC TO SETUP SPEECH UNITS'''

plg_profiles = profiles[profiles['Assigned To']=='Phillip Gilmore']
plg_profiles.reset_index(inplace = True)



'''SETUP THE SPEECH FUNCTION'''
def bang_speak(text_string):
    engine = pyttsx.init()
    engine.setProperty('volume', 1.00)
    engine.setProperty('rate', 150)
    engine.say(text_string)
    engine.runAndWait()
    return


def loop_profiles(specific_profiles):
    df = specific_profiles
    line = "Okay, what do we have "
    
    for i in range(0,len(df)):
        line = line + ' ' + df.ix[i,'Task (Profile Name)'].split()[0] + ' , ' #Gables
        line = line + ' ' + df.ix[i,'Task (Profile Name)'].split()[1] + ' . ' #7R

        n =  df.ix[i,'n']
        if n < 40:
            line = line + ' smallish sample size. ' #
        elif n >= 40 and n < 200:
            line = line + ' decent sample size on this one. '
        else:
            line = line + ' wow, great sample size for this profile. '
        
        
        line = line + ' . This profile was built on the metric type. ' + df.ix[i,'Metric Type']
        
        r =  df.ix[i,'r']
        if r < .20:
            line = line + ' pretty weak profile, but it built; hopefully we can recalibrate this soon. ' #
        elif r >= .20 and r < .40:
            line = line + ' good profile here. '
        else:
            line = line + ' very strong effect size. '
            if n < 60:
                line = line + ' but small samples tend to have inflated effect sizes. '
            else:
                line = line + ' very strong profile. '       

        if i < (len(df)-1):
            line = line + ' okay, whats next. '
        else:
            line = line + ' ummmmmm, i think thats it. '
    
    return line



if len(plg_profiles) == 0:
    profile_summary = "No profiles for me this week"
    profile_details = ""
else:
    profile_summary = "I had {} profiles this week".format(len(plg_profiles))
    profile_details = loop_profiles(plg_profiles)

 
goodbye = "Thanks, that's all for me"


bang_speak(profile_summary)
bang_speak(profile_details)
bang_speak(mondayscomments)
bang_speak(goodbye)

