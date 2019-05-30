class TreeEmptyError(Exception):
    pass

class Node:
    def __init__(self, value):
        self.info = value
        self.lchild = None
        self.rchild = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root == None
    
    def insert(self, x):
        self.root = self._insert(self.root, x)

    def _insert(self, p, x):
        if p is None:
            p = Node(x)
        elif x < p.info:
            p.lchild = self._insert(p.lchild, x)
        elif x > p.info:
            p.rchild = self._insert(p.rchild, x)
        else:
            print(x, ' already present in the tree')
        return p

    def insert_iteratively(self, x):
        p = self.root
        par = None
        while p is not None:
            par = p
            if x < p.info:
                p = p.lchild
            elif x > p.info:
                p = p.rchild
            else:
                print(x, ' already present in the tree')
        
        temp = Node(x)

        if par is None:
            self.root = temp
        elif x < par.info:
            self.lchild = temp
        else:
            self.rchild = temp

    def search(self, x):
        return self._search(self.root, x) is not None
    
    def _search(self, p, x):
        if p is None:
            return None
        if x < p.info:
            return self._search(p.lchild, x)
        if x > p.info:
            return self._search(p.rchild, x)
        return p

    def search_iteratively(self, x):
        p = self.root
        while p is not None:
            if x < p.info:
                p = p.lchild
            elif x > p.info:
                p = p.rchild
            else:
                return True
        return False

    def delete(self, x):
        self._delete(self.root, x)

    def _delete(self, p, x):
        if p is None:
            return -1

        if x < p.info:
            p.lchild = self._delete(p.lchild, x)
        elif x > p.info:
            p.rchild = self._delete(p.rchild, x)
        else:
            # found key to be deleted
            if p.lchild is not None and p.rchild is not None:
                s = p.rchild
                while s.lchild is not None:
                    s = s.lchild
                p.info = s.info
                p.rchild = self._delete(p.rchild, s.info)
            else:
                if p.lchild is not None:
                    ch = p.lchild
                else:
                    ch = p.rchild
                p = ch
        return p

    def delete_iteratively(self, x):
        p = self.root
        par = None

        while p is not None:
            if x == p.info:
                break
            par = p
            if x < p.info:
                p = p.lchild
            else:
                p = p.rchild
            
        if p == None:
            return

        # case 3: two children
        # Find inorder successor and its parent
        if p.lchild is not None and p.rchild is not None:
            ps = p
            s = p.rchild

            while s.lchild is not None:
                ps = s
                s = s.lchild
            p.info = s.info
            p = s
            par = ps

        # case 2 and 1: one or no child
        if p.lchild is not None:
            ch = p.lchild
        else:
            ch = p.rchild

        if par == None:
            self.root = ch
        elif p == par.lchild:
            par.lchild = ch
        else:
            par.rchild = ch

    def min(self):
        if self.is_empty():
            raise TreeEmptyError('Tree is empty')
        return self._min(self.root).info

    def _min(self, p):
        if p.lchild is None:
            return p
        return self._min(p.lchild)
    
    def min_iteratively(self):
        if self.is_empty():
            raise TreeEmptyError('Tee is empty')
        p = self.root
        while p.lchild is not None:
            p = p.lchild
        return p.info
    
    def max(self):
        if self.is_empty():
            raise TreeEmptyError('Tree is empty')
        return self._max(self.root).info

    def _max(self, p):
        if p.rchild is None:
            return p
        return self._max(p.rchild)

    def max_iteratively(self):
        if self.is_empty():
            raise TreeEmptyError('Tee is empty')
        p = self.root
        while p.rchild is not None:
            p = p.rchild
        return p.info

    def display(self):
        self._display(self.root, 0)
        print()
    
    def _display(self,p,level):
        if p is None:
            return
        self._display(p.rchild, level+1)
        print()

        for i in range(level):
            print('   ', end='')
        print(p.info)
        self._display(p.lchild, level+1)

    def preorder(self):
        self._preorder(self.root)
        print()

    def _preorder(self, p):
        if p is None:
            return
        print(p.info, ' ', end='')
        self._preorder(p.lchild)
        self._preorder(p.rchild)

    def inorder(self):
        self._inorder(self.root)
        print()

    def _inorder(self, p):
        if p is None:
            return
        self._inorder(p.lchild)
        print(p.info, ' ', end='')
        self._inorder(p.rchild)

    def postorder(self):
        self._postorder(self.root)
        print()

    def _postorder(self, p):
        if p is None:
            return
        self._postorder(p.lchild)
        self._postorder(p.rchild)
        print(p.info, ' ', end='')

    def height(self):
        return self._height(self.root)
        
    def _height(self, p):
        if p is None:
            return 0

        hL = self._height(p.lchild)
        hR = self._height(p.rchild)

        if hL > hR:
            return hL + 1
        else:
            return hR + 1

bst = BinarySearchTree()
bst.root = Node(25)
bst.root.lchild = Node(15)
bst.root.rchild = Node(50)
bst.root.lchild.lchild = Node(10)
bst.root.lchild.rchild = Node(22)
bst.root.rchild.lchild = Node(35)
bst.root.rchild.rchild = Node(70)
bst.insert(4)
bst.insert(12)
bst.insert(18)
bst.insert(22)
bst.insert(24)
bst.insert(31)
bst.insert(44)
bst.insert(66)
bst.insert(90)

bst.display()

print('after deletion :')

bst.delete(15)
bst.display()