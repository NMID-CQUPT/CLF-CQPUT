import random

n = int(input())
random.seed(n)
m = random.randint(1, n)
# print(m)

ls = list(range(1, n+1))
ls2 = ls.copy()
print(ls2)

k = n//m
# print(k)
a = list(range(1, k+1))
# print(a[0],a[1])
for i in range(k):
    index = (a[i]*m)-(i+1)
    ls.pop(index)
print(ls)
