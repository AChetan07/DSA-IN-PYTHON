# 1.Library management system using linked list
# Story: Imagine you are the librarian of a local library. You need to manage a collection of books using a linked list, where each book has a title, author, and a unique ID. You need to be able to add new books to the collection, delete old books, search for a specific book by title, and print the list of all books.
# Data Structure: Singly Linked List
# Functions to Implement:
# •	Add a book
# •	Delete a book by ID
# •	Search for a book by title
# •	Print all books


class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None

    def insertion(self, bookid, title, author):
        data = {'id': bookid, 'title': title, 'author': author}
        new = node(data)
        if self.head is None:
            self.head = new
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = new
    def deletion(self,bookid):
        if self.head  is None:
            print("Empty")
            return
        itr =self.head
        while itr.next is not None:
           if itr.next.data['id'] == bookid: 
               temp=itr.next
               itr.next=temp.next
               temp.next=None
               print(f"{bookid} deleted")
               return
           itr=itr.next
        print("Invalid")
    def print(self):
        if self.head is None:
            print("Empty")
            return
        itr = self.head
        print("Books:-")
        while itr:
           print(f"ID: {itr.data['id']}, Title: {itr.data['title']}, Author: {itr.data['author']}")
           itr = itr.next
    def search(self, title):
        if self.head is None:
            print("Library is empty.")
            return

        itr = self.head
        while itr is not None:
            if itr.data['title'] == title:
                print(" Found:", end=' ')
                print(f"ID: {itr.data['id']}, Title: {itr.data['title']}, Author: {itr.data['author']}")
                return
            itr = itr.next

        print(f"No book with title '{title}' found.")


ll = LinkedList()
ll.insertion(1, "Atomic habits", "James Clear")
ll.insertion(2, "Psychology Of Money", "Morgan Housel")
ll.print()
ll.search("Psychology Of Money")
ll.deletion(2)
ll.print()




       



               

        
   
