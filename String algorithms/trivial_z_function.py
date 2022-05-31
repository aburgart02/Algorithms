def trivial_z_function(string):
    z = [0] * len(string)
    for i in range(1, len(string)):
        while i + z[i] < len(string) and string[z[i]] == string[i + z[i]]:
            z[i] += 1
    return z


print(trivial_z_function('abacaba'))