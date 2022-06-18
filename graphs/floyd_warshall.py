class Graph:
    def __init__(self, v_number):
        self.v = v_number
        self.distances = [[float('inf') for _ in range(v_number)] for _ in range(v_number)]

    def add_edge(self, v1, v2, w):
        self.distances[v1][v2] = w
        self.distances[v1][v1] = 0
        self.distances[v2][v2] = 0

    def floyd_warshall(self):
        for k in range(self.v):
            for i in range(self.v):
                for j in range(self.v):
                    if self.distances[i][j] > self.distances[i][k] + self.distances[k][j]:
                        self.distances[i][j] = self.distances[i][k] + self.distances[k][j]
        if [self.distances[i][i] for i in range(self.v) if self.distances[i][i] < 0]:
            print('В графе есть цикл отрицательного веса')
            return
        [print(d) for d in self.distances]


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
g.floyd_warshall()