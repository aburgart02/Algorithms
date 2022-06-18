from collections import defaultdict


class Graph:
    def __init__(self, v_number):
        self.v = v_number
        self.graph = defaultdict(list)

    def add_edge(self, v1, v2):
        self.graph[v1].append(v2)

    def topological_sort(self, v, visited, stack):
        visited[v] = True
        for neighbour in self.graph[v]:
            if not visited[neighbour]:
                self.topological_sort(neighbour, visited, stack)
        stack.insert(0, v)

    def kahn(self):
        visited = [False] * self.v
        stack = []
        for i in range(self.v):
            if not visited[i]:
                self.topological_sort(i, visited, stack)
        print(stack)


g = Graph(6)
g.add_edge(5, 2)
g.add_edge(5, 0)
g.add_edge(4, 0)
g.add_edge(4, 1)
g.add_edge(2, 3)
g.add_edge(3, 1)
g.kahn()