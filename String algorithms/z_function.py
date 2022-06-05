def z_function(string):
    z = [0] * len(string)
    left, right = 0, 0
    for i in range(1, len(string)):
        if i <= right:
            z[i] = min(right - i + 1, z[i - left])
        while i + z[i] < len(string) and string[z[i]] == string[i + z[i]]:
            z[i] += 1
        if i + z[i] - 1 > right:
            left = i
            right = i + z[i] - 1
    return z


print(z_function('abacaba'))