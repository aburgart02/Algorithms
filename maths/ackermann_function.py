def ackermann_function(m, n):
    if m == 0:
        return n + 1
    if m > 0 and n == 0:
        return ackermann_function(m - 1, 1)
    if m > 0 and n > 0:
        return ackermann_function(m - 1, ackermann_function(m, n - 1))


print(ackermann_function(3, 5))