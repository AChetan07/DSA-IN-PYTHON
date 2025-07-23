# 2.Cafe token queue
# Story: You are in charge of managing a Cafe checkout queue. Customers arrive at the queue and are processed in a first-come, first-served order. Each customer has a unique ID, and once a customer is checked out, they leave the queue. You need to implement a system that can add a customer to the queue, process the first customer in line, and check if the queue is empty.
# Data Structure: Queue
# Functions to Implement:
# •	Enqueue a customer
# •	Dequeue a customer (process the next customer)
# •	Check if the queue is empty
# •	Display the current queue

class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CafeQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, cid):
        new= node(cid)
        if self.front is None:
            self.front = new
            self.rear = new
        else:
            self.rear.next = new
            self.rear = new
        print(f"Customer {cid} joined the queue.")

    def dequeue(self):
        if self.front is None:
            print("Queue empty")
            return
        temp = self.front
        self.front = temp.next
        temp.next = None
        print(f"Customer {temp.data} dequeued")
        if self.front is None:
            self.rear = None
    def queuempty(self):
        if self.front is None:
            print("queue empty")
        else:
            print("queue is not empty")
    def display(self):
        if self.front is None:
            print("Queue  empty.")
            return
        itr = self.front
        print("queue:")
        while itr:
            print(f"Customer ID: {itr.data}", end='  ')
            itr = itr.next
        print("None")

a=CafeQueue()
a.enqueue(1)
a.enqueue(2)
a.enqueue(3)
a.display()
a.dequeue()
a.display()



