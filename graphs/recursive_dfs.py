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


def dfs(v, visited):
    if v not in visited:
        visited.append(v)
        for neighbour in graph[v]:
            dfs(neighbour, visited)
    return visited


print(dfs(1, []))
