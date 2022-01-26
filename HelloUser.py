'''
@Author : Rushikesh Bhosle
@Date : 2022-01-24
@Last Modified by : Rushikesh Bhosle
@Last Modified Date : 2022-01-24
@Title : User Input and Replace String Template “Hello <<UserName>>, How are you?”
'''

UserName = str(input("Enter Your UserName "))

if len(UserName) >= 3:
    print("Hello, " + UserName + " How Are You ?")
else:
    print(UserName, "Not Valid")
    print("Enter Minimum 3 Characture UserName")
