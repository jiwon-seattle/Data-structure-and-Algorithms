class MinHeap:
    def __init__(self,heapsize):
        self.heapsize = heapsize
        self.minheap = [0] * (heapsize + 1)
        self.realSize = 0

    def add(self, element):
        if self.realSize > self.heapsize:
            print("Add too many elements!")
            self.realSize -= 1
            return
        self.minheap[self.realSize] = element
        index = self.realSize
        parent = index // 2
        while (self.minheap[index] < self.minheap[parent] and index > 1):
            self.minheap[parent], self.minheap[index] = self.minheap[index], self.minheap[parent]
            index = parent
            parent = index //2
    def peek(self):
        return self.minheap[1]

    def pop(self):
        if self.realSize < 1:
            print("Don't have any element!")
            return
        else:
            removeElement = self.minheap[1]
            self.minheap[1] = self.minheap[self.realSize]
            self.realSize -= 1
            index = 1
            while (index < self.realSize and index <= self.realSize // 2):
                left = index * 2
                right = (index * 2) + 1
                if (self.minheap[index] > self.minheap[left] or self.minheap[index] > self.minheap[right]):
                    if self.minheap[left] < self.minheap[right]:
                        self.minheap[left], self.minheap[index] = self.minheap[index], self.minheap[left]
                        index = left

                    else:
                        self.minheap[right], self.minheap[index] = self.minheap[index], self.minheap[right]
                        index = right
                else:
                    break
            return removeElement
    def size(self):
        return self.realSize

    def __str__(self):
        return str(self.miheap[1:self.realSize+1])
