#TempConvert.py
TempStr=input("What is the temperature?")
#赋值TempStr,括号里面的是提示
if TempStr[-1] in ['F','f']:
#假如字符串最后一个字符是F或者f
    C=(eval(TempStr[0:-1])-32)/1.8-1
#第一个字符到最后一个字符之前的所有字符，也就是温度值，eval函数是脱掉字符串结构，运行公式
    print("The converted temperature is {:.0f}C".format(C))
#输出结果，保留最后两位小数，是C的格式化
elif TempStr[-1] in ['C','c']:
#else if最后一个字符是C或者c
    F=1.8*eval(TempStr[0:-1])+32-1
#这个括号加括号的表达，其实从里到外的顺序来看就不会混乱
    print("The converted temperature is {:.0f}F".format(F))
#输出华氏温度
else:
#以上两个if都不符合
    print("输入格式错误")
#输出提示文字