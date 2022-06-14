# The bottle problem:
# Two bottetles: b1 with a volume of m and b2 with volume a of n.
# Our goal is to create a matrix that describes the various volume divisons.
import numpy as np

def Bottle_problem_matix_create(b1, b2):
    size = (b1 + 1)*(b2 +1)
    mx = max(b1,b2)
    mat = np.zeros([size, size])
    for i in range(b1):
        for j in range(b2):
            index = get_index(mx, i, j)
            mat[index][get_index(mx, 0, j)] = 1
            mat[index][get_index(mx, i, 0)] = 1
            mat[index][get_index(mx, b1, j)] = 1
            mat[index][get_index(mx, i, b2)] = 1
            mat[index][get_index(mx, min(b1, i+j), i + j - min(b1, i + j))] = 1
            mat[index][get_index(mx, i + j -min(b2, i+j),  min(b2, i + j))] = 1
    return mat

def Bottle_problem(b1, b2, n):
    mat = Bottle_problem_matix_create(b1, b2)
    size = (b1 + 1) * (b2 + 1)
    path = np.zeros([size, size])
    for i in range(size):
        x1, y1 = get_pair_from_index(n, i)
        for j in range(size):
            x2, y2 = get_pair_from_index(n, i)
            if mat[i, j] != np.inf:
                path[i, j] = [[x1,y1],[x2,y2]]
    for k in range(size):
        for i in range(size):
            for j in range(size):
                if mat[i,j] > mat[i,k] + mat[k,j]:
                    mat[i,j] = mat[i,k] + mat[k,j]
                    path[i,j] = [path[i,k] ,paths[k,j]]
    return path



def get_pair_from_index(n, i):
    return i/(n + 1), i%(n + 1)


def get_index(n, i, j):
    return (n+1)*i + j
