from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.
n = int(input())
for i in range(1,n+1):
    count = 1
    for j in range(1,i):
        print(" ",end="")
        count = count + 1
    num = i 
    for j in range(count,n+1):
        print(num,end="") 
        num = num + 1
    print()
for i in range(n-1,0,-1):
    count = 1
    for j in range(1,i):
        print(" ",end="") 
        count = count + 1
    num = i 
    for j in range(count,n+1): 
        print(num,end="")
        num = num + 1 
    print()
