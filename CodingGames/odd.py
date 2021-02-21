import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
sum=0
curr=1
while i<n:
    sum+=curr
    curr+=2
    i+=1

#if(n==1):
#   print(1)
#else:
#   print(n+(n-1)*n)
print(sum)