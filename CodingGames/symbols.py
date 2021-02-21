import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

mode = input()
s = input()
summ=0
least = mode.split()
for i in range(len(least)):
    summ = sum(map(ord, least[i]))
print(str(summ))