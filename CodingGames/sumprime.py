import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

a = int(input())
sum = 0
for i in range(a):
    x=int(input())
    for y in range(2,1000):
        res = x%y
        if res==0:
            sum = sum + x
            break
print(sum)