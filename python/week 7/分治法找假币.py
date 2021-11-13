
def Sum(coins, start, n):
    sum = 0
    k = 0
    for i in coins[start:]:
        k += 1
        if n >= k:
            sum += i
    return sum


def findFalseCoin(coins, start, n):
    if n == 1:
        print('Fake coin:{}'.format(int(start)))
        return
    elif n % 2 == 0:
        if Sum(coins, int(start), int(n/2)) < Sum(coins, int(start+n/2), int(n/2)):
            return findFalseCoin(coins, int(start), int(n/2))
        elif Sum(coins, int(start), int(n/2)) > Sum(coins, int(start+n/2), int(n/2)):
            return findFalseCoin(coins, start+n/2, n/2)
        else:
            print('Fake coin is not found')
            return
    elif n % 2 != 0:
        if Sum(coins, int(start), int(n//2)) < Sum(coins, int(start+n//2), int(n//2)):
            return findFalseCoin(coins, int(start), int(n//2))
        elif Sum(coins, int(start), int(n//2)) > Sum(coins, int(start+n//2), int(n//2)):
            return findFalseCoin(coins, int(start+n//2), int(n//2))
        else:
            print('Fake coin:{}'.format(start+n-1))
            return


k = 0
a = list(map(int, input().split(',')))
for i in a:
    k += 1
findFalseCoin(a, 0, k)
