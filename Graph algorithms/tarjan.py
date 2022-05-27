from collections import defaultdict


class Graph:
    def __init__(self, v_number):
        self.v = v_number
        self.graph = defaultdict(list)
        self.time = 0

    def add_edge(self, v1, v2):
        self.graph[v1].append(v2)

    def tarjan(self):
        index = [-1] * self.v
        temp = [-1] * self.v
        stack_member = [False] * self.v
        stack = []
        for i in range(self.v):
            if index[i] == -1:
                self.get_scc(i, index, temp, stack_member, stack)

    def get_scc(self, v, index, temp, stack_member, stack):
        index[v] = self.time
        temp[v] = self.time
        self.time += 1
        stack_member[v] = True
        stack.append(v)
        for neighbour in self.graph[v]:
            if index[neighbour] == -1:
                self.get_scc(neighbour, index, temp, stack_member, stack)
                temp[v] = min(temp[v], temp[neighbour])
            elif stack_member[neighbour]:
                temp[v] = min(temp[v], index[neighbour])
        w = -1
        if temp[v] == index[v]:
            while w != v:
                w = stack.pop()
                stack_member[w] = False
                print(w, end=' ')
            print()


g4 = Graph(8)
g4.add_edge(0, 1)
g4.add_edge(1, 2)
g4.add_edge(2, 0)
g4.add_edge(3, 1)
g4.add_edge(3, 2)
g4.add_edge(3, 4)
g4.add_edge(4, 3)
g4.add_edge(4, 5)
g4.add_edge(5, 2)
g4.add_edge(5, 6)
g4.add_edge(6, 5)
g4.add_edge(7, 4)
g4.add_edge(7, 6)
g4.add_edge(7, 7)
g4.tarjan()