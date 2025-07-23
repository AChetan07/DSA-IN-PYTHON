
# def maxfunc(n):
#     l=[15,25,7,65,93,47,19]
#     print(l)

#     for i in range(n+1,max(l)+1):
#         if i in l:
#             print(i)
#             break
#         else:
#             print(n,"Itself is greatest")
#             break

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    def  add_at_end(self,data):
        new=Node(data)
        if self.head is None:
            self.head=new
            return
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=new

    def add_at_start(self,data):
        new= Node(data)
        new.next=self.head
        self.head=new
    def display(self):
        itr=self.head
        while itr:
            print(itr.data,end='->')
            itr=itr.next
        print("None")
    def del_at_St(self):
         if self.head is None:
            print("Cannot remove form empty Linked List")
            return
         itr=self.head
         self.head=itr.next
         itr.next=None

    def del_at_end(self):
        itr=self.head
        while itr.next.next:
            itr=itr.next
        itr.next=None

# n=int(input("Enter a number"))
# maxfunc(n)
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class linkedlist:
#      def __init__(self):
#         self.head=None
    
n=int(input("enter number"))
r=n
ng =n
itr=self.head

while itr:
    if  itr.data>n:
        if itr.data-n<r:
            r=itr-n
            ng=itr.data
        itr=itr.next


# n = 5
# for i in range(n):
#     for j in range(n):
#         if j == n - i - 1:
#             print("*", end=" ")
#         else:
#             print(n - j, end=" ")
#     print()
