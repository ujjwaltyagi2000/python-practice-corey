import my_module as mm # importing the module as mm
# my_module can be imported directly if it's in the same working directory
# shortening my_module to mm is convenient


courses = ['History', 'Math', 'Physics', 'CompSci']

index = mm.find_index(courses, 'CompSci')
print(index)

# to only include find_index, write: from my_module import find_index as fi
# the code will now change to:
# index = fi(courses, 'CompSci')

# to import everything from my_module, write: from my_module import *
# the code will now change to:
# from my_module import *
# but this is not recommended as it becomes a problem during debugging.
# it becomes to determine wether the error is in the working file or the imported module
# instead, use:
# from my_module import find_index, test

# how does python know where to find the module?
import sys
print("These are the directories where Python looks for modules:")
print(sys.path)
# within this path, the first directory is the directory where the script is located
# the following directories are environment variables
# to add a directory in sys.path:
# sys.path.append("D:\Projects\Python")



# some more libraries
import random
# by convention all imports should be above the code

random_course = random.choice(courses)
print("\nRandomly Chosen Course is: " + random_course)

import math

rads = math.radians(90)
print(rads)
print(f"sin(90) = {math.sin(rads)}")

import datetime
import calendar

today = datetime.date.today()
print(today)

day = calendar.day_name[today.weekday()]
print(day)

import os
print(os.getcwd()) # get current working directory

# finding path of these libraries:
print("\nFinding path of 'os' library")
print(os.__file__) # absolute path of the library
# __file__ is a dunder method in Python

import antigravity
# this is a python joke that leads to a tab opening on the web of a python comic
