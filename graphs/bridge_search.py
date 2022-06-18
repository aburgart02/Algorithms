from collections import defaultdict


class Graph:
    def __init__(self, v_number):
        self.v = v_number
        self.graph = defaultdict(list)
        self.time = 0

    def add_edge(self, v1, v2):
        self.graph[v1].append(v2)
        self.graph[v2].append(v1)

    def dfs(self, u, temp, index, visited, parent):
        temp[u] = self.time
        index[u] = self.time
        visited[u] = True
        self.time += 1
        for v in self.graph[u]:
            if not visited[v]:
                parent[v] = u
                self.dfs(v, temp, index, visited, parent)
                temp[u] = min(temp[u], temp[v])
                if index[u] < temp[v]:
                    print(u, v)
            elif v != parent[u]:
                temp[u] = min(temp[u], index[v])

    def search_bridges(self):
        index = [float('inf')] * self.v
        temp = [float('inf')] * self.v
        visited = [False] * self.v
        parent = [-1] * self.v
        for i in range(self.v):
            if not visited[i]:
                self.dfs(i, temp, index, visited, parent)


g = Graph(9)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(0, 3)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(4, 5)
g.add_edge(4, 8)
g.add_edge(5, 8)
g.add_edge(6, 7)
g.search_bridges()