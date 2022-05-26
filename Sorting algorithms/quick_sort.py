import random


def quicksort(numbers):
    if len(numbers) <= 1:
        return numbers
    q = random.choice(numbers)
    left = [x for x in numbers if x < q]
    center = [q] * numbers.count(q)
    right = [x for x in numbers if x > q]
    return quicksort(left) + center + quicksort(right)


print(quicksort([12, 33, 2, 87, 216, 7, 5, 367]))