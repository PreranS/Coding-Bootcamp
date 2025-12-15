def reverse_array(arr):
    return arr[::-1]


def sort_array(arr, ascending=True):
    return sorted(arr, reverse=not ascending)


def binary_search(arr, key):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == key:
            return mid
        if arr[mid] < key:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


if __name__ == "__main__":
    arr = [5, 2, 9, 1, 7]
    print(reverse_array(arr))
    print(sort_array(arr, ascending=True))
    sorted_arr = sort_array(arr)
    print(binary_search(sorted_arr, 7))
