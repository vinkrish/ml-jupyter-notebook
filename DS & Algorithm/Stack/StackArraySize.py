class EmptyStackError(Exception):
    pass

class StackFullError(Exception):
    pass

class Stack:

    def __init__(self, max_size = 10):
        self.items = [None] * max_size
        self.count = 0

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count == len(self.items)

    def size(self):
        return self.count

    def push(self, item):
        if self.is_full():
            raise StackFullError('Stack is full, can\'t push')
        self.items[self.count] = item
        self.count += 1

    def pop(self):
        if self.is_empty():
            raise EmptyStackError('Stack is empty, can\'t pop')
        x = self.items[self.count-1]
        self.items[self.count-1] = None
        self.count -+ 1
        return x

    def peek(self):
        if self.is_empty():
            raise EmptyStackError('Stack is empty, can\'t peek')
        return self.items[-1]

    def display(self):
        print(self.items)

stack = Stack()

print('Check if stack is empty :')
check_stack = stack.is_empty()
print(check_stack)

print('Pushing element to stack :')
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.push(6)
stack.push(7)
stack.push(8)
stack.push(9)
stack.push(10)
stack.display()

print('Is stack full :')
full = stack.is_full()
print(full)

print('Pop element from stack :')
pop = stack.pop()
print(pop)
stack.display()

print('Peek at stack :')
peek = stack.peek()
print(peek)
stack.display()

print('Size of stack :')
size = stack.size()
print(size)

print('Check if stack is empty :')
check_stack = stack.is_empty()
print(check_stack)