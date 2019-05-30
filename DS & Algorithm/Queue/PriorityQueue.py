class EmptyQueueError(Exception):
    pass

class Node:
    def __init__(self, value, pr):
        self.info = value
        self.priority = pr
        self.link = None

class PriorityQueue:

    def __init__(self):
        self.front = None
    
    def is_empty(self):
        return self.front == None

    def size(self):
        n = 0
        p = self.front
        while p is not None:
            n += 1
            p = p.link
        return n

    def enqueue(self, data, data_priority):
        temp = Node(data, data_priority)

        if self.is_empty() or data_priority < self.front.priority:
            temp.link = self.front
            self.front = temp
        else:
            p = self.front
            while p.link is not None and p.link.priority <= data_priority:
                p = p.link
            temp.link = p.link
            p.link = temp

    def dequeue(self):
        if self.is_empty():
            raise EmptyQueueError('Queue is empty')
        x = self.front.info
        self.front = self.front.link
        return x

    def display(self):
        if self.is_empty():
            raise EmptyQueueError('Queue is empty')
        else:
            p = self.front
            while p is not None:
                print(p.info, " ", end='')
                p = p.link
            print()
pq = PriorityQueue()

print('adding elements :')
pq.enqueue(9,1)
pq.enqueue(5,2)
pq.enqueue(3,3)
pq.enqueue(1,3)
pq.enqueue(0,0)

pq.display()

pop = pq.dequeue()
print('element that is popped : ', pop)
print('after popping one element from front of queue :')
pq.display()

print('size of queue :', pq.size())