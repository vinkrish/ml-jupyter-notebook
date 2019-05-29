class Node(object):
    def __init__(self, value):
        self.info = value
        self.prev = None
        self.next = None

class DoubleLinkedList(object):

    def __init__(self):
        self.start = None
    
    def insert_in_beginning(self, data):
        temp = Node(data)
        temp.next = self.start
        self.start.prev = temp
        self.start = temp

    def insert_in_empty_list(self, data):
        temp = Node(data)
        self.start = temp

    def insert_at_end(self, data):
        temp = Node(data)
        p = self.start
        while p.next is not None:
            p = p.next
        p.next = temp
        temp.prev = p

    def create_list(self):
        n = int(input('Enter the number of nodes :'))
        if n == 0:
            return
        data = int(input('Enter the first element to be inserted :'))
        self.insert_in_empty_list(data)

        for i in range(n-1):
            data = int(input('Enter the next element to be inserted :'))
            self.insert_at_end(data)

    def insert_after(self, data, x):
        p = self.start
        while p.next is not None:
            if p.info == x:
                break
            p = p.next

        if p is None:
            return -1
        else:
            temp = Node(data)
            temp.next = p.next
            temp.prev = p
            if p.next is not None:
                p.next.prev = temp
            p.next = temp

    def insert_before(self, data, x):
        if self.start is None:
            return -1

        if self.start.info == x:
            temp = Node(data)
            temp.next = self.start
            self.start.prev = temp
            self.start = temp
            return

        p = self.start
        while p.next is not None:
            if p.info == x:
                break
            p = p.next

        if p is None:
            return -1
        else:
            temp = Node(data)
            temp.next = p
            temp.prev = p.prev
            p.prev.next = temp
            p.prev = temp

    def display_list(self):
        if self.start is None:
            print('List in empty')
            return
        else:
            p = self.start
            while p is not None:
                print(p.info, " ", end='')
                p = p.next
            print()

    def delete_first_node(self):
        if self.start is None:
            return

        if self.start.next is None:
            self.start = None
            return

        self.start = self.start.next
        self.start.prev = None
    
    def delete_last_node(self):
        if self.start is None:
            return

        if self.start.next is None:
            self.start = None
            return

        p = self.start
        while p.next != None:
            p = p.next
        p.prev.next = None
    
    def delete_node(self, x):
        if self.start is None:
            return

        if self.start.next is None:
            if self.start.info == x:
                self.start = None
            else:
                return -1
            return

        if self.start.info == x:
            self.start = self.start.next
            self.start.prev = None
            return

        p = self.start.next
        while p.next is not None:
            if p.info == x:
                break
            p = p.next

        if p.next is not None:
            p.prev.next = p.next
            p.next.prev = p.prev
        else:
            if p.info == x:
                p.prev.next = None
            else:
                return -1

    def reverse_list(self):
        if self.start is None:
            return -1

        p1 = self.start
        p2 = p1.next
        p1.next = None
        p1.prev = p2
        while p2 is not None:
            p2.prev = p2.next
            p2.next = p1
            p1 = p2
            p2 = p2.prev
        self.start = p1

print('Creating Double Linked List :')
d_list = DoubleLinkedList()
d_list.create_list()
d_list.display_list()

print('Inserting at beginning, before and after :')
d_list.insert_in_beginning(0)
d_list.insert_before(2.5, 3)
d_list.insert_after(4.5, 4)
d_list.display_list()

print('Deleting at beginning, end and node :')
d_list.delete_first_node()
d_list.delete_last_node()
d_list.delete_node(4.5)
d_list.display_list()

print('Reversing list :')
d_list.reverse_list()
d_list.display_list()