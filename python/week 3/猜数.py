m = 100
c = True
while c == True:
    n = eval(input())
    if(n > m):
        print('larger than expected')
    elif(n < 100):
        print('less than expected')
    elif(n == 100):
        print('you win')
        c == False
        break
