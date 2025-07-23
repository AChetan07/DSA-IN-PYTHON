# stack using list
# stack operations
# class stack:
#         def __init__(self):
#             self.stack=[]
#         def push(self,data):
#             self.stack.append(data)
#         def pop(self):
#              self.stack.pop()
#         def display(self):
#              print(self.stack)
# st=stack()
# st.push(50)
# st.push(20)
# st.push(30)
# st.push(69)
# st.push(40)
# st.push(70)
# st.push(320)
# st.push(420)
# st.display()
# st.pop()
# st.pop()
# st.pop()
# st.pop()
# st.display()

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Stack:
     def __init__(self):
          self.head=None
     def push(self,data):
          new=Node(data)
          if self.head is not  None:
               new.next = self.head
               self.head = new

          self.head=new
     def pop(self):
            itr=self.head
            self.head=itr.next
            itr=None
# for queue instead of pop add code of popping at rear end




    
