# 元素去重可以考虑集合的元素不可重复性
def BubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


# 把输入字符串去重
m = input()
n = set(m)
a = list(n)
# 将字符串变成ASCII码进行冒泡排序
b = list()
for letter in a:
    asc = ord(letter)
    b.append(asc)
result = BubbleSort(b)
# 将排好序的ASCII码换回字符串按顺序打印
c = list()
for j in result:
    ch = chr(j)
    print(ch, end='')
