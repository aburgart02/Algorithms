from collections import defaultdict


class Graph:
    def __init__(self, v_number):
        self.v = v_number
        self.graph = defaultdict(list)
        self.time = 0

    def add_edge(self, v1, v2):
        self.graph[v1].append(v2)
        self.graph[v2].append(v1)

    def dfs(self, u, index, temp, visited, parent, ap):
        children = 0
        index[u] = self.time
        temp[u] = self.time
        self.time += 1
        visited[u] = True
        for v in self.graph[u]:
            if not visited[v]:
                parent[v] = u
                children += 1
                self.dfs(v, index, temp, visited, parent, ap)
                temp[u] = min(temp[u], temp[v])
                if parent[u] == -1 and children > 1:
                    ap[u] = True
                if parent[u] != - 1 and index[u] <= temp[v]:
                    ap[u] = True
            elif v != parent[u]:
                temp[u] = min(temp[u], index[v])

    def search_articulation_points(self):
        index = [float('inf')] * self.v
        temp = [float('inf')] * self.v
        visited = [False] * self.v
        parent = [-1] * self.v
        ap = [False] * self.v
        for i in range(self.v):
            if not visited[i]:
                self.dfs(i, index, temp, visited, parent, ap)
        [print(i) for i, value in enumerate(ap) if value]


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
g.search_articulation_points()