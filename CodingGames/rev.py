import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

l = input()
s = "abcdefghijklmnopqrstuvwxyz"
t=0
for i in range(26):
    for j in range(26):
        t+=i
        print(s[i])