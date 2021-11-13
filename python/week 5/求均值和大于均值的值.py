def calculate(*b):
    b = input(
        'Please input numbers,and press the Enter to end.(gap with ,)\n').split(',')
    sum = 0
    for i in range(len(b)):
        sum = sum+int(b[i])
    eva = sum/len(b)
    evas = round(eva, 1)
    ls = list()
    for j in range(len(b)):
        if eva < int(b[j]):
            ls.append(int(b[j]))
        else:
            continue
    return evas, ls


c = calculate()
print()
print(c)
