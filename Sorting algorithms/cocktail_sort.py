def cocktail_sort(numbers):
    left = 0
    right = len(numbers) - 1
    while left <= right:
        for i in range(left, right):
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
        right -= 1
        for i in range(right, left, -1):
            if numbers[i] < numbers[i - 1]:
                numbers[i], numbers[i - 1] = numbers[i - 1], numbers[i]
        left += 1
    return numbers


print(cocktail_sort([12, 33, 2, 87, 216, 7, 5, 367]))