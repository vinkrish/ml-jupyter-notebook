class EmptyQueueError(Exception):
    pass

class Node:
    
    def __init__(self, value):
        self.info = value
        self.link = None

class Queue:

    def __init__(self):
        self.front = None
        self.rear = None
        self.size_queue = 0

    def is_empty(self):
        return self.front == None

    def size(self):
        return self.size_queue

    def enqueue(self, item):
        temp = Node(item)
        if self.front == None:
            self.front = temp
        else:
            self.rear.link = temp
        self.rear = temp
        self.size_queue += 1

    def dequeue(self):
        if self.is_empty():
            raise EmptyQueueError('Queue is empty')
        x = self.front.info
        self.front = self.front.link
        self.size_queue -= 1
        return x

    def peek(self):
        if self.is_empty():
            raise EmptyQueueError('Queue is empty')
        return self.front.info

    def display(self):
        p = self.front
        while p is not None:
            print(p.info, ' ', end=' ')
            p = p.link
        print()

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