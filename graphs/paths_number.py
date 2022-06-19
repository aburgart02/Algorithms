graph = {
    0: [1],
    1: [2, 3, 6],
    2: [],
    3: [4, 5],
    4: [6],
    5: [6],
    6: []
}


def count_paths(start_v, target_v):
    dp = [0] * len(graph.keys())
    dp[target_v] = 1
    for v in range(target_v - 1, -1, -1):
        for next in graph[v]:
            dp[v] += dp[next]
    return dp[start_v]


print(count_paths(0, 6))
