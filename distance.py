'''
Author: Rushikesh Bhosle
Date: 2022-01-25
Last Modified by: Rushikesh Bhosle
Last Modified time: 2022-01-25
Title : Distance Program.
'''

#import the math function for operation.
import math

''' Description : Creating Function for distance
    Parameter: x1,x2,y1,y2
'''
def Distance(x1,y1,x2,y2):
    dis=((y2*y2-y1*y1)+(x2*x2-x1*x1))
    print(math.sqrt(dis))
try:
    pointX2=int(input("enter a x value of slope: "))
    pointY2= int(input("Enter a y value of a slope "))
    x1=0
    y1=0
    Distance(x1,y1,pointX2,pointY2)
except Exception as e:
    print("Enter int input",e)
