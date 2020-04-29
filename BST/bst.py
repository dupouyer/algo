class Node:
    def __init__(self, v):
        self.value = v
        self.left = None
        self.right = None

    def setChild(self, isLeft, node):
        if isLeft:
            self.left = node
        else:
            self.right = node

class BST:
    def __init__(self, values):
        self.root = None
        for v in values:
            self.insert(v)
    
    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            self._insert(self.root, Node(value))

    def _insert(self, parent, node):
        if parent.value == node.value:
            return
        elif parent.value > node.value:
            if parent.left == None:
                parent.left = node
                return
            else:
                self._insert(parent.left, node)
                return
        elif parent.value < node.value:
            if parent.right == None:
                parent.right = node
                return
            else:
                self._insert(parent.right, node)
                return


    def remove(self, value):
        self._remove(self.root, value)

    def _remove(self,node, key, parent, isLeft):
        if node == None:
            return
        elif node.value < key:
            return self._remove(node.right, key, node, False)
        elif node.value > key:
            return self._remove(node.left, key, node, True)
        elif node.value == key:
            rmNode = node
            if node.left == None:
                parent.setChild(isLeft, node.right)
            elif parent.right == None:
                parent.setChild(isLeft, node.left)
            else:
                last = node
                minNode = node.right
                while minNode.left:
                    last = minNode
                    minNode = minNode.left
                
                parent.setChild(isLeft, minNode)
                last.setChild(True, None)

            return rmNode

    def search(self, value):
        return self._search(self.root, value)
    
    def _search(self, parent, value):
        if parent == None:
            return None, False
        elif parent.value == value:
            return parent,True
        elif parent.value < value:
            return self._search(parent.right, value)
        elif parent.value > value:
            return self._search(parent.left, value)

    def dump(self):
        self._dump(self.root)

    def _dump(self, parent):
        if parent == None:
            return

        self._dump(parent.left)
        print(parent.value)
        self._dump(parent.right)
