class EmptyStackError(Exception):
    pass

class Node:
    def __init__(self, value):
        self.info = value
        self.link = None

class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top == None

    def size(self):
        p = self.top
        count = 0
        while p is not None:
            count += 1
            p = p.link            
        return count
    
    def push(self, item):
        temp = Node(item)
        temp.link = self.top
        self.top = temp
    
    def pop(self):
        if self.is_empty():
            raise EmptyStackError('stack is empty, can\t pop')
        popped = self.top.info
        self.top = self.top.link
        return popped

    def peek(self):
        if self.is_empty():
            raise EmptyStackError('stack is empty, can\t peek')
        peeked = self.top.info
        return peeked

    def display(self):
        if self.is_empty():
            print('Stack in empty')
            return

        p = self.top
        while p is not None:
            print(p.info, " ", end='')
            p = p.link
        print()

stack = Stack()

print('Check if stack is empty :')
check_stack = stack.is_empty()
print(check_stack)

print('Size of stack :')
size = stack.size()
print(size)

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