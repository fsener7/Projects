import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
for i in range(n):
    x = int(input())
    #print(bin(x).replace("0b", "")) 
    print(bin(x)[2:])
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

