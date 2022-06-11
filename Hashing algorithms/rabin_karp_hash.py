import random


p = 2 ** 64 - 59


def rabin_karp_hash(s):
    if len(s) == 1:
        return ord(s[0])
    x, h = random.randint(1, p - 1), ord(s[0])
    for k in range(1, len(s)):
        h = h * x + ord(s[k])
    return h % p


print(rabin_karp_hash('abcde'))