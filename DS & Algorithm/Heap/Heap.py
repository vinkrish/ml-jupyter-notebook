class EmptyHeapError(Exception):
    pass

class Heap:

    def __init__(self, maxsize = 10):
        self.a = [None]*maxsize
        self.n = 0
        self.a[0]= 99999

    def insert(self, value):
        self.n += 1
        self.a[self.n] = value
        self.restore_up(self.n)

    def restore_up(self, i):
        k = self.a[i]
        iparent = i // 2

        while self.a[iparent] < k:
            self.a[i] = self.a[iparent]
            i = iparent
            iparent = i // 2
        self.a[i] = k

    def delete_root(self):
        if self.n == 0:
            raise EmptyHeapError('Heap is empty')
        
        maxValue = self.a[1]
        self.a[1] = self.a[self.n]
        self.n -= 1
        self.restore_down(1)
        return maxValue

    def restore_down(self, i):
        k = self.a[i]
        lchild = 2*1
        rchild = lchild + 1

        while rchild <= self.n:
            if k >= self.a[lchild] and k >= self.a[rchild]:
                self.a[i] = k
                return
            else:
                if self.a[lchild] > self.a[rchild]:
                    self.a[i] = self.a[lchild]
                    i = lchild
                else:
                    self.a[i] = self.a[rchild]
                    i = rchild

            lchild = 2 * i
            rchild = lchild + i

        # if number of nodes is even
        if lchild == self.n and k < self.a[lchild]:
            self.a[i] = self.a[lchild]
            i = lchild
        self.a[i] = k

    def display(self):
        if self.n == 0:
            raise EmptyHeapError('Heap is empty')
        for i in range(1, self.n+1):
            print(self.a[i], " ", end=' ')
        print()

heap = Heap(20)

heap.insert(70)
heap.insert(60)
heap.insert(42)
heap.insert(56)
heap.insert(30)
heap.insert(25)

heap.display()

print('Deleting root :')
heap.delete_root()
heap.display()

print('Inserting :')
heap.insert(45)
heap.display()