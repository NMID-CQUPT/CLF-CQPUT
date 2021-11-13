m = eval(input())
n = eval(input())
# 求最大公约数
a, b = m, n
if a < b:
    a, b = b, a
while b != 0:
    temp = a % b
    a = b
    b = temp
print(a, end=' ')
print(int(m*n/a))
# 求最小公倍数
