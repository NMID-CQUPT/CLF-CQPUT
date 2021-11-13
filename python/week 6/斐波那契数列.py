def fbi(N):
    if N == 1 or N == 2:
        return 1
    else:
        return fbi(N-1)+fbi(N-2)


M = eval(input())
print(fbi(M))
