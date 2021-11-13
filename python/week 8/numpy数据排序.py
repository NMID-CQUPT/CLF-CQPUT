import numpy as np


def main():
    arr = input("")
    a = [float(x) for x in arr.split()]
    a = np.array(a)
    print(np.sort(a))


if __name__ == '__main__':
    main()

