class Graph:
    def __init__(self, v_number):
        self.v = v_number
        self.edges = []

    def add_edge(self, v1, v2, weight):
        self.edges.append([v1, v2, weight])

    def bellman_ford(self, start_v):
        D = {v: float('inf') for v in range(self.v)}
        D[start_v] = 0
        while True:
            flag = False
            for u, v, w in self.edges:
                if D[u] != float('inf') and D[u] + w < D[v]:
                    D[v] = D[u] + w
                    flag = True
            if not flag:
                break
        for u, v, w in self.edges:
            if D[u] != float('inf') and D[u] + w < D[v]:
                print('В графе есть цикл отрицательного веса')
        return D


g = Graph(9)
g.add_edge(0, 1, 4)
g.add_edge(0, 6, 7)
g.add_edge(1, 6, 11)
g.add_edge(1, 7, 20)
g.add_edge(1, 2, 9)
g.add_edge(2, 3, 6)
g.add_edge(2, 4, 2)
g.add_edge(3, 4, 10)
g.add_edge(3, 5, 5)
g.add_edge(4, 5, 15)
g.add_edge(4, 7, 1)
g.add_edge(4, 8, 5)
g.add_edge(5, 8, 12)
g.add_edge(6, 7, 1)
g.add_edge(7, 8, 3)
print(g.bellman_ford(0))