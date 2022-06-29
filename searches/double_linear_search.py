def double_linear_search(number, array):
    left = 0
    right = len(array) - 1
    while left <= right:
        if number == array[left]:
            return left
        elif number == array[right]:
            return right
        else:
            left += 1
            right -= 1
    return -1


print(double_linear_search(87, [2, 5, 7, 12, 33, 87, 216, 367]))