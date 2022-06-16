#This file contains a method to find the diameter of a straigh line graph (p).
#The diameter of a graph is the most expensive route from a single node to another.
#For the solution, the dynamic programming methood is useed.
# The diameter_dp function gets an array of weights and calculates the most expensive sequence.
# The function return the matrix, the diagonal itself, and an array of 2 indicators for the sequence itself

# The function best does the same thing, but has complexity of O(n).

import numpy as np

def diameter_dp(arr):
    n = len(arr)
    d = 0
    seq = [0,0]
    mat = np.zeros((n, n))
    for i in range(n):
        for j in range(n): #O(n^2)
            if i == j:
                mat[i][j] = arr[i]
            if i + 1 < n:
                mat[i][j] = mat[i][j-1] + arr[j]
            if i > j:
                mat[i][j] = 0
            if mat[i][j] >= d:
                d = mat[i][j]
                seq[0] = i
                seq[1] = j
    return mat, d, seq

def cycle_diameter_dp(arr):
    n = len(arr)
    d = 0
    seq = [0,0]
    mat = np.zeros((n, n))
    for i in range(n):
        for j in range(n): #O(n^2)
            if i == j:
                mat[i][j] = arr[i]
            if i + 1 < n:
                mat[i][j] = mat[i][j-1] + arr[j]
            if i>j:
                mat[i][j] = 0
            if mat[i][j] >= d:
                d = mat[i][j]
                seq[0] = i
                seq[1] = j
    for i in range(n):
        for j in range(n):  # O(n^2)
            if i > j:
                if i - j == 1:
                    mat[i][j] = mat[0][n-1]
                    continue
                mat[i][j] = mat[0][n-1] - mat[j+1][i-1]
                if mat[i][j] >= d:
                    d = mat[i][j]
                    seq[0] = i
                    seq[1] = j
    return mat, d, seq

def best(arr):
    count = 0
    flag = 0
    max = - 1
    sum = 0
    seq = [0, 0]
    for i in range(len(arr)):#O(n)
        sum = sum + arr[i]
        count += 1
        if max < sum:
            if flag ==1:
                seq[0] = i - count + 1
                flag = 0
            max = sum
            seq[1] = i
        if sum < 0:
            flag = 1
            sum = 0
            count = 0
    return max, seq

def cycle_best(arr):
    sum_straight = np.sum(arr)
    negative_arr = arr
    for i in range(len(arr)):
        negative_arr[i] = -1*arr[i]
    min_best,seq = best(negative_arr)
    if max(sum_straight + min_best,sum_straight) == sum_straight:
        return sum_straight, [0,len(arr)]
    else:
        return sum_straight + min_best , [seq[0]+1, seq[1]-1]
