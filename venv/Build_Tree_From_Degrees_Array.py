import numpy as np


def build_tree(arr):
    N = len(arr)
    sum = 0
    tree = np.zeros(N)
    for i in range(N):
        sum = sum + arr[i]
    if (sum / 2) + 1 != N:
        print(sum)
        print("The input array is not a tree degrees array")
        return
    arr = np.sort(arr)
    for k in range(N):
        if arr[k] > 1:
            j=k
            break
    for i in range(N-2):
        tree[i] = j
        arr[j] = arr[j] - 1
        if arr[j] == 1:
            j = j + 1
    tree[N-2] = tree[N-3]
    tree[N-1] = 0
    return tree

