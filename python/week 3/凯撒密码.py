a=input()
if a[1]==' ':
    x=int(a[0:1])
    y=a[2:]
elif a[2]==' ':
    x=int(a[0:2])
    y=a[3:]

for p in y:
    if ord('a') <= ord(p) <= ord('z'):
        print(chr( ord('a') + (ord(p) - ord('a') + x )%26), end='')
    elif ord('A') <= ord(p) <= ord('Z'):
        print(chr( ord('A') + (ord(p) - ord('A') + x )%26), end='')
    else:
        print(p,end='')