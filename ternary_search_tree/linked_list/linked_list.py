class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = None

    def insertStart(self, data):
        newNode = Node(data)

        if not self.head:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def insertEnd(self, data):
        newNode = Node(data)

        if not self.head:
            self.head = newNode
        else:
            tmp = self.head
            while tmp.next:
                tmp = tmp.next

            tmp.next = newNode


    def delete(self, data):
        if not self.head:
            return

        if self.head.data == data:
            self.head = self.head.next
        else:
            cur  = self.head.next
            prev = self.head
            while cur:
                if cur.data == data:
                    prev.next = cur.next
                    return

                prev = cur
                cur  = cur.next


    def traverse(self):
        tmp = self.head
        while tmp:
            print(tmp.data)
            tmp = tmp.next

