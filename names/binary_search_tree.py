class BinarySearchTree:
    def __init__(self):
        self.root_node = None

    def emptyNode(self):
        return self.root_node is None

    def insert(self, value):
        if self.emptyNode():
            self.root_node = BSTNode(value)
        else:
            self.root_node.insert(value)

    def contains(self, target):
        if self.emptyNode():
            return False
        else:
            return self.root_node.contains(target)
    
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        elif value >= self.value:
            if not self.right:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    def contains(self, target):
        if target == self.value:
            return True
        elif target < self.value:
            return self.left.contains(target) if self.left else False
        else:
            return self.right.contains(target) if self.right else False

