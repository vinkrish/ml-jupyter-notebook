class EmptyQueueError(Exception):
    pass

class Queue:

    def __init__(self, default_size = 10):
        self.items = [None] * default_size
        self.front = 0
        self.count = 0

    def is_empty(self):
        return self.count == 0

    def size(self):
        return self.count

    def enqueue(self, item):
        if self.count == len(self.items):
            self.resize(2*len(self.items))

        i = (self.front + self.count) % len(self.items)
        self.items[i] = item
        self.count += 1

    def dequeue(self):
        if self.is_empty():
            raise EmptyQueueError('Queue is empty')

        x = self.items[self.front]
        self.items[self.front] = None
        self.front = (self.front + 1) % len(self.items)
        self.count -= 1
        return x

    def peek(self):
        if self.is_empty():
            raise EmptyQueueError('Queue is empty')

        return self.items[self.front]

    def resize(self, newsize):
        old_list = self.items
        self.items = [None] * newsize
        i = self.front
        for j in range(self.count):
            self.items[j] = old_list[i]
            i = (1+i) % len(old_list)
        self.front = 0

    def display(self):
        print(self.items)

queue = Queue()

print('enqueue :')
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

queue.display()

print('peek :')
print(queue.peek())
queue.display()

print('dequeue :')
pop = queue.dequeue()
print(pop)
queue.display()

print('size :')
print(queue.size())

print('use all index :')
queue.enqueue(4)
queue.enqueue(5)
queue.enqueue(6)
queue.enqueue(7)
queue.enqueue(8)
queue.enqueue(9)
queue.enqueue(10)
queue.enqueue(11)
queue.display()

print('adding one more causes resize :')
queue.enqueue(12)
queue.display()