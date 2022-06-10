class DynamicArray:
    def __init__(self):
        self.size = 0
        self.capacity = 1
        self.buffer = [None]

    def append(self, e):
        if self.size == self.capacity:
            self.capacity = 2 * self.size
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
array.delete()
print(array.buffer, array.elements, array.length, array.get_element(8))
array.append(9)
print(array.buffer, array.elements, array.length, array.get_element(9))