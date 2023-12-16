from math import *
from collections import *
from sys import *
from os import *

N = int(input())

# Base cases for the first two Fibonacci numbers
fibonacci = [0, 1]

if N <= 1:
    print(fibonacci[N])
else:
    for i in range(2, N + 1):
        # Calculate the next Fibonacci number by adding the last two numbers
        fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])
    
    print(fibonacci[N])

