def trivial_prefix_function(string):
    p = [0] * len(string)
    for i in range(len(string)):
        for k in range(i):
            if string[:k+1] == string[i-k:i+1]:
                p[i] = k + 1
    return p


print(trivial_prefix_function('abcdabcabcdabcdab'))