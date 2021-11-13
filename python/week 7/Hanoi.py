def Hanoi(n, A, B, C):  # 参数1：>=1就继续；参数2：要移动的盘；参数3：中转位置；参数4：盘的目的地
    global count
    if n == 1:
        count += 1
        print('[STEP{: >4.0f}]'.format(count), A, end='')
        print('->', end='')
        print(C)
        # A,'->',C
        return
    else:
        Hanoi(n-1, A, C, B)
        count += 1
        print('[STEP{: >4.0f}]'.format(count), A, end='')
        print('->', end='')
        print(C)
        Hanoi(n-1, B, A, C)


count = 0
m = eval(input())
Hanoi(m, 'A', 'B', 'C')
