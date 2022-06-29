from maxheap import MaxHeap

a = {
    'name': 'a',
    'valor': 5
}
b = {
    'name': 'b',
    'valor': 4
}
c = {
    'name': 'c',
    'valor': 3
}
heap = MaxHeap()
heap.insert(c)
heap.insert(b)
heap.insert(a)
heap.insert({'name': 'd', 'valor': 6})
heap.insert({'name': 'f', 'valor': 2})
print(heap.heapList)
print(heap.sortedList(3))
print(heap.heapList)