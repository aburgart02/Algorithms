def levenshtein_distance(f, s):
    opt = []
    [opt.append([x for x in range(len(f) + 1)]) if i == 0 else opt.append([i] + [0] * len(f)) for i in range(len(s) + 1)]
    for i in range(1, len(s) + 1):
        for j in range(1, len(f) + 1):
            if f[j - 1] == s[i - 1]:
                opt[i][j] = opt[i - 1][j - 1]
            else:
                opt[i][j] = min(opt[i][j - 1] + 1, opt[i - 1][j] + 1, opt[i - 1][j - 1] + 1)
    return opt[len(s)][len(f)]


print(levenshtein_distance('дивергенция', 'диверсификация'))