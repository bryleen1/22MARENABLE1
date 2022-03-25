#1 print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are")

#2  import sys
#   print(sys.version)
""" #3
import datetime
now = datetime.datetime.now()
print(f"The date and time is {now}")
"""
''' 4
from math import pi
r = float(input ("Input the radius of the circle : "))
print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))
'''
""" 5
first_name = input("Enter first name ")
last_name = input("Enter last name ")
print(last_name, first_name)
"""
""" 6
user = input("Enter sequence seperated by comma ")
print(user.split(","))
print(tuple(user.split(",")))
"""
"""  7
filename = input("Enter filename ")
ext = filename.split(".")
print("The extension of this file is: ",ext[-1])
"""
""" 8
color_list = ["Red","Green","White" ,"Black"]
print(color_list[0],color_list[-1])
"""
"""9
#This questions uses % for formating. There has be a letter next to the % so that its not read as a str
exam_st_date = (11, 12, 2014)
print( "The examination will start from : %i / %i / %i"%exam_st_date)
"""
"""   10
x = str(input("Enter integer "))
result = int(x) + int((x+x)) + int((x+x+x))
print(result)
"""

#print(int.__doc__) question 11

def division(num):
    if num % 15 == 0:
        return f"{num} is divisable by 15"
    else:
        return f"{num} not divisable by 15"

list1 = [15, 30, 40, 45, 55]
for i in list1:
    print(division(i))