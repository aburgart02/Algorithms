import random


p = 2 ** 64 - 59
x = random.randint(1, p - 1)


def get_pref(s):
    pref = [0] * len(s)
    pref[0] = ord(s[0])
    for k in range(1, len(s)):
        pref[k] = (pref[k - 1] * x + ord(s[k])) % p
    return pref


def get_xk(s):
    xk = [0] * (len(s) + 1)
    xk[0] = 1
    for k in range(1, len(s) + 1):
        xk[k] = xk[k - 1] * x % p
    return xk


def cut_prefix(st, s, k, xk):
    return (st + p - s * xk[k] % p) % p


def rabin_karp(s, i, j):
    pref = get_pref(s)
    xk = get_xk(s)
    return cut_prefix(pref[j], pref[i - 1], j - i + 1, xk) if i > 0 else pref[j]


print(rabin_karp('abcbcba', 1, 3))
print(rabin_karp('abcbcba', 3, 5))
print(rabin_karp('abcabc', 0, 2))
print(rabin_karp('abcabc', 3, 5))
print(rabin_karp('abcabcdfdf', 6, 7))
print(rabin_karp('abcabcdfdf', 8, 9))