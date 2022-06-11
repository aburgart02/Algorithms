def binary_search(number, array):
    left = 0
    right = len(array) - 1
    while left < right:
        center = (right + left) // 2
        if number <= array[center]:
            right = center
        else:
            left = center + 1
    if array[left] == number:
        return left
    return -1


print(binary_search(87, [2, 5, 7, 12, 33, 87, 216, 367]))
