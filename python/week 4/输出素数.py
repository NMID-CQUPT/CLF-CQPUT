m = eval(input())
a = []
for i in range(2, m):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        a.append(i)
print(a)
