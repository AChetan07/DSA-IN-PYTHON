# # heap data structure
# # heap is a special tree-based data structure that satisfies heap property
# # in a max heap for any given node the value of i is greater than or equal to the values of its children
# # in a min heap the value of i is less than or equal to the values of its children.
# # heaps are commonly used to implement priority queues where the highest priority element is always at the root of the heaap
# # heaps can be implemented usinf arrays parent-child relationship is defined by the indices of the array

# # int his implemetation we will use a list to represent the heap and implement basic operations such as insertion deletion and hepify
# # we will also implement a method to print the heap in a readable format
# heap is a special tree based daya structure that satisfies the heap property
# in a max heap for any given node I , the value of i is greater than or equal to the value of itss children.

import heapq
num={1,3,5,7,9,2,4,6,8,0}
heapq.heapify(num)  #heapify the list
print(f"heap is {num}")

# to get max value of heap

heapq.heappop(num)
print(f"Remaining values {num}")

# differences between heap and heapq , heap and graph

