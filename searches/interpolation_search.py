def interpolation_search(number, array):
    left = 0
    right = len(array) - 1
    while left <= right and array[left] <= number <= array[right]:
        pos = left + int((right - left) * (number - array[left]) / (array[right] - array[left]))
        if number == array[pos]:
            return pos
        if number > array[pos]:
            left = pos + 1
        else:
            right = pos - 1
    return -1


print(interpolation_search(87, [2, 5, 7, 12, 33, 87, 216, 367]))