def counting_sort(numbers):
    array = [0] * (max(numbers) + 1)
    result = []
    for number in numbers:
        array[number] += 1
    for i in range(len(array)):
        result += [i] * array[i]
    return result


print(counting_sort([12, 33, 2, 87, 216, 7, 5, 367]))