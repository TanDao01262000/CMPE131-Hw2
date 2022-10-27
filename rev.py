def reverse_list(arr):
    l = len(arr)
    for i in range(l//2):
        arr[i], arr[l-i-1] = arr[l-i-1], arr[i]

    # return list(reversed(arr))
    return arr
