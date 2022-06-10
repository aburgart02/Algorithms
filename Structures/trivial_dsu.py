parent = [None] * 1000


def make_set(v):
    parent[v] = v


def find_set(v):
    if v == parent[v]:
        return v
    return find_set(parent[v])


def union_sets(a, b):
    a = find_set(a)
    b = find_set(b)
    if a != b:
        parent[b] = a


make_set(5)
make_set(6)
make_set(7)
print(find_set(6))
union_sets(5, 6)
print(find_set(6))