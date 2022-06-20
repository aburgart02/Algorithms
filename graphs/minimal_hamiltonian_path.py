import sys
from collections import defaultdict


class Graph:
    def __init__(self, v_number):
        self.v = v_number
        self.graph = defaultdict(list)
        self.used = [False] * self.v

    def add_edge(self, v1, v2, w):
        self.graph[v1].append([v2, w])

    def get_min_path(self, v):
        cnt = 0
        for x in self.used:
            if x == False:
                cnt += 1
        if cnt == 0:
            return 0
        ans = sys.maxsize
        for pair in self.graph[v]:
            to, c = pair[0], pair[1]
            if not self.used[to]:
                self.used[to] = True
                ans = min(ans, c + self.get_min_path(to))
                self.used[to] = False
        return ans

    def minimal_hamiltonian_path(self):
        ans = sys.maxsize
        for v in range(self.v):
            self.used[v] = True
            ans = min(ans, self.get_min_path(v))
            self.used[v] = False
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
