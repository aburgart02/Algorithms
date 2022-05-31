def binpow(number, pow):
    if pow == 0:
        return 1
    if pow % 2 == 0:
        return binpow(number, pow // 2) ** 2
    else:
        return binpow(number, pow - 1) * number


print(binpow(31, 23))