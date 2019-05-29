class EmptyQueueError(Exception):
    pass

class Queue:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise EmptyQueueError('Queue is empty')
        return self.items.pop(0)

    def peek(self):
        if self.is_empty():
            raise EmptyQueueError('Queue is empty')
        return self.items[0]
        
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
