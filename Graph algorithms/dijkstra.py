from queue import PriorityQueue


class Graph:
    def __init__(self, v_number):
        self.v = v_number
        self.edges = [[-1 for _ in range(v_number)] for _ in range(v_number)]
        self.visited = []

    def add_edge(self, v1, v2, weight):
        self.edges[v1][v2] = weight
        self.edges[v2][v1] = weight

    def dijkstra(self, start_v, target_v):
        D = {v: float('inf') for v in range(self.v)}
        P = {p: -1 for p in range(self.v)}
        D[start_v] = 0
        pq = PriorityQueue()
        pq.put((0, start_v))
        while not pq.empty():
            distance, v = pq.get()
            self.visited.append(v)
            for neighbour in range(self.v):
                if self.edges[v][neighbour] != -1 and neighbour not in self.visited:
                    old_cost = D[neighbour]
                    new_cost = D[v] + self.edges[v][neighbour]
                    if new_cost < old_cost:
                        D[neighbour] = new_cost
                        P[neighbour] = v
                        pq.put((new_cost, neighbour))
        if D[target_v] == float('inf'):
            print(f'Нет пути от вершины {start_v} до вершины {target_v}')
        else:
            path = []
            while target_v != -1:
                path.append(target_v)
                target_v = P[target_v]
            [print(v, end=' ') for v in reversed(path)]
        print(D)


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
g.dijkstra(0, 8)