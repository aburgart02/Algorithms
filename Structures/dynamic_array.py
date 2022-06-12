class DynamicArray:
    def __init__(self):
        self.size = 0
        self.a = 2
        self.b = 3
        self.capacity = 1
        self.buffer = [None]

    def append(self, e):
        if self.size == self.capacity:
            self.capacity = self.a * self.size
            tmp = [None] * self.capacity
            for i in range(len(self.buffer)):
                tmp[i] = self.buffer[i]
            self.buffer = tmp
        self.buffer[self.size] = e
        self.size += 1

    def get_element(self, i):
        if i >= self.size or i < 0:
            raise IndexError
        return self.buffer[i]

    def delete(self):
        self.buffer[self.size - 1] = None
        self.size -= 1
        if self.b * self.size < self.capacity:
            self.capacity = self.a * self.size
            self.buffer = self.buffer[:self.capacity]

    @property
    def length(self):
        return self.size

    @property
    def elements(self):
        return self.buffer[:self.size]


array = DynamicArray()
for i in range(10):
    array.append(i)
    print(array.buffer, array.elements, array.length, array.get_element(i))
[array.delete() for _ in range(5)]
print(array.buffer, array.elements, array.length, array.get_element(4))
array.append(5)
print(array.buffer, array.elements, array.length, array.get_element(5))