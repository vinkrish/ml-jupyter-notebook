class EmptyQueueError(Exception):
    pass

class Queue:

    def __init__(self):
        self.items = []
        self.front = 0

    def is_empty(self):
        return self.front == len(self.items)

    def size(self):
        return len(self.items) - self.front

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise EmptyQueueError('Queue is empty')
        x = self.items[self.front]
        self.items[self.front] = None
        self.front += 1
        return x

    def peek(self):
        if self.is_empty():
            raise EmptyQueueError('Queue is empty')
        return self.items[self.front]
        
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
