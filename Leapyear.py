'''
@Author : Rushikesh Bhosle
@Date : 2022-01-24
@Last Modified by : Rushikesh Bhosle
@Last Modified Date : 2022-01-24
@Title : print the year leap or not
'''


print("enter a year")
year = int(input())
if (year%100==0) and (year%400==0) or (year%4==0):
    print('Leap Year')
else:
     print('Not Leap Year')