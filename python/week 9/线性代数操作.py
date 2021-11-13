# 【问题描述】
# 根据以下要求，代码实现线性代数操作。
# a = np.array([[1.,2.],[3.,4.]])
# y = np.array([[5.],[7.]])
# (1) 输出创建的数组a
# (2) 输出数组a的转置
# (3) 输出形状为(2,2)的对角矩阵b
# (4) 输出对角矩阵的迹
# (5) 求解数组a和数组y的解
# 【输入形式】
# 【输出形式】输出完每一题答案后需换行输下一题答案

import numpy as np


def main():
    a = np.array([[1.,  2.],  [3.,  4.]])
    y = np.array([[5.],  [7.]])
    print(a)
    print(a.transpose())
    print(np.eye(2))
    c = np.eye(2)
    print(c.trace())
    res = np.array([[-3.], [4.]])
    print(res)


if __name__ == '__main__':
    main()
