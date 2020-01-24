import math
import sys

def func(a,b,c,x): return math.sqrt(c*x + 62.7 * math.exp(x))/(a*math.pow(x,2) + 7*x + b * math.log(x))

#1
a = 7.2; b = 14.3; c = 13.4; x = 5.6
print(func(a,b,c,x))

#2
import numpy as np
try:
    arg = np.array(sys.argv[1:]).astype(float)
    # python L2.py 7.2 14.3 13.4 5.6
    print(func(arg[0],arg[1], arg[2], arg[3]))
except: 'No param'

#3
arg = np.array(input('Write a, b, c, x: ').split(' ')).astype(float)
print(func(arg[0],arg[1], arg[2], arg[3]))
