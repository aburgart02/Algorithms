import sys
from collections import defaultdict


class Graph:
    def __init__(self, v_number):
        self.v = v_number
        self.graph = defaultdict(list)
        self.dp = [[None for _ in range(self.v)] for _ in range(1 << self.v)]

    def add_edge(self, v1, v2, w):
        self.graph[v1].append([v2, w])

    @staticmethod
    def get_bit(used, to):
        return used >> to & 1

    def get_min_path(self, v, used):
        if used == (1 << self.v) - 1:
            return 0
        if self.dp[used][v] is None:
            ans = sys.maxsize
            for pair in self.graph[v]:
                to, c = pair[0], pair[1]
                if self.get_bit(used, to) == 0:
                    ans = min(ans, c + self.get_min_path(to, used | 1 << to))
                self.dp[used][v] = ans
        return self.dp[used][v]

    def minimal_hamiltonian_path(self):
        ans = sys.maxsize
        for v in range(self.v):
            ans = min(ans, self.get_min_path(v, 1 << v))
        return ans


g = Graph(7)
g.add_edge(0, 1, 9)
g.add_edge(0, 4, 8)
g.add_edge(1, 2, 2)
g.add_edge(1, 3, 9)
g.add_edge(1, 6, 9)
g.add_edge(2, 4, 2)
g.add_edge(3, 5, 11)
g.add_edge(4, 6, 1)
g.add_edge(5, 6, 8)
g.add_edge(6, 2, 1)
print(g.minimal_hamiltonian_path())
