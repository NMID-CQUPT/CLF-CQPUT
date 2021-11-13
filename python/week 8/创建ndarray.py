import numpy as np
n, m = map(int, input().split())

array = np.zeros([1, n], dtype=np.float)
array[0][m-1] = 1
print(array)
