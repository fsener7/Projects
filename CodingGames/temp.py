
import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
n = int(input())
for i in range(n):
    b, t = [int(j) for j in input().split()]
    b= 9/5*b+32
    t= 9/5*t+32
    if b==t:
        print("Same")
    if b>t:
        print("Higher")
    if b<t:
        print("Lower")