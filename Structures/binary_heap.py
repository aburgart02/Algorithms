class BinaryHeap:
    def __init__(self):
        self.list = []

    def add(self, n):
        self.list.append(n)
        i = len(self.list) - 1
        parent = (i - 1) // 2
        while i > 0 and self.list[i] > self.list[parent]:
            self.list[i], self.list[parent] = self.list[parent], self.list[i]
            i = parent
            parent = (i - 1) // 2

    def heapify(self, n):
        while True:
            left_child = 2 * n + 1
            right_child = 2 * n + 2
            max_child = n
            if left_child < len(self.list) and self.list[left_child] > self.list[max_child]:
                max_child = left_child
            if right_child < len(self.list) and self.list[right_child] > self.list[max_child]:
                max_child = right_child
            if max_child == n:
                break
            self.list[n], self.list[max_child] = self.list[max_child], self.list[n]
            n = max_child

    def build_heap(self, array):
        self.list = array
        for i in range(len(self.list) // 2, -1, -1):
            self.heapify(i)

    def get_max(self):
        result = self.list[0]
        self.list[0] = self.list.pop()
        self.heapify(0)
        return result

    def heap_sort(self, array):
        result = []
        self.build_heap(array)
        for i in range(len(self.list) - 1):
            result.append(self.get_max())
        result.append(self.list[0])
        return list(reversed(result))


data = [12, 33, 2, 87, 216, 7, 5, 367]
b = BinaryHeap()
b.build_heap(data)
print(b.list)
print(b.heap_sort(data))
b = BinaryHeap()
b.add(1)
b.add(2)
b.add(4)
b.add(5)
b.add(6)
b.add(8)
b.add(9)
b.add(10)
b.add(11)
b.add(16)
print(b.list)
print(b.get_max())
print(b.list)
