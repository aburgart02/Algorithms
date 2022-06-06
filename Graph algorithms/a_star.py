from queue import PriorityQueue


class Grid:
    def __init__(self, w, h, m):
        self.weight = w
        self.height = h
        self.map = m
        self.grid = self.create_grid()

    def get_neighbours(self, i, j):
        return [(cell, self.map[cell[0]][cell[1]]) for cell in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]
                if 0 <= cell[0] < self.height and 0 <= cell[1] < self.weight]

    def create_grid(self):
        return {(i, j): self.get_neighbours(i, j) for i in range(self.height) for j in range(self.weight)}

    @staticmethod
    def heuristic(target_v, neighbour):
        return abs(target_v[0] - neighbour[0]) + abs(target_v[1] - neighbour[1])

    def a_star(self, start_v, target_v):
        D = {start_v: 0}
        P = {start_v: None}
        pq = PriorityQueue()
        pq.put((0, start_v))
        while not pq.empty():
            priority, v = pq.get()
            if v == target_v:
                break
            for neighbour, cost in self.grid[v]:
                new_cost = D[v] + cost
                if neighbour not in D or new_cost < D[neighbour]:
                    D[neighbour] = new_cost
                    P[neighbour] = v
                    priority = new_cost + self.heuristic(target_v, neighbour)
                    pq.put((priority, neighbour))
        path = []
        while target_v is not None:
            path.append(target_v)
            target_v = P[target_v]
        [print(v, end=' ') for v in reversed(path)]


grid = []
weight, height = map(int, input().split())
[grid.append(list(map(int, input().split()))) for _ in range(height)]
start = tuple(map(int, input().split()))
target = tuple(map(int, input().split()))
g = Grid(weight, height, grid)
g.a_star(start, target)