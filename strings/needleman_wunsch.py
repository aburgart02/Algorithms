def global_alignment(A, B, mch=1, mis=-1, gap=-1):
    M = [[0 for _ in range(len(B) + 1)] for _ in range(len(A) + 1)]
    for i in range(len(A) + 1):
        M[i][0] = gap * i
    for j in range(len(B) + 1):
        M[0][j] = gap * j

    for i in range(1, len(A) + 1):
        for j in range(1, len(B) + 1):
            cost = mch if A[i - 1] == B[j - 1] else mis
            match = M[i - 1][j - 1] + cost
            delete = M[i - 1][j] + gap
            insert = M[i][j - 1] + gap
            M[i][j] = max(match, insert, delete)

    alignment_a, alignment_b = "", ""
    i, j = len(A), len(B)
    while i > 0 or j > 0:
        cost = mch if A[i - 1] == B[j - 1] else mis
        if i > 0 and j > 0 and M[i][j] == M[i - 1][j - 1] + cost:
            alignment_a = A[i - 1] + alignment_a
            alignment_b = B[j - 1] + alignment_b
            i -= 1
            j -= 1
        elif i > 0 and M[i][j] == M[i - 1][j] + gap:
            alignment_a = A[i - 1] + alignment_a
            alignment_b = "_" + alignment_b
            i -= 1
        else:
            alignment_a = "_" + alignment_a
            alignment_b = B[j - 1] + alignment_b
            j -= 1

    print(alignment_a)
    print(alignment_b)


global_alignment("AGCT", "ACT")
