def local_alignment(A, B, mch=1, mis=-1, gap=-1):
    score = [[0 for _ in range(len(B) + 1)] for _ in range(len(A) + 1)]
    pointer = [[0 for _ in range(len(B) + 1)] for _ in range(len(A) + 1)]
    max_score, max_i, max_j = 0, 0, 0

    for i in range(1, len(A) + 1):
        for j in range(1, len(B) + 1):
            cost = mch if A[i - 1] == B[j - 1] else mis
            score_diagonal = score[i - 1][j - 1] + cost
            score_left = score[i][j - 1] + gap
            score_up = score[i - 1][j] + gap
            score[i][j] = max(0, score_up, score_left, score_diagonal)
            if score[i][j] == 0:
                pointer[i][j] = 0
            if score[i][j] == score_up:
                pointer[i][j] = 1
            if score[i][j] == score_left:
                pointer[i][j] = 2
            if score[i][j] == score_diagonal:
                pointer[i][j] = 3
            if score[i][j] >= max_score:
                max_i = i
                max_j = j
                max_score = score[i][j]

    alignment_a, alignment_b = "", ""
    i, j = max_i, max_j
    while pointer[i][j] != 0:
        if pointer[i][j] == 3:
            alignment_a += A[i - 1]
            alignment_b += B[j - 1]
            i -= 1
            j -= 1
        elif pointer[i][j] == 2:
            alignment_a += '_'
            alignment_b += B[j - 1]
            j -= 1
        elif pointer[i][j] == 1:
            alignment_a += A[i - 1]
            alignment_b += '_'
            i -= 1

    alignment_a = alignment_a[::-1]
    alignment_b = alignment_b[::-1]

    print(alignment_a)
    print(alignment_b)


local_alignment("TCCCCGGGAACCAACC", "AAACCCCCGGGGTA")
