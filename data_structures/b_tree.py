class BTreeNode:
    def __init__(self, leaf=False):
        self.leaf = leaf
        self.keys = []
        self.child = []


class BTree:
    def __init__(self, t):
        self.t = t
        self.root = BTreeNode(True)

    def insert(self, n):
        node = self.root
        if len(node.keys) == 2 * self.t - 1:
            temp = BTreeNode()
            self.root = temp
            temp.child.insert(0, node)
            self.split_child(temp, 0)
            self.insert_non_full(temp, n)
        else:
            self.insert_non_full(node, n)

    def insert_non_full(self, node, n):
        k = len(node.keys) - 1
        if node.leaf:
            node.keys.append((None, None))
            while k >= 0 and n[0] < node.keys[k][0]:
                node.keys[k + 1] = node.keys[k]
                k -= 1
            node.keys[k + 1] = n
        else:
            while k >= 0 and n[0] < node.keys[k][0]:
                k -= 1
            k += 1
            if len(node.child[k].keys) == 2 * self.t - 1:
                self.split_child(node, k)
                if n[0] > node.keys[k][0]:
                    k += 1
            self.insert_non_full(node.child[k], n)

    def split_child(self, node, k):
        y = node.child[k]
        z = BTreeNode(y.leaf)
        node.child.insert(k + 1, z)
        node.keys.insert(k, y.keys[self.t - 1])
        z.keys = y.keys[self.t:2 * self.t - 1]
        y.keys = y.keys[:self.t - 1]
        if not y.leaf:
            z.child = y.child[self.t:2 * self.t]
            y.child = y.child[:self.t - 1]

    def search_key(self, key, node=None):
        if node:
            k = 0
            while k < len(node.keys) and key > node.keys[k][0]:
                k += 1
            if k < len(node.keys) and key == node.keys[k][0]:
                return node.keys[k]
            elif node.leaf:
                return None
            else:
                return self.search_key(key, node.child[k])
        else:
            return self.search_key(key, self.root)

    def print_tree(self, node, level=0):
        print(level, end=' ')
        [print(x, end=' ') for x in node.keys]
        print()
        level += 1
        if len(node.child) > 0:
            [self.print_tree(x, level) for x in node.child]


B = BTree(3)
for i in range(10):
    B.insert((i, 0))
B.print_tree(B.root)
print(B.search_key(8))