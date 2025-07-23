# 3.Tickets booking system using stack:
# Story: You are responsible for managing the reservation of tickets for Movie/Train. Passengers can book tickets for, but they can also cancel or undo their previous reservation. You need to keep track of the reservations using a stack, where each booking is added to the top of the stack, and a cancellation undoes the most recent booking.
# Data Structure: Stack
# Functions to Implement:
# •	Push a reservation (book a ticket)
# •	Pop a reservation (cancel the most recent booking)
# •	Display current reservations
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Ticket:
    def __init__(self):
        self.top = None

    def push(self, booking):
        new = Node(booking)
        if self.top is not None:
            new.next = self.top
        self.top = new
        print(f"Booking done: {booking}")

    def pop(self):
        if self.top is None:
            print("No bookings to cancel.")
            return
        temp = self.top
        print(f"Booking cancelled: {temp.data}")
        self.top = temp.next
        temp.next = None

    def display(self):
        if self.top is None:
            print("No current bookings.")
            return
        temp = self.top
        print("Current bookings:")
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print("None")

ts = Ticket()
ts.push("T1 ")
ts.push("T2 ")
ts.push("T3")
ts.display()
ts.pop()
ts.pop()
ts.display()
