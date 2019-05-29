class EmptyQueueError(Exception):
    pass

class Deque:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def insert_front(self, item):
        self.items.insert(0, item)

    def insert_rear(self, item):
        self.items.append(item)

    def delete_front(self):
        if self.is_empty():
            raise EmptyQueueError('Queue is empty')
        return self.items.pop(0)

    def delete_rear(self):
        if self.is_empty():
            raise EmptyQueueError('Queue is empty')
        return self.items.pop()

    def first(self):
        if self.is_empty():
            raise EmptyQueueError('Queue is empty')
        return self.items[0]

    def last(self):
        if self.is_empty():
            raise EmptyQueueError('Queue is empty')
        return self.items[-1]

    def display(self):
        print(self.items)

deque = Deque()

deque.insert_front(1)
deque.insert_rear(2)
deque.insert_rear(3)

print('first item :')
first = deque.first()
print(first)

print('last item :')
last = deque.last()
print(last)

print('deleting front :')
deque.delete_front()
deque.display()

print('deleting rear :')
deque.delete_rear()
deque.display()

print('size :')
size = deque.size()
print(size)

print('Is empty :')
is_empty = deque.is_empty()
print(is_empty)