class Node(object):
    def __init__(self, value):
        self.info = value
        self.link = None

class CircularLinkedList(object):
    def __init__(self):
        self.last = None

    def create_list(self):
        n = int(input("Enter the number of nodes : "))
        if n == 0:
            return

        data = int(input('Enter first element to be inserted :'))
        self.insert_in_empty_list(data)

        for i in range(n):
            data = int(input("Enter the element to be inserted : "))
            self.insert_at_end(data)

    def insert_in_beginning(self, data):
        temp = Node(data)
        temp.link = self.last.link
        self.last.link = temp

    def insert_in_empty_list(self, data):
        temp = Node(data)
        self.last = temp
        self.last.link = self.last

    def insert_at_end(self, data):
        temp = Node(data)
        temp.link = self.last.link
        self.last.link = temp
        self.last = temp        

    def insert_after(self, data, x):
        p = self.last.link
        while True:
            if p.info == x:
                break
            p = p.link
            if p == self.last.link:
                break

        if p == self.last.link and p.info != x:
            return -1
        else:
            temp = Node(data)
            temp.link = p.link
            p.link = temp
            if p == self.last:
                self.last = temp
        
    def insert_before(self, data, x):
        if self.last is None:
            return -1

        if self.last.link.info == x:
            temp = Node(data)
            temp.link = self.last.link
            self.last.link = temp
            self.last = temp
            return

        p = self.last.link
        while True:
            if p.link.info == x:
                break
            p = p.link
            if p == self.last.link:
                break

        if p == self.last.link and p.info != x:
            return -1
        else:
            temp = Node(data)
            temp.link = p.link
            p.link = temp

    def display_list(self):
        if self.last is None:
            print('List in empty')
            return

        p = self.last.link
        while True:
            print(p.info, " ", end='')
            p = p.link
            if p == self.last.link:
                break
        print()    

    def count_nodes(self):
        p = self.last.link
        count = 0
        while True:
            count += 1
            p = p.link
            if p == self.last.link:
                break            
        return count

    def contains(self, x):
        p = self.last.link
        while True:
            if p.info == x:
                return True
            p = p.link
            if p == self.last.link:
                break
        else:
            return False

    def delete_node(self, x):
        if self.last is None:
            return -1

        if self.last == self.last.link:
            self.last = None
            return

        if self.last.link.info == x:
            self.last.link = self.last.link.link
            return

        p = self.last.link
        while p.link != self.last.link:
            if p.link.info == x:
                break
            p = p.link

        if p.link == self.last.link:
            return -1
        else:
            p.link = p.link.link
            if self.last.info == x:
                self.last = p


    def delete_first_node(self):
        if self.last is None:
            return -1
        if self.last.link == self.last:
            self.last = None
            return
        self.last.link = self.last.link.link

    def delete_last_node(self):
        if self.last is None:
            return -1

        if self.last == self.last.link:
            self.last = None
            return

        p = self.last.link
        while p.link != self.last:
            p = p.link
        p.link = self.last.link
        self.last = p

    def concatenate(self, list2):
        if self.last is None:
            self.last = list2.last
            return
        
        if list2.last is None:
            return

        p = self.last.link
        self.last.link = list2.last.link
        list2.last.link = p
        self.last = list2.last

print('Creating list :')
list = CircularLinkedList()

list.create_list()
list.display_list()

elem_status = list.contains(1)
print('Does list contains 1 : ', elem_status)

print('Inserting at beginning & end :')
list.insert_in_beginning(0)
list.insert_at_end(4)
list.display_list()

list_count = list.count_nodes()
print('Length of list is : ', list_count)

print('Inserting after, before, at_position :')
list.insert_after(5, 4)
list.insert_before(4.5, 5)
list.display_list()

print('Deleting first_node, last_node, node_with_value :')
list.delete_first_node()
list.delete_last_node()
list.delete_node(4.5)
list.display_list()

print('Concatenate list :')
list2 = CircularLinkedList()
list2.create_list()
list2.display_list()
list.concatenate(list2)
list.display_list()