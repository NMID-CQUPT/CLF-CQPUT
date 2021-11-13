def trigon(list, A_list, n):  # list总序列，alist每行序列
    blist = [1]
    if n > 0:
        for j in range(len(A_list)):
            if j < len(A_list) - 1:
                sum = A_list[j] + A_list[j+1]
                blist.append(sum)
        blist.append(1)
        list.append(blist)
        n -= 1
        trigon(list, blist, n)


if __name__ == "__main__":
    list1 = [1]  # 第一行
    list2 = [1, 1]  # 第二行
    n = int(input())
    list = []
    list.append(list1)
    list.append(list2)
    trigon(list, list2, n - 2)  # 计算出整个杨辉三角
    l = len(str(max(list[n-1])))
    for i in range(0, n):  # 输出n行
        j = 0
        while j < n-i:  # 打印每个数之间的间隔
            print(' '*l, end='')
            j += 1
        j = 0
        while j <= i:
            print(' '*(l-len(str(list[i][j]))), end='')  # 补位
            print(list[i][j], end='')
            print(' '*l, end='')
            j += 1
        print(end='\n')
