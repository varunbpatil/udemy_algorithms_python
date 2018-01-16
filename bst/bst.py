class Node():
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

    def traverse_inorder(self):
        if self.leftChild:
            self.leftChild.traverse_inorder()

        print(self.data)

        if self.rightChild:
            self.rightChild.traverse_inorder()

    def insert(self, data):
        if data < self.data:
            if not self.leftChild:
                self.leftChild = Node(data)
            else:
                self.leftChild.insert(data)

        else:
            if not self.rightChild:
                self.rightChild = Node(data)
            else:
                self.rightChild.insert(data)

    def delete(self, data, parentNode):
        if self.data == data:
            if self.leftChild and self.rightChild:
                self.data = self.rightChild.getMin()
                self.rightChild.delete(self.data, self)

            elif self == parentNode.leftChild:
                tmp = self.leftChild if self.leftChild else self.rightChild
                parentNode.leftChild = tmp

            else:
                tmp = self.leftChild if self.leftChild else self.rightChild
                parentNode.rightChild = tmp

        elif data < self.data:
            if self.leftChild:
                self.leftChild.delete(data, self)
        else:
            if self.rightChild:
                self.rightChild.delete(data, self)

    def getMin(self):
        if self.leftChild:
            return self.leftChild.getMin()
        else:
            return self.data




class BST():
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
            return

        self.root.insert(data)


    def delete(self, data):
        if self.root:
            if self.root.data == data:
                tempNode = Node(None)
                tempNode.leftChild = self.root
                self.root.delete(data, tempNode)
                self.root = tempNode.leftChild
            else:
                self.root.delete(data, None)


    def traverse_inorder(self):
        if self.root:
            self.root.traverse_inorder()
