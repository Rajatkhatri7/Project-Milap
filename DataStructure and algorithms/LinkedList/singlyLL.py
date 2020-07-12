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

    def delete_node(self,key): # deletion by data
        ptr = self.head  #when key is starting position
        if ptr and ptr.data ==key:
            self.head = ptr.next
            ptr = None
            return
        else: # when deleting element is at other position
            prev = None
            while ptr and ptr.data!=key:
                prev = ptr
                ptr = ptr.next
            if ptr is None:
                print("Provided node is not present in the linked list")
                return 
            prev.next = ptr.next
            ptr = None    # removing garbage value


    def delet_by_position(self,pos): #deletion by position
        if self.head:  
            ptr  = self.head
        if pos == 0:     # when starting postion given
            self.head = ptr.next
            ptr  = None
            return    
        else:             #when other than starting postion
            prev = None
            pos_count = 0
            while ptr and pos_count!=pos:
                prev = ptr
                ptr = ptr.next
                pos_count+=1
            if ptr == None:
                print("Index out of range")
            else:    
                prev.next = ptr.next
                ptr = None         

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

llist.delete_node("B")
llist.delete_node("V")
llist.delet_by_position(5)
llist.delet_by_position(0)
llist.print_list()  