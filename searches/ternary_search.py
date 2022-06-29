def ternary_search(number, array):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid1 = (right - left) // 3
        mid2 = right - mid1
        if number == array[mid1]:
            return mid1
        if number == array[mid2]:
            return mid2
        if number < array[mid1]:
            right = mid1 - 1
        elif number > array[mid2]:
            left = mid2 + 1
        else:
            left = mid1 + 1
            right = mid2 - 1
    return -1


print(ternary_search(87, [2, 5, 7, 12, 33, 87, 216, 367]))