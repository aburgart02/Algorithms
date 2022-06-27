def prime_check(number):
    if number <= 3:
        return number > 1
    if not number % 2 or not number % 3:
        return False
    i = 5
    stop = int(number ** 0.5)
    while i <= stop:
        if not number % i or not number % (i + 2):
            return False
        i += 6
    return True


print(prime_check(13))
print(prime_check(71))
print(prime_check(7686814307))
print(prime_check(100))