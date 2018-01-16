class Node():
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.parentNode = None
        self.balance_factor = 0 # diff in height of left and right subtrees

    def traverse_inorder(self):
        if self.leftChild:
            self.leftChild.traverse_inorder()

        print(self.data)

        if self.rightChild:
            self.rightChild.traverse_inorder()

    def insert(self, data):
        if data < self.data:
            if self.leftChild:
                return self.leftChild.insert(data)
            else:
                self.leftChild = Node(data)
                self.leftChild.parentNode = self
                return self

        else:
            if self.rightChild:
                return self.rightChild.insert(data)
            else:
                self.rightChild = Node(data)
                self.rightChild.parentNode = self
                return self



class AVL():
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
            return

        # This is the parent of the newly inserted leaf node.
        # Start rebalancing from the parent upwards till root.
        node_to_start_rebalance_from = self.root.insert(data)

        self.rebalance(node_to_start_rebalance_from)


    def traverse_inorder(self):
        if self.root:
            self.root.traverse_inorder()

    def rebalance(self, node):
        node.balance_factor = self.height(node.leftChild) - self.height(node.rightChild)

        if node.balance_factor > 1:
            # left heavy
            
            if self.height(node.leftChild.leftChild) >= self.height(node.leftChild.rightChild):
                # double left heavy - LL (single right rotation)
                self.rotateRight(node)
            else:
                # LR - left followed by right rotation
                self.rotateLeftRight(node)


        elif node.balance_factor < -1:
            # right heavy

            if self.height(node.rightChild.rightChild) >= self.height(node.rightChild.leftChild):
                # double right heavy - RR (single left rotation)
                self.rotateLeft(node)
            else:
                # RL - right followed by left rotation
                self.rotateRightLeft(node)


        if node.parentNode:
            self.rebalance(node.parentNode)
        else:
            # node.parentNode is None means "node" is the root
            # Rebalancing can change the root node.
            self.root = node


    def rotateLeftRight(self, node):
        print("Rotate left right at node " + str(node.data))
        self.rotateLeft(node.leftChild)
        self.rotateRight(node)


    def rotateRightLeft(self, node):
        print("Rotate right left at node " + str(node.data))
        self.rotateRight(node.rightChild)
        self.rotateLeft(node)


    def rotateLeft(self, node):
        print("Rotate left at node " + str(node.data))

        tmp = node.rightChild
        tmp_left = tmp.leftChild

        # Things that will change in 'tmp' node:
        # 1. Its left child
        # 2. Its parent
        tmp.leftChild = node
        tmp.parentNode = node.parentNode


        # Things that will change in 'node':
        # 1. Its right child ('tmp's left child will become 'node's right child)
        # 2. Its parent
        node.rightChild = tmp_left
        node.parentNode = tmp


        # Things that will change in 'tmp's left child:
        # 1. Its parent
        if tmp_left:
            tmp_left.parentNode = node

        # Things that will change in 'tmp's (new) parent:
        # 1. Either the left or right child pointer (which was earlier pointing to 'node')
        if tmp.parentNode:
            if tmp.parentNode.leftChild == node:
                tmp.parentNode.leftChild = tmp
            else:
                tmp.parentNode.rightChild = tmp


    def rotateRight(self, node):
        print("Rotate right at node " + str(node.data))

        tmp = node.leftChild
        tmp_right = tmp.rightChild

        # Things that will change in 'tmp' node:
        # 1. Its right child
        # 2. Its parent
        tmp.rightChild = node
        tmp.parentNode = node.parentNode


        # Things that will change in 'node':
        # 1. Its left child ('tmp's right child will become 'node's left child)
        # 2. Its parent
        node.leftChild = tmp_right
        node.parentNode = tmp


        # Things that will change in 'tmp's right child:
        # 1. Its parent
        if tmp_right:
            tmp_right.parentNode = node

        # Things that will change in 'tmp's (new) parent:
        # 1. Either the left or right child pointer (which was earlier pointing to 'node')
        if tmp.parentNode:
            if tmp.parentNode.leftChild == node:
                tmp.parentNode.leftChild = tmp
            else:
                tmp.parentNode.rightChild = tmp


    def height(self, node):
        if not node:
            return -1
        else:
            return 1 + max(self.height(node.leftChild), self.height(node.rightChild))










tree = AVL()
tree.insert(7)
tree.insert(8)
tree.insert(4)
tree.insert(5)
tree.insert(6)
tree.insert(6.5)
tree.traverse_inorder()
