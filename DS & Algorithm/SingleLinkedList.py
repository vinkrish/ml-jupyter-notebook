class Node:
    def __init__(self, value):
        self.info = value
        self.link = None

class SingleLinkedList:
    def __init__(self):
        self.start = None

    def create_list(self):
        n = int(input("Enter the number of nodes : "))
        if n == 0:
            return
        for i in range(n):
            data = int(input("Enter the element to be inserted : "))
            self.insert_at_end(data)

    def insert_in_beginning(self, data):
        temp = Node(data)
        temp.link = self.start
        self.start = temp

    def insert_at_end(self, data):
        temp = Node(data)
        if self.start is None:
            self.start = temp
            return

        p = self.start
        while p.link is not None:
            p = p.link
        p.link = temp
    
    def insert_at_position(self, data, pos):
        if pos == 0:
            temp = Node(data)
            temp.link = self.start
            self.start = temp
            return

        p = self.start
        i = 0
        while i < pos-1 and p is not None:
            i += 1
            p = p.link

        if p is None:
            return -1
        else:
            temp = Node(data)
            temp.link = p.link
            p.link = temp
        

    def insert_after(self, data, x):
        p = self.start
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
        if self.start is None:
            return -1

        if self.start.info == x:
            temp = Node(data)
            temp.link = self.start
            self.start = temp
            return

        p = self.start
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
        if self.start is None:
            print('List in empty')
            return
        else:
            p = self.start
            while p is not None:
                print(p.info, " ", end='')
                p = p.link
            print()    

    def count_nodes(self):
        p = self.start
        count = 0
        while p is not None:
            count += 1
            p = p.link            
        return count

    def contains(self, x):
        p = self.start
        while p is not None:
            if p.info == x:
                return True
            p = p.link
        else:
            return False
    
    def index_of(self, x):
        p = self.start
        position = 0
        while p is not None:
            if p.info == x:
                return position
            position += 1
            p = p.link
        else:
            return -1

    def reverse_list(self):
        if self.start is None:
            return -1

        if self.start.link is None:
            return

        prev = None
        p = self.start
        while p is not None:
            next = p.link
            p.link = prev
            prev = p
            p = next
        self.start = prev

    def delete_node(self, x):
        if self.start is None:
            return -1

        if self.start.info == x:
            self.start = self.start.link
            return

        p = self.start
        while p.link is not None:
            if p.link.info == x:
                break
            p = p.link

        if p.link is None:
            return -1
        else:
            p.link = p.link.link


    def delete_first_node(self):
        if self.start is None:
            return -1  
        self.start = self.start.link

    def delete_last_node(self):
        if self.start is None:
            return -1

        if self.start.link is None:
            self.start = None
            return

        p = self.start
        while p.link.link is not None:
            p = p.link
        p.link = None

    def bubble_sort_exdata(self):
        end = None

        while self.start.link != end:
            p = self.start
            while p.link != end:
                q = p.link
                if q.info < p.info:
                    p.info, q.info = q.info, p.info
                p = p.link
            end = p

    def bubble_sort_exlinks(self):
        end = None

        while self.start.link != end:
            r = p = self.start
            while p.link != end:
                q = p.link
                if p.info > q.info:
                    p.link = q.link
                    q.link = p
                    if p!=self.start:
                        r.link = q
                    else:
                        self.start = q
                    p,q = q,p
                r = p
                p = p.link
            end = p

    def insert_cycle(self, x):
        if self.start is None:
            return
        p = self.start
        px = None
        prev = None

        while p is not None:
            if p.info == x:
                px = p
            prev = p
            p = p.link

        if px is not None:
            prev.link = px
    
    def has_cycle(self):
        if self.find_cycle() is None:
            return False
        else:
            return True

    def find_cycle(self):
        if self.start is None or self.start.link is None:
            return None
        
        slowR = self.start
        fastR = self.start

        while slowR is not None and fastR.link is not None:
            slowR = slowR.link
            fastR = fastR.link.link
            if slowR == fastR:
                return slowR
        return None

    def remove_cycle(self):
        c = self.find_cycle()
        if c is None:
            return

        p = c
        q = c
        len_cycle = 0
        while True:
            len_cycle += 1
            q = q.link
            if p == q:
                break

        p = self.start
        len_rem_cycle = 0
        while p!=q:
            len_rem_cycle += 1
            p = p.link
            q = q.link

        length_list = len_cycle + len_rem_cycle

        p = self.start
        for i in range(length_list - 1):
            p = p.link
        p.link = None
    
    # Merging by creating a new list
    def merge_newlist(self, list2):
        p1 = self.start
        p2 = list2.start

        if p1.info < p2.info:
            p = Node(p1.info)
            p1 = p1.link
        else:
            p = Node(p2.info)
            p2 = p2.link

        p_temp = p

        while p1 is not None and p2 is not None:
            if p1.info <= p2.info:
                p_temp.link = Node(p1.info)
                p1 = p1.link
            else:
                p_temp.link = Node(p2.info)
                p2 = p2.link
            p_temp = p_temp.link

        while p1 is not None:
            p_temp.link = Node(p1.info)
            p_temp = p_temp.link
            p1 = p1.link

        while p2 is not None:
            p_temp.link = Node(p2.info)
            p_temp = p_temp.link
            p2 = p2.link

        merged_list = SingleLinkedList()
        merged_list.start = p
        return merged_list
    
    # merging by rearranging links (using MergeSort Algorithm)
    def merge_rearrange(self, list2):
        merged_list = SingleLinkedList()
        merged_list.start = self._merge_rearrange(self.start, list2.start)
        return merged_list

    def _merge_rearrange(self, p1, p2):
        if p1.info < p2.info:
            p = p1
            p1 = p1.link
        else:
            p = p2
            p2 = p2.link
        
        p_temp = p
        
        while p1 is not None and p2 is not None:
            if p1.info <= p2.info:
                p_temp.link = p1
                p1 = p1.link
            else:
                p_temp.link = p2
                p2 = p2.link
            p_temp = p_temp.link

        if p1 is None:
            p_temp.link = p2
        else:
            p_temp.link = p1

        return p

    def merge_sort(self):
        self.start = self._merge_sort_rec(self.start)

    def _merge_sort_rec(self, list_start):
        if list_start is None or list_start.link is None:
            return list_start

        start1 = list_start
        start2 = self._divide_list(list_start)
        start1 = self._merge_sort_rec(start1)
        start2 = self._merge_sort_rec(start2)
        startM = self._merge_rearrange(start1, start2)
        return startM

    def _divide_list(self, p):
        q = p.link.link
        while q is not None and q.link is not None:
            p = p.link
            q = q.link.link
        start2 = p.link
        p.link = None
        return start2

print('Creating list :')
list = SingleLinkedList()

list.create_list()
list.display_list()

print('Check if list contains and get position :')
elem_status = list.contains(1)
elem_position = list.index_of(1)

print('Does list contains 1 : ', elem_status)
print('Position of 1 is :', elem_position)

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

print('Deleting first_node, last_node, node_with_value :')
list.delete_first_node()
list.delete_last_node()
list.delete_node(4.25)
list.display_list()

print('Reversing list :')
list.reverse_list()
list.display_list()

print('Sorting list by exchanging data :')
list.bubble_sort_exdata()
list.display_list()

print('Reversing list :')
list.reverse_list()
list.display_list()

print('Sorting list by exchanging link :')
list.bubble_sort_exlinks()
list.display_list()

list2 = SingleLinkedList()
list2.create_list()
list2.insert_in_beginning(1)
list2.insert_at_end(6)
list2.insert_after(3, 6)
list2.display_list()

print('Sorting 2nd list :')
list2.bubble_sort_exdata()
list2.display_list()

print('Merging list :')
merged_list = list.merge_newlist(list2)
merged_list.display_list()

print('Merge by rearranging :')
merged_list = list.merge_rearrange(list2)
merged_list.display_list()

merged_list.reverse_list()
merged_list.display_list()
print('MergeSort :')
merged_list.merge_sort()
merged_list.display_list()

print('Cyles in list :')
merged_list.insert_cycle(4)
print(merged_list.has_cycle())
merged_list.remove_cycle()
merged_list.display_list()