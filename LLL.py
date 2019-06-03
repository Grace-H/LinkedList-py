#LLL.py: contains Node class and LLL class
#Author: Grace-H
#Date: 02 June 2019

#class Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

#class LLL, implementation of a Linear Linked List
class LLL:
    def __init__(self, head=None):
        self.head = head

    #return all data members space-seperated
    def __str__(self):
        out = ""
        cur = self.head
        while cur:
            out += str(cur)
            out += " "
            cur = cur.next
        return out

    #add item to end of list
    def add(self, data):
        n = Node(data)

        #if head is None
        if self.head is None:
            self.head = n
        else:
            #go to end of list
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = n

    #remove item from list
    def remove(self, data):
        #find object
        cur = self.head
        prev = None
        while cur:
            #break when object found
            if cur.data == data:
                break
            prev = cur
            cur = cur.next

        #if object was found, remove it, change pointers
        #cur will be None if end of lis was reached before object found
        if cur is not None:
            if prev is not None:
                prev.next = cur.next
            else:
                self.head = cur.next
