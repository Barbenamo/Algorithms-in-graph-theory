# This file contains methods that finds the maximum sub matrix inside a n*m matrix.

import numpy as np

def Sub_Matrix_dp(mat):
    mx = -1
    sum = 0
    index = [[0, 0], [0, 0]]
    n = len(mat)
    m = len(mat[0])
    H = np.zeros([n,m])
    H[0][0] = mat[0][0]
    for i in range(1,n):
        H[i][0] = mat[i][0] + H[i-1][0]
    for j in range(1, m):
        H[0][j] = mat[0][j] + H[0][j-1]

    for i in range(1,n):
        for j in range(1,m):
            H[i][j] = mat[i][j] + H[i-1][j] + H[i][j-1] -H[i-1][j-1]
    for i in range(1,n):
        for j in range(1,m):
            for k in range(i,n):
                for t in range(j,m):
                    sum = H[k][t] - H[k][j-1] - H[i-1][t] + H[i-1][j-1]
                    if sum >= mx:
                        mx = sum
                        index[0][0] = i
                        index[0][1] = j
                        index[1][0] = k
                        index[1][1] = t
    return H , index, mx

