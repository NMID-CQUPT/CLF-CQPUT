import numpy as np
m = eval(input())
a = np.eye(m)
row, col = np.diag_indices_from(a)
a[row, col] = np.arange(0, m, 1)+1
print(a)



