class Node():
    def __init__(self, data):
        self.data  = data          # stores each of the characters in the key
        self.value = None          # stores the value associated with the key

        self.leftChild   = None
        self.middleChild = None
        self.rightChild  = None



class TST():
    def __init__(self):
        self.root = None


    def put(self, key, value):
        if not key:
            return

        self.root = self.putItem(key, value, self.root, 0)


    def putItem(self, key, value, node, index):
        if not node:
            node = Node(key[index])
            # IMP: No incrementing of index here

        if key[index] < node.data:
            node.leftChild = self.putItem(key, value, node.leftChild, index)

        elif key[index] > node.data:
            node.rightChild = self.putItem(key, value, node.rightChild, index)

        else:
            if (index + 1) == len(key):
                # we have reached the end of the key
                node.value = value
            else:
                node.middleChild = self.putItem(key, value, node.middleChild, index + 1)

        return node


    def get(self, key):
        if not key:
            return None

        return self.getItem(key, self.root, 0)


    def getItem(self, key, node, index):
        if not node:
            return None

        if key[index] < node.data:
            return self.getItem(key, node.leftChild, index)

        elif key[index] > node.data:
            return self.getItem(key, node.rightChild, index)

        else:
            if (index + 1) == len(key):
                return node.value
            else:
                return self.getItem(key, node.middleChild, index + 1)


