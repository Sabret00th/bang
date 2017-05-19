# -*- coding: utf-8 -*-
"""
Created on Mon Feb 01 08:56:08 2016

@author: pgilmore
"""

'''BAM module
Monday meeting, weekly tracker reporting locked down profiles

thanks to phihag for snippet on stackoverflow
http://stackoverflow.com/questions/6558535/python-find-the-date-for-the-first-monday-after-a-given-a-date
'''

import datetime

def next_weekday(d, weekday):
    days_ahead = weekday - d.weekday()
    if days_ahead <= 0: # Target day already happened this week
        days_ahead += 7
    return d + datetime.timedelta(days_ahead)

d = datetime.date(2011, 7, 2)
next_monday = next_weekday(d, 0) # 0 = Monday, 1=Tuesday, 2=Wednesday...
print(next_monday)

#filepath to 2016 directory of weekly tracker,
#typically tracker is reported on Monday 9a CST, and otherwise if not said Monday 
#before 9a, then a new tracker is saved with filename indicating date of
#next monday
#Z:\I-O\Weekly Reports\2016
