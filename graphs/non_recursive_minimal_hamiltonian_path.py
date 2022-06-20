import sys
from collections import defaultdict


class Graph:
    def __init__(self, v_number):
        self.v = v_number
        self.graph = defaultdict(list)
        self.dp = [[[sys.maxsize, None] for _ in range(self.v)] for _ in range(1 << self.v)]

    def add_edge(self, v1, v2, w):
        self.graph[v1].append((v2, w))

    @staticmethod
    def get_bit(used, to):
        return used >> to & 1

    def minimal_hamiltonian_path(self):
        for v in range(self.v):
            self.dp[(1 << self.v) - 1][v][0] = 0
        for used in range((1 << self.v) - 2, -1, -1):
            for v in range(self.v):
                for to, c in self.graph[v]:
                    if self.get_bit(used, to) == 0:
                        if c + self.dp[used | (1 << to)][to][0] < self.dp[used][v][0]:
                            self.dp[used][v] = [c + self.dp[used | (1 << to)][to][0], to]
        length = sys.maxsize
        start_v = 0
        for v in range(self.v):
            if self.dp[1 << v][v][0] < length:
                length = self.dp[1 << v][v][0]
                start_v = v
        path = [start_v]
        used = 1 << start_v
        while used != (1 << self.v) - 1:
            start_v = self.dp[used][start_v][1]
            path.append(start_v)
            used |= 1 << start_v
        return path, length


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
