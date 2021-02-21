import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
s = input().split(' ')
x=0
y=0
for i in range(len(s)):
    if s[i] == "boom":
        x=x+1
    if s[i]=="ding":
        y=y+1
    if s[i]=="bing":
        y=y-1
    if s[i]=="ts":
        x=x-1
print(str(x) + " "+ str(y))
"""
x,y=0,0
for m in input().split():
 if m=="ts":x=max(x-1,0)
 elif m=="boom":x=min(x+1,30)
 elif m=="ding":y=max(y-1,0)
 else:y=min(y+1,10)
print(x,y)
"""