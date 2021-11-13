def FengJie(n):
    lt = []
    while n != 1:
        for i in range(2, int(n+1)):
            if n % i == 0:
                lt.append(i)
                n = n/i
                break
    print(lt)


m = eval(input())
FengJie(m)
