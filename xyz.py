class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedListQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        if self.head is None:
            print("Queue is empty")
            return
        print(f"Dequeued: {self.head.data}")
        self.head = self.head.next
        if self.head is None:
            self.tail = None

    def front(self):
        if self.head:
            print(f"Front: {self.head.data}")
        else:
            print("Queue is empty")

    def rear(self):
        if self.tail:
            print(f"Rear: {self.tail.data}")
        else:
            print("Queue is empty")

    def size(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        print(f"Size: {count}")
        return count


# Example usage
obj = LinkedListQueue()
obj.enqueue(89)
obj.enqueue(42)
obj.enqueue(17)
obj.front() 
obj.rear()   
obj.size()  
obj.dequeue()
obj.front()  
