from queue import Queue

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


def bfs(start_v):
    q = Queue()
    q.put(start_v)
    visited = []
    while not q.empty():
        v = q.get()
        if v not in visited:
            visited.append(v)
            [q.put(e) for e in graph[v]]
    return visited


print(bfs(1))
