def sort_dictionary(dict):
    def sort_arr(arr):
        i = 1
        while i < len(arr):
            j = i
            while j > 0:
                if arr[j] < arr[j-1]:
                    arr[j], arr[j-1] = arr[j-1], arr[j]
                j -= 1
            i += 1
        return arr

    new_dict= {}
    for item in dict.items():
        new_dict[item[1][1]] = (item[0], item[1][0])
    sorted_key = sort_arr(list(new_dict.keys()))
    res = []
    for key in sorted_key:
        res.append(new_dict[key])
    return res
