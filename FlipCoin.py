'''
@Author : Rushikesh bhosle
@Date : 2022-01-24
@Last Modified by : Rushikesh Bhosle
@Last Modified Date : 2022-01-24
@Title : Flip Coin Print Percentage head and tails
'''

import random
head=0
tail=0
print("Enter number of times to flip coin")


n=int(input())
if n < 0:
    print("Please enter the positive number")

for i in range (n):
     num = random.randint(0,1)
     if num < 0.5:
        head+=1
else:
   tail += 1

sum=head + tail
hp=float(head/sum*100)
tp=float(tail/sum*100)
print("Head percentage =",hp)
print("Tail percentage =",tp)

