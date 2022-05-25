#This file contains the Floyd & Warshall algorithm
#for finding the weighted neighbor matrix of a graph.

def Floyd_Warshall(T):
    n = len(T)
    p = {}
    T_old = T
    for k in range(0, n):
        for i in range(0, n):
            for j in range(0, n):
                if i == j:
                    T[i][j] = 0
                if T_old[i, j] > T_old[i, k] + T_old[k, j]:
                    T[i, j] = T_old[i, k] + T_old[k, j]
                    p[j, i] = k
        T_old = T
    return T, p
