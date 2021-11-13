m = input().split(' ')
if m[0] > m[1]:
    if m[0] > m[2]:
        print(m[0])
    else:
        print(m[2])
elif m[0] < m[1]:
    if m[1] > m[2]:
        print(m[1])
    else:
        print(m[2])
elif m[0] == m[1]:
    if m[0] > m[2]:
        print(m[0])
    elif m[0] < m[2]:
        print(m[2])
    else:
        print(m[0])
