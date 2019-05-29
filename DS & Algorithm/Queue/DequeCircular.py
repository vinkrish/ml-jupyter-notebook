class EmptyQueueError(Exception):
    pass

class Deque:

    def __init__(self, default_size = 10):
        self.items = [None] * default_size
        self.front = 0
        self.count = 0

    def is_empty(self):
        return self.count == 0

    def size(self):
        return self.count

    def insert_front(self, item):
        if self.count == len(self.items):
            self.resize(2*len(self.items))
        
        self.front = (self.front - 1) % len(self.items)
        self.items[self.front] = item
        self.count += 1

    def insert_rear(self, item):
        if self.count == len(self.items):
            self.resize(2*len(self.items))

        i = (self.front + self.count) % len(self.items)
        self.items[i] = item
        self.count += 1

    def delete_front(self):
        if self.is_empty():
            raise EmptyQueueError('Queue is empty')

        x = self.items[self.front]
        self.items[self.front] = None
        self.front = (self.front + 1) % len(self.items)
        self.count -= 1
        return x

    def delete_rear(self):
        if self.is_empty():
            raise EmptyQueueError('Queue is empty')

        rear = (self.front + self.count - 1) % len(self.items)
        x = self.items[rear]        
        self.items[rear] = None
        self.count -= 1
        return x

    def first(self):
        if self.is_empty():
            raise EmptyQueueError('Queue is empty')
        return self.items[self.front]
        
    def last(self):
        if self.is_empty():
            raise EmptyQueueError('Queue is empty')
        rear = (self.front + self.count - 1) % len(self.items)
        return self.items[rear]

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

queue = Deque()

print('enqueue :')
queue.insert_front(1)
queue.display()
queue.insert_rear(2)
queue.display()
queue.insert_front(3)
queue.display()

print('first and last :')
print(queue.first())
print(queue.last())
queue.display()

print('dequeue :')
pop = queue.delete_front()
print(pop)
pop = queue.delete_rear()
queue.display()

print('size :')
print(queue.size())

print('use all index :')
queue.insert_rear(4)
queue.insert_rear(5)
queue.insert_rear(6)
queue.insert_rear(7)
queue.insert_front(8)
queue.insert_front(9)
queue.insert_front(10)
queue.insert_front(11)
queue.insert_front(12)
queue.display()

print('adding one more causes resize :')
queue.insert_front(13)
queue.display()