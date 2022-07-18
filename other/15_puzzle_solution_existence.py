def check_solution_existance(puzzle):
    inv = 0
    for i in range(16):
        if puzzle[i]:
            for j in range(i):
                if puzzle[j] > puzzle[i]:
                    inv += 1
        else:
            inv += 1 + i // 4
    print('Решение существует') if inv % 2 == 0 else print('Решения не существует')


check_solution_existance([12, 5, 8, 7, 4, 11, 2, 14, 13, 6, 1, 0, 10, 9, 15, 3])
check_solution_existance([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 14, 0])
check_solution_existance(list(range(16)))
