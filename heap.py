class Heap:
    """
    Heap class
    """
    def __init__(self):
        self.heapList = []
        self.size = 0

    def parentIndex(self, index):
        return (index-1) // 2

    def leftChildIndex(self, index):
        return 2 * index + 1

    def leftChild(self, index):
        """
        Get value of left child
        :param index:
        :return:
        """
        leftIndex = self.leftChildIndex(index)
        if leftIndex < self.size:
            return self.heapList[leftIndex]
        return -1

    def rightChildIndex(self, index):
        return 2 * index + 2

    def rightChild(self, index):
        """
        Get value of right child
        :param index:
        :return:
        """
        rightIndex = self.rightChildIndex(index)
        if rightIndex < self.size:
            return self.heapList[rightIndex]
        return -1

    def searchElement(self, itm):
        i = 0
        while i <= self.size:
            if itm == self.heapList[i]:
                return i
            i += 1

    def maximumChildIndex(self, idx):

        valueLeftChild = self.leftChild(idx)
        valueRightChild = self.rightChild(idx)
        if valueRightChild == -1:
            return self.leftChildIndex(idx)
        elif valueLeftChild['valoracion'] > valueRightChild['valoracion']:
            return self.leftChildIndex(idx)
        elif valueLeftChild['valoracion'] < valueRightChild['valoracion']:
            return self.rightChildIndex(idx)
        else :
            # return any child index
            return self.leftChildIndex(idx)

    def minimumChildIndex(self, idx):
        valueLeftChild = self.leftChild(idx)
        valueRightChild = self.rightChild(idx)
        #print("valueLeftChild = %d" % valueLeftChild)
        #print("valueRightChild = %d" % valueRightChild)

        if valueRightChild == -1 :
            return self.leftChildIndex(idx)

        if valueLeftChild > valueRightChild :
            return self.rightChildIndex(idx)
        elif valueLeftChild < valueRightChild :
            return self.leftChildIndex(idx)
        else :
            # return any child index
            return self.rightChildIndex(idx)

    def getTop(self):
        """
        Get root value for Heap
        :return:
        """
        if self.size == 0:
            return -1
        return self.heapList[0]

    def percolateDown(self, i):
        pass

    def buildHeap(self,list):
        """
        Built heap from array
        :param list:
        :return:
        """
        i = len(list) // 2
        self.size = len(list)
        self.heapList = list
        print("")
        while i >= 0:
            tmp = self.heapList[i]
            #print("percolate-down ", tmp , " <<", self.heapList)
            self.percolateDown(i)
            #print("percolate-down ", tmp , " >>", self.heapList)
            #print("")
            i = i - 1

    def percolateUp(self, i):
        pass

    def insert(self, k):
        '''
        Insert an element at the end
        of heap and apply percolate up
        :param k:
        :return:
        '''
        self.heapList.append(k)
        self.size = self.size + 1
        self.percolateUp(self.size - 1)

    def delete(self):
        '''
        Delete an element from top
        of heap and apply percolate doown
        :return:
        '''
        ret = self.heapList[0]
        self.heapList[0] = self.heapList[self.size-1]
        self.size = self.size-1
        self.heapList.pop()
        self.percolateDown(0)
        return ret

    def interchangeTopWithBottom(self):
        '''
        interchange first and last element
        of heap
        :return:
        '''
        tmp = self.heapList[0]
        self.heapList[0] = self.heapList[self.size - 1]
        self.heapList[self.size - 1] = tmp
        self.size = self.size - 1
        self.percolateDown(0)

#
#             10 ->0
#        3->1      9->2
#    1->3 2->4  7->5 8->6
#

if __name__ == '__main__':
    new_heap = Heap()
    new_heap.heapList = [10, 3, 9, 1, 2, 7, 8]
    print(new_heap.heapList)
