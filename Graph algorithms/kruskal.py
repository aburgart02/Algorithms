class Graph:
    def __init__(self, v_number):
        self.v = v_number
        self.graph = []

    def add_edge(self, v1, v2, w):
        self.graph.append([v1, v2, w])

    def get_parent(self, parent, v):
        if v == parent[v]:
            return v
        return self.get_parent(parent, parent[v])

    @staticmethod
    def union(parent, rank, v1, v2):
        if rank[v1] < rank[v2]:
            parent[v1] = v2
        elif rank[v1] > rank[v2]:
            parent[v2] = v1
        else:
            parent[v2] = v1
            rank[v1] += 1

    def kruskal(self):
        i, j = 0, 0
        result = []
        parent, rank = list(range(self.v)), [0] * self.v
        self.graph = sorted(self.graph, key=lambda k: k[2])
        while j < self.v - 1:
            v1, v2, w = self.graph[i]
            i += 1
            x = self.get_parent(parent, v1)
            y = self.get_parent(parent, v2)
            if x != y:
                j += 1
                result.append([v1, v2, w])
                self.union(parent, rank, x, y)
        [print(e) for e in result]


g = Graph(7)
g.add_edge(0, 1, 7)
g.add_edge(1, 2, 8)
g.add_edge(2, 4, 5)
g.add_edge(0, 3, 5)
g.add_edge(1, 3, 9)
g.add_edge(1, 4, 7)
g.add_edge(3, 4, 15)
g.add_edge(3, 5, 6)
g.add_edge(4, 5, 8)
g.add_edge(4, 6, 9)
g.add_edge(5, 6, 11)
g.kruskal()