import random


class RabinKarp:
    def __init__(self, s):
        self.p = 2 ** 64 - 59
        self.x = random.randint(1, self.p - 1)
        self.pref = self.get_pref(s)
        self.xk = self.get_xk(s)

    def get_pref(self, s):
        pref = [0] * len(s)
        pref[0] = ord(s[0])
        for k in range(1, len(s)):
            pref[k] = (pref[k - 1] * self.x + ord(s[k])) % self.p
        return pref

    def get_xk(self, s):
        xk = [0] * (len(s) + 1)
        xk[0] = 1
        for k in range(1, len(s) + 1):
            xk[k] = xk[k - 1] * self.x % self.p
        return xk

    def cut_prefix(self, st, s, k, xk):
        return (st + self.p - s * xk[k] % self.p) % self.p

    def rabin_karp(self, i, j):
        return self.cut_prefix(self.pref[j], self.pref[i - 1], j - i + 1, self.xk) if i > 0 else self.pref[j]


rk = RabinKarp('abcbcba')
print(rk.rabin_karp(1, 3))
print(rk.rabin_karp(3, 5))
rk = RabinKarp('abcabc')
print(rk.rabin_karp(0, 2))
print(rk.rabin_karp(3, 5))
rk = RabinKarp('abcabcdfdf')
print(rk.rabin_karp(6, 7))
print(rk.rabin_karp(8, 9))