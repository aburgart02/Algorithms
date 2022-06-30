def prefix_function(string):
    p = [0] * len(string)
    for i in range(1, len(string)):
        j = p[i - 1]
        while j > 0 and string[i] != string[j]:
            j = p[j - 1]
        if string[i] == string[j]:
            j += 1
        p[i] = j
    return p


print(prefix_function('abcdabcabcdabcdab'))