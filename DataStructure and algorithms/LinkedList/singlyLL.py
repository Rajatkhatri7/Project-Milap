#!/usr/bin/env python3
class Node:
    def __init__(self,data):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None       


    def appending(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
            new_node.next = None
            return
        else:
            new_node = Node(data)
            last_node = self.head
            while last_node.next:
                last_node = last_node.next
            last_node.next = new_node
            new_node.next = None

    def prepend(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
            new_node.next = None
            return
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node


    def insert_after(self,target_node,data):
        ptr = self.head
        while ptr: 
            if target_node not in ptr.data:
                print("target node not in the list") 
                return
            else:

                new_node = Node(data)

                new_node.next = ptr.next
                ptr.next = new_node
            ptr = ptr.next



    def print_list(self):
        ptr = self.head
        while ptr:
            print(ptr.data)
            ptr = ptr.next


llist = LinkedList()
llist.appending("A")
llist.appending("B")
llist.appending("C")


llist.insert_after("m", "D")

llist.print_list()  