def gnome_sort(numbers):
    i, j = 1, 2
    while i < len(numbers):
        if numbers[i - 1] < numbers[i]:
            i = j
            j += 1
        else:
            numbers[i], numbers[i - 1] = numbers[i - 1], numbers[i]
            i -= 1
            if i == 0:
                i = j
                j += 1
    return numbers


print(gnome_sort([12, 33, 2, 87, 216, 7, 5, 367]))