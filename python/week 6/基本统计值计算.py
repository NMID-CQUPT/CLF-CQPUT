def getNum():  # 获取用户不定长度的输入
    M = input().split(',')
    m = list(map(lambda x: float(x), M))
    return m


def mean(numbers):  # 计算平均值
    sum = 0
    for i in range(len(numbers)):
        sum += numbers[i]
    ave = sum/len(numbers)
    return ave


def dev(numbers, mean):  # 计算标准差
    sum = 0
    for i in range(len(numbers)):
        sum += (numbers[i]-mean)**2
    sum = sum/(len(numbers)-1)
    #print(sum, end=',')
    SD = pow(sum, 0.5)
    # print(sum)
    return SD

# 判断一个数是整型还是浮点型并返回它的值


def judge(a):
    n1 = str(float(a))
    n2 = n1.split('.')
    if n2[1] == '0':
        return int(a)
    else:
        return a


def median(numbers):  # 计算中位数
    numbers.sort()
    if len(numbers) % 2 == 0:
        medi = (numbers[int(len(numbers)/2)] +
                numbers[int(len(numbers)/2)-1])*0.5
    else:
        medi = numbers[int((len(numbers)-1)/2)]
    c = judge(medi)
    return c

    # n是个列表
n = getNum()  # 主体函数
m = mean(n)
x = dev(n, m)
y = median(n)
# print("Average:{:.2f}".format(m))
# print("Average:{:.2f},Standard Deviation:{:.2f}".format(m, x))
print("Average:{:.2f},Standard Deviation:{:.2f},Median:{}".format(m, x, y))
