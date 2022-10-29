from math import ceil


def swap_list(arr):
    l = len(arr)
    if l > 1:
        arr[ceil(l/2)-1], arr[-1] = arr[-1], arr[ceil(l/2)-1]
    return arr  