ls = ['the lord of the rings', 'anaconda',
      'legally blonde', 'gone with the wind']

try:
    m = input()
    ls1 = list()
    if m == '1':
        for i in range(10):
            ls1.append(i*i*i)
        print(ls1)

    ls2 = list()
    if m == '2':
        for i in range(10):
            if i % 2 == 0:
                ls2.append(i*i*i)
        print(ls2)

    ls3 = list()
    if m == '3':
        for i in range(10):
            if i % 2 != 0:
                ls3.append((i, i*i*i))
        tur1 = ls3
        print(tur1)

    if m == '4':
        for i in range(len(ls)):
            ls[i] = ls[i].capitalize()
        print(ls)

except:
    print('End of the program')
