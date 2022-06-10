parent = [None] * 10000
rank = [-1] * 10000


def make_set(v):
    parent[v] = v
    rank[v] = 0


def find_set(v):
    if v == parent[v]:
        return v
    parent[v] = find_set(parent[v])
    return parent[v]


def union_sets(a, b):
    a = find_set(a)
    b = find_set(b)
    if a != b:
        if rank[a] < rank[b]:
            a, b = b, a
        parent[b] = a
        if rank[a] == rank[b]:
            rank[a] += 1


make_set(0)
make_set(1)
make_set(2)
make_set(3)
union_sets(0, 1)
union_sets(2, 3)
union_sets(1, 3)
print(find_set(3))