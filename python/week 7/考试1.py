def a(x):
    if 0 < x < 5:
        return x
    elif 5 <= x < 15:
        return x+6
    elif x >= 15:
        return x-6
    else:
        return 'illegal input'


m = eval(input())
print(a(m))
