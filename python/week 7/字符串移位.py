def f(s, n):
    p = ''
    if s == '':
        return p
    t = (len(s)-n) % len(s)
    p = s[t:]
    p += s[:t]
    return p


s = input()
n = int(input())
print(f(s, n))
