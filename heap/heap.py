class Heap():

    HEAP_SIZE = 1000

    def __init__(self):
        self.heap = [0] * self.HEAP_SIZE
        self.cur_pos = -1 # no elements in the heap

    def insert(self, data, no_heapify=False):
        self.cur_pos += 1
        self.heap[self.cur_pos] = data

        if no_heapify:
            # Don't do heapify right now.
            return
        else:
            self.fixUp(self.cur_pos)

    def fixUp(self, index):
        # Recursive fixUp
        #if index <= 0:
        #    # Reached the top of the heap. fixUp is done.
        #    return
        #else:
        #    parent_index = (int)((index - 1) / 2) # Note: This works for both left and right children

        #    if self.heap[parent_index] < self.heap[index]:
        #        # swap parent and child
        #        self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]
        #        self.fixUp(parent_index)
        #    else:
        #        return



        # Iterative fixUp
        while index > 0:
            parent_index = (int)((index - 1) / 2) # Note: This works for both left and right children

            if self.heap[parent_index] < self.heap[index]:
                # swap parent and child
                self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]
                index = parent_index
            else:
                break
            


    def fixDown(self, index):
        # Recursive fixDown
        #if index > self.cur_pos:
        #    return

        #leftChild  = 2 * index + 1
        #rightChild = 2 * index + 2

        #val_leftChild = self.heap[leftChild] if leftChild <= self.cur_pos else float('-inf')
        #val_rightChild = self.heap[rightChild] if rightChild <= self.cur_pos else float('-inf')

        #if self.heap[index] < max(val_leftChild, val_rightChild):
        #    if val_leftChild > val_rightChild:
        #        self.heap[index], self.heap[leftChild] = self.heap[leftChild], self.heap[index]
        #        self.fixDown(leftChild)
        #    else:
        #        self.heap[index], self.heap[rightChild] = self.heap[rightChild], self.heap[index]
        #        self.fixDown(rightChild)


        # Iterative fixDown
        while index <= self.cur_pos:
            leftChild  = 2 * index + 1
            rightChild = 2 * index + 2

            val_leftChild = self.heap[leftChild] if leftChild <= self.cur_pos else float('-inf')
            val_rightChild = self.heap[rightChild] if rightChild <= self.cur_pos else float('-inf')

            if self.heap[index] < max(val_leftChild, val_rightChild):
                if val_leftChild > val_rightChild:
                    self.heap[index], self.heap[leftChild] = self.heap[leftChild], self.heap[index]
                    index = leftChild
                else:
                    self.heap[index], self.heap[rightChild] = self.heap[rightChild], self.heap[index]
                    index = rightChild
            else:
                break


    def heapify(self):
        # Case when no_heapify = True

        # Heapify from the beginning of the array
        #for i in range(self.cur_pos + 1):
        #    # 1. Swap 'i' with the largest of its two children
        #    # 2. Call fixUp on 'i' 
        #    leftChild  = 2 * i + 1
        #    rightChild = 2 * i + 2

        #    val_leftChild = self.heap[leftChild] if leftChild <= self.cur_pos else float('-inf')
        #    val_rightChild = self.heap[rightChild] if rightChild <= self.cur_pos else float('-inf')

        #    if self.heap[i] < max(val_leftChild, val_rightChild):
        #        if val_leftChild > val_rightChild:
        #            self.heap[i], self.heap[leftChild] = self.heap[leftChild], self.heap[i]
        #        else:
        #            self.heap[i], self.heap[rightChild] = self.heap[rightChild], self.heap[i]

        #        self.fixUp(i)
            



        # Heapify from the end of the array
        for i in range(self.cur_pos, -1, -1):
            # 1. Swap 'i' with the largest of its two children
            # 2. Call fixDown on the largest child
            leftChild  = 2 * i + 1
            rightChild = 2 * i + 2

            val_leftChild = self.heap[leftChild] if leftChild <= self.cur_pos else float('-inf')
            val_rightChild = self.heap[rightChild] if rightChild <= self.cur_pos else float('-inf')

            if self.heap[i] < max(val_leftChild, val_rightChild):
                if val_leftChild > val_rightChild:
                    self.heap[i], self.heap[leftChild] = self.heap[leftChild], self.heap[i]
                    self.fixDown(leftChild)
                else:
                    self.heap[i], self.heap[rightChild] = self.heap[rightChild], self.heap[i]
                    self.fixDown(rightChild)




    def heapsort(self):
        # 1. Swap first element with last.
        #    Now, last element is sorted.
        # 2. Call fixDown() on the first element.
        while self.cur_pos > 0:
            self.heap[0], self.heap[self.cur_pos] = self.heap[self.cur_pos], self.heap[0]
            self.cur_pos -= 1
            self.fixDown(0)



h = Heap()
for i in range(900):
    h.insert(i, False)
h.heapsort()
print(h.heap)
