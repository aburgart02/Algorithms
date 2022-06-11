from rabin_karp_hash import p, x, rabin_karp_hash


def pow_mod_p(x, n):
    if n == 0:
        return 1
    if n % 2 == 1:
        return x * pow_mod_p(x, n - 1) % p
    y = pow_mod_p(x, n // 2)
    return y * y % p


ix = pow_mod_p(x, p - 2)


def concat(s, t, t_len):
    xt = pow_mod_p(x, t_len)
    return (s * xt + t) % p


def cut_suffix(st, t, t_len):
    ixt = pow_mod_p(ix, t_len)
    return ((st + p - t) % p) * ixt % p


def cut_prefix(st, s, t_len):
    xt = pow_mod_p(x, t_len)
    return (st + p - s * xt % p) % p


s = rabin_karp_hash('abc')
t = rabin_karp_hash('def')
st = rabin_karp_hash('abcdef')
print(s, t, st)
print(concat(s, t, 3))
print(cut_suffix(st, t, 3))
print(cut_prefix(st, s, 3))