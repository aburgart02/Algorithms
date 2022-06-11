def eratosthenes_sieve(n):
    sieve = list(range(n + 1))
    sieve[1] = 0
    for i in sieve:
        if i > 1:
            for j in range(i ** 2, len(sieve), i):
                sieve[j] = 0
    [print(e, end=' ') for e in sieve if e != 0]


eratosthenes_sieve(100)