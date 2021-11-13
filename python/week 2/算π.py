from random import random, seed 
from math import sqrt


seed(123)
DARTS = eval(input())
hits =0.0


for i in range(1,DARTS+1):
    x,y=random(),random()
    dist = sqrt(x**2+y**2)
    if dist<=1.0:
        hits=hits+1
pi = 4*(hits/DARTS)
print('{:.6f}'.format(pi))

