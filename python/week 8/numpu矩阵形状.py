import numpy as np


def main():
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    n, m = input().split()
    n = int(n)
    m = int(m)
    a = np.array(a)
    if n*m==12:
        b=a.reshape(n,m)
        print(b)
    else:
        print('NO')


if __name__ == '__main__':
    main()

