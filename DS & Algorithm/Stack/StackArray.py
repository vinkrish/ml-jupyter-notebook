class EmptyStackError(Exception):
    pass

class Stack:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise EmptyStackError('Stack is empty')
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise EmptyStackError('Stack is empty')
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
stack.display()

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