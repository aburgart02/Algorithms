def insertion_sort(numbers):
    for i in range(len(numbers)):
        key = numbers[i]
        j = i - 1
        while j >= 0 and numbers[j] > key:
            numbers[j + 1] = numbers[j]
            j -= 1
        numbers[j + 1] = key
    return numbers


print(insertion_sort([12, 33, 2, 87, 216, 7, 5, 367]))