class EmptyQueueError(Exception):
    pass

class Node:
    def __init__(self, value):
        self.info = value
        self.prev = None
        self.next = None

class Deque:

    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front == None

    def size(self):
        count = 0
        p = self.front
        while p is not None:
            count += 1
            p = p.next
        return count
    
    def insert_front(self, item):
        temp = Node(item)
        if self.is_empty():
            self.front = self.rear = temp
        else:
            temp.next = self.front
            self.front.prev = temp
            self.front = temp

    def insert_rear(self, item):
        temp = Node(item)
        if self.is_empty():
            self.front = self.rear = temp
        else:
            temp.prev = self.rear
            self.rear.next = temp
            self.rear = temp

    def display(self):
        if self.is_empty():
            raise EmptyQueueError('Queue is empty')
        else:
            p = self.front
            while p is not None:
                print(p.info, " ", end='')
                p = p.next
            print()

    def delete_front(self):
        if self.is_empty():
            raise EmptyQueueError('Queue is empty')

        x = self.front.info
        if self.front.next is None:
            self.front = self.rear = None
        else:
            self.front = self.front.next
            self.front.prev = None
        return x

    def delete_rear(self):
        if self.is_empty():
            raise EmptyQueueError('Queue is empty')

        x = self.rear.info
        if self.front.next is None:
            self.front = self.rear = None
        else:
            self.rear = self.rear.prev
            self.rear.next = None
        return x

    def first(self):
        if self.is_empty():
            raise EmptyQueueError('Queue is empty')
        return self.front.info

    def last(self):
        if self.is_empty():
            raise EmptyQueueError('Queue is empty')
        return self.rear.info

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
print('removed from front :', pop)
pop = queue.delete_rear()
print('removed from rear :', pop)

queue.display()

print('size :')
print(queue.size())

print('adding more :')
queue.insert_rear(4)
queue.insert_rear(5)
queue.insert_rear(6)
queue.insert_rear(7)
queue.insert_front(8)
queue.insert_front(9)
queue.insert_front(10)
queue.display()
