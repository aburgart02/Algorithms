graph = {
    0: [1],
    1: [2, 3, 6],
    2: [],
    3: [4, 5],
    4: [6],
    5: [6],
    6: []
}
memory = [-1] * len(graph.keys())


def count_paths(start_v, target_v):
    if memory[start_v] != -1:
        return memory[start_v]
    if start_v == target_v:
        return 1
    result = 0
    for v in graph[start_v]:
        result += count_paths(v, target_v)
    memory[start_v] = result
    return result


print(count_paths(0, 6))
