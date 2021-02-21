import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
summ=0
for i in range(n):
    if i % 3 == 0  or i % 5 == 0 or i % 7 == 0:
        summ=summ+i
print(str(summ))