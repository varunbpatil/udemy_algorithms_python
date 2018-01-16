# Splay tree implementation.
#
# Every time we go searching for an element, we make that element come up to the root (caching, garbage collection).
# The way we do that is by doing tree rotation multiple times until the element becomes the root.
#
# There are 3 cases to deal with:
# Note: In all cases, we consider the current node (the one we are searching for), its parent and grandparent.
#
# 1. zig-zag: The node is the right child of a left child OR
#             The node is the left child of a right child
#             Rotate in one direction at the parent node. Then rotate the other direction at the grandparent.
#             (TWO ROTATIONS)
#
# 2. zig-zig: The node is the left child of a left child OR
#             The node is the right child of a right child
#             Rotate twice in the same direction once at the grandparent and next time at the parent.
#             (TWO ROTATIONS)
#
# 3. zig    : The node is the left child of the root OR
#             The node is the right child of the root
#             Rotate a single time at the root.
#             (ONE ROTATION)
#
# Note: The aim of rotations in splay trees is not to make the tree balanced,
#       but to move the node closer to the root with each rotation.



class Node():
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.parentNode = None


    # Same as BST/AVL insert
    def insert(self, data):
        if data < self.data:
            if self.leftChild:
                self.leftChild.insert(data)
            else:
                self.leftChild = Node(data)
                self.leftChild.parentNode = self
        else:
            if self.rightChild:
                self.rightChild.insert(data)
            else:
                self.rightChild = Node(data)
                self.rightChild.parentNode = self



    def find(self, data):
        if data < self.data:
            if self.leftChild:
                return self.leftChild.find(data)
            else:
                return None
        elif data > self.data:
            if self.rightChild:
                return self.rightChild.find(data)
            else:
                return None
        else:
            return self





class Splay():
    def __init__(self):
        self.root = None

    # inserts are just like any other BST/AVL insert
    def insert(self, data):
        if not self.root:
            self.root = Node(data)
            return

        self.root.insert(data)


    def find(self, data):
        if not self.root:
            return

        node = self.root.find(data)
        if not node:
            # Node not found. Splaying not required.
            print("Data not found")
            return

        if node == self.root:
            # No splaying required since data is already at root.
            print("Data found at root")
            return


        print("Data found... Splaying...")
        # Splaying will change the root node. Hence, you have to return the new root node.
        self.root = self.splay(node)

        assert(self.root.data == data and self.root == node)



    def splay(self, node):

        parentNode = node.parentNode

        # Base case of recursion.
        # The node has now become the root. Nothing more to do. Return the new root.
        if not parentNode:
            return node



        grandParentNode = parentNode.parentNode

        if not grandParentNode:
            # "zig" case
            print("zig")
            if parentNode.leftChild == node:
                # Single right rotation
                tmp = self.rotateRight(parentNode)
            else:
                # Single left rotation
                tmp = self.rotateLeft(parentNode)


        elif grandParentNode.leftChild == parentNode and parentNode.leftChild == node:
            # "zig-zig" case
            # Two right rotations
            print("zig-zig")
            tmp = self.rotateRight(grandParentNode)
            assert(tmp == parentNode)
            tmp = self.rotateRight(tmp)


        elif grandParentNode.rightChild == parentNode and parentNode.rightChild == node:
            # "zig-zig" case
            # Two left rotations
            print("zig-zig")
            tmp = self.rotateLeft(grandParentNode)
            assert(tmp == parentNode)
            tmp = self.rotateLeft(tmp)


        else:
            # "zig-zag" case
            print("zig-zag")
            if grandParentNode.leftChild == parentNode and parentNode.rightChild == node:
                tmp = self.rotateLeft(parentNode)
                assert(tmp == node)
                tmp = self.rotateRight(grandParentNode)
            else:
                tmp = self.rotateRight(parentNode)
                assert(tmp == node)
                tmp = self.rotateLeft(grandParentNode)


        assert(tmp == node)

        return self.splay(tmp)



    # Picked directly from AVL tree implementation.
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

        return tmp


    # Picked directly from AVL tree implementation.
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

        return tmp





t = Splay()
t.insert(3)
t.insert(2)
t.insert(4)
t.find(2)
print("----------------")
t.find(4)
print("----------------")
t.find(4)
print("----------------")
t.find(3)
print("----------------")
t.find(2)
print("----------------")
t.insert(2.5)
t.find(2.5)
print("----------------")
