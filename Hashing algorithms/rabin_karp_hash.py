import random


p = 2 ** 64 - 59
x = random.randint(1, p - 1)


def rabin_karp_hash(s):
    if len(s) == 1:
        return ord(s[0])
    h = 0
    for k in range(len(s)):
        h = h * x + ord(s[k])
    return h % p


print(rabin_karp_hash('abcde'))