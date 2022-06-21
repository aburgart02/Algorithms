import random
import math


class Node:
    def __init__(self, key, value, next):
        self.key = key
        self.value = value
        self.next = next


class HashTable:
    def __init__(self):
        self.n = 0
        self.m = 1
        self.T = [-1] * self.m
        self.K = [None] * self.m
        self.w = 64
        self.a = random.randint(0, 2 ** self.w) | 1

    def f(self, k):
        return (k * self.a) % 2 ** self.w >> int(self.w - math.log2(self.m))

    def get(self, key):
        i = self.T[self.f(key)]
        while i != -1 and key != self.K[i].key:
            i = self.K[i].next
        if i == -1:
            return None
        return self.K[i].value

    def insert(self, key, value):
        if self.get(key):
            return
        if self.n >= self.m:
            self.recreate_table()
        cell = self.f(key)
        self.K[self.n] = Node(key, value, self.T[cell])
        self.T[cell] = self.n
        self.n += 1

    def recreate_table(self):
        self.n = 0
        self.m *= 2
        self.T = [-1] * self.m
        K = [None] * self.m
        for node in self.K:
            cell = self.f(node.key)
            K[self.n] = Node(node.key, node.value, self.T[cell])
            self.T[cell] = self.n
            self.n += 1
        self.K = K


ht = HashTable()
ht.insert(1, 'value_1')
ht.insert(11, 'value_11')
ht.insert(111, 'value_111')
ht.insert(2, 'value_2')
ht.insert(22, 'value_22')
ht.insert(3, 'value_3')
print(ht.get(1))
print(ht.get(11))
print(ht.get(111))
print(ht.get(2))
print(ht.get(22))
print(ht.get(3))