from math import *
a,b,c = map(float,input().split())
'''b=float(input("b"))
c=float(input("c"))'''
if b**2-4*a*c < 0:
    print("No")
else:
    x1=(-b+sqrt(b**2-4*a*c))/2*a
    x2=(-b-sqrt(b**2-4*a*c))/2*a
    if x1>x2:
        print("{:.2f} {:.2f}".format(x1,x2))
    else:
        print("{:.2f} {:.2f}".format(x2,x1))