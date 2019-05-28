class Node(object):
    def __init__(self, value):
        self.info = value
        self.link = None

class SortedLinkedList(object):

    def __init__(self):
        self.start = None

    def insert_in_order(self, data):
        temp = Node(data)

        if self.start == None or data < self.start.info:
            temp.link = self.start
            self.start = temp
            return

        p = self.start
        while p.link is not None and p.link.info <= data:
            p = p.link
        temp.link = p.link
        p.link = temp

    def create_list(self):
        n = int(input('Enter the number of nodes :'))
        if n == 0:
            return
        for i in range(n):
            data = int(input('Enter the elememt to be inserted :'))
            self.insert_in_order(data)

    def display_list(self):
        if self.start is None:
            print('List in empty')
            return
        else:
            p = self.start
            while p is not None:
                print(p.info, " ", end='')
                p = p.link
            print()

    def search(self, x):
        if self.start is None:
            return -1

        position = 0
        p = self.start
        while p is not None and p.info <= x:
            if p.info == x:
                break
            position += 1
            p = p.link
        
        if p is None and p.info != x:
            return -1
        else:
            return position

print('Creating List :')
list = SortedLinkedList()

list.create_list()
list.display_list()

print('Searching list :')
print(list.search(2))