import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
for i in range(n):
    t = input()
    if sum(list(map(int, t[:3]))) == sum(list(map(int, t[3:]))):
        print("true")
    else:
        print("false")

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

