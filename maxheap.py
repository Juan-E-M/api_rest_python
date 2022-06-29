from heap import Heap

class MaxHeap(Heap):
    def __init__(self):
        Heap.__init__(self)

    def percolateDown(self, i):
        """
        Apply function percolate up to heap
        :return:
        """
        while self.leftChildIndex(i) < self.size:
            maximumChildIndex = self.maximumChildIndex(i)
            if self.heapList[i]['valoracion'] < self.heapList[maximumChildIndex]['valoracion']:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[maximumChildIndex]
                self.heapList[maximumChildIndex] = tmp
            i = maximumChildIndex

    def percolateUp(self, i):
        """
        Apply to percolate up to heap
        :return:
        """
        iParent = self.parentIndex(i)
        while iParent >= 0:
            #print(iParent)
            #print(i)
            if self.heapList[iParent]['valoracion'] < self.heapList[i]['valoracion']:
                tmp = self.heapList[iParent]
                self.heapList[iParent] = self.heapList[i]
                self.heapList[i] = tmp
            i = iParent
            iParent = self.parentIndex(i)
            #print(self.heapList)

    def sortedList(self, n):
        if n <= self.size:
            return [self.delete() for element in range(n)]
        else:
            return [self.delete() for element in range(self.size)]


if __name__ == '__main__':
    LIST_ORIGIN = [3, 9, 10, 1, 7, 2, 8, 20, 5]

    list = LIST_ORIGIN

    heap = MaxHeap()

    for i in range(len(list)):
        #print("c[%d] = %d" % (i,list[i]))
        heap.insert(list[i])
        print("--------------------------")
        print(heap.heapList)

    print("--------------------------")
    print("input <<",list)
    print("output >>",heap.heapList)

    print(heap.sortedList(6))
    print("new output >>", heap.heapList)

    '''LIST_ORIGIN = [3, 9, 10, 1, 7, 2, 8, 20, 5]

    list = LIST_ORIGIN
    print(list)
    heap = MaxHeap()
    heap.buildHeap(list)

    print("=========================")
    for i in range(len(heap.heapList)):
        print(heap.heapList)
        ret = heap.delete()
        print("------------------------")
        print("attend --> ", ret)

    print(heap.heapList)'''

    '''list = [10, 3, 9, 1, 2, 7, 8, 12, 465, 7767, 2, 45]
    print("====== Array Unsorted =======")
    print(list)
    heap = MaxHeap()
    heap.buildHeap(list)
    print("========== Heaps ============")
    print(heap.heapList)
    print("======- Start Sorted ========")
    for i in range(len(heap.heapList)):
        print("--- Extract %d number -----" % (i + 1))
        heap.interchangeTopWithBottom()
        print(heap.heapList)
    print("======- Array Sorted ========")
    print(heap.heapList)'''



    '''LIST_ORIGIN = [3, 9, 10, 1, 7, 2, 8, 20, 5]

    list = LIST_ORIGIN

    heap = MaxHeap()

    for i in range(len(list)):
        #print("c[%d] = %d" % (i,list[i]))
        heap.insert(list[i])
        print("--------------------------")
        print(heap.heapList)

    print("--------------------------")
    print("input <<",list)
    print("output >>",heap.heapList)'''



    '''LIST_ORIGIN = [3, 9, 10, 1, 7, 2, 8, 20, 5]

    list = LIST_ORIGIN
    print(list)
    heap = MaxHeap()
    heap.buildHeap(list)

    print("=========================")
    for i in range(len(heap.heapList)):
        print(heap.heapList)
        ret = heap.delete()
        print("------------------------")
        print("attend --> ", ret)

    print(heap.heapList)'''

    '''LIST_ORIGIN = [3, 9, 10, 1, 7, 2, 8, 20, 5]
    list = LIST_ORIGIN
    print("input <<",list)
    heap = MaxHeap()
    heap.buildHeap(list)
    print("output >>", heap.heapList)'''


