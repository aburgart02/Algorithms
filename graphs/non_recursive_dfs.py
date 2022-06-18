graph = {
    1: [2, 7, 8],
    2: [1, 3, 6],
    3: [2, 4, 5],
    4: [3],
    5: [3],
    6: [2],
    7: [1],
    8: [1, 9, 12],
    9: [8, 10, 11],
    10: [9],
    11: [9],
    12: [8]
}


def dfs(start_v):
    stack = [start_v]
    visited = []
    while stack:
        v = stack.pop()
        if v not in visited:
            visited.append(v)
            stack.extend(graph[v])
    return visited


print(dfs(1))
