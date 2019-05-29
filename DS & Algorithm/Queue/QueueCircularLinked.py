class EmptyQueueError(Exception):
    pass

class Node:

    def __init__(self, value):
        self.info = value
        self.link = None

class Queue:

    def __init__(self):
        self.rear = None

    def is_empty(self):
        return self.rear == None

    def size(self):
        if self.is_empty():
            return 0

        n = 0
        p = self.rear.link
        while True:
            n += 1
            p = p.link
            if p == self.rear.link:
                break
        return n

    def enqueue(self, item):
        temp = Node(item)

        if self.is_empty():
            self.rear = temp
            self.rear.link = self.rear
        else:
            temp.link = self.rear.link
            self.rear.link = temp
            self.rear = temp

    def dequeue(self):
        if self.is_empty():
            raise EmptyQueueError('Queue is empty')

        if self.rear.link == self.rear:
            temp = self.rear
            self.rear = None
        else:
            temp = self.rear.link
            self.rear.link = self.rear.link.link
        return temp.info

    def peek(self):
        if self.is_empty():
            raise EmptyQueueError('Queue is empty')

        return self.rear.link.info

    def display(self):
        p = self.rear.link
        while True:
            print(p.info, ' ', end=' ')            
            p = p.link
            if p == self.rear.link:
                break
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