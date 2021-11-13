def a(x, N):
    ls = [3]
    ls.append(x)
    for i in range(2, N):
        x = ls[i-2]+ls[i-1]
        if x > 120:
            print("Age"+str(i+1)+'is larger than 120!')
        else:
            a(x, N)
    print(ls[::-1])


XN = input()
x, n = XN.split(',')
x, n = int(x), int(n)
a(x, n)
