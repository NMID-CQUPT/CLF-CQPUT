# TempConvert.py
TempStr = input("What is the temperature?")
if TempStr[-1] in ['F', 'f']:
    C = (eval(TempStr[0:-1])-32)/1.8-1
    print("The converted temperature is {:.0f}C".format(C))
elif TempStr[-1] in ['C', 'c']:
    F = 1.8*eval(TempStr[0:-1])+32-1
    print("The converted temperature is {:.0f}F".format(F))
else:
    print('Input is wrong!')
