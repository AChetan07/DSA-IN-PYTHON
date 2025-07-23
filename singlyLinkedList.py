# L=[1,2,3]
# def add_at_end(data):
#     L.append(data)
    
# def  add_at_start(data):
#     L.insert(0,data)

# def removeatend(data):
#     L.pop()
# def removeatstart(data):
#     L.pop(0)


# def  display():
#     print(L);

# display()

#linked list using oops   n
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

ll= LinkedList()
ll.add_at_end(50)
ll.add_at_start(30)
ll.add_at_end(40)
ll.add_at_start(20)
ll.display()
ll.del_at_end()
ll.del_at_St()
ll.display()


