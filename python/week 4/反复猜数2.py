m = 100
c = True
count = 0
while c == True:
    count = count+1
    try:
        n = eval(input())
        if(n > m):
            print('larger than expected')
        elif(n < 100):
            print('less than expected')
        elif(n == 100):
            print('you have tried {:.0f} times, you win'.format(count))
            c == False
            break
    except NameError:
        print("input error")
