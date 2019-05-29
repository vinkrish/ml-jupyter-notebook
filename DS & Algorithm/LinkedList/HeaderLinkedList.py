class Node:
    def __init__(self, value):
        self.info = value
        self.link = None

class HeaderLinkedList:
    def __init__(self):
        self.head = Node(0)

    def create_list(self):
        n = int(input("Enter the number of nodes : "))
        for i in range(n):
            data = int(input("Enter the element to be inserted : "))
            self.insert_at_end(data)

    def insert_in_beginning(self, data):
        temp = Node(data)
        temp.link = self.head.link
        self.head.link = temp

    def insert_at_end(self, data):
        temp = Node(data)

        p = self.head
        while p.link is not None:
            p = p.link
        p.link = temp
    
    def insert_at_position(self, data, pos):
        p = self.head
        i = 1
        while i < pos and p is not None:
            i += 1
            p = p.link

        if p is None:
            return -1
        else:
            temp = Node(data)
            temp.link = p.link
            p.link = temp
        

    def insert_after(self, data, x):
        p = self.head
        while p is not None:
            if p.info == x:
                break
            p = p.link

        if p is None:
            return -1
        else:
            temp = Node(data)
            temp.link = p.link
            p.link = temp
        

    def insert_before(self, data, x):
        p = self.head
        while p.link is not None:
            if p.link.info == x:
                break
            p = p.link

        if p.link is None:
            return -1
        else:
            temp = Node(data)
            temp.link = p.link
            p.link = temp

    def display_list(self):
        if self.head.link is None:
            print('List in empty')
            return
        else:
            p = self.head.link
            while p is not None:
                print(p.info, " ", end='')
                p = p.link
            print()    

    def count_nodes(self):
        p = self.head.link
        count = 0
        while p is not None:
            count += 1
            p = p.link            
        return count

    def contains(self, x):
        p = self.head.link
        while p is not None:
            if p.info == x:
                return True
            p = p.link
        else:
            return False

    def reverse_list(self):
        prev = None
        p = self.head.link
        while p is not None:
            next = p.link
            p.link = prev
            prev = p
            p = next
        self.head.link = prev

    def delete_node(self, x):
        p = self.head
        while p.link is not None:
            if p.link.info == x:
                break
            p = p.link

        if p.link is None:
            return -1
        else:
            p.link = p.link.link

    def delete_last_node(self):
        p = self.head
        while p.link.link is not None:
            p = p.link
        p.link = None

print('Creating list :')
list = HeaderLinkedList()

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
list.insert_at_position(4.25, 5)
list.display_list()

print('Reversing list :')
list.reverse_list()
list.display_list()

print('Deleting last_node, node_with_value :')
list.delete_last_node()
list.delete_node(4.25)
list.display_list()