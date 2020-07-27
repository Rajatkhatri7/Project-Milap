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

    
    def print_list(self):
        ptr = self.head
        while ptr:
            print(ptr.data)
            ptr = ptr.next        

    def reverse_iteratiion(self): #swapping via iteration

        prev = None
        current = self.head
        while current !=None:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        self.head = prev    


    def recursive_reverse(self):

        def _reverse_reverse(current,prev):
            if not current: #base case when current reach the end of linked list ,current is None 
                return prev


            nxt = current.next
            current.next = prev
            prev = current
            current = nxt

            return _reverse_reverse(current,prev)


        self.head = _reverse_reverse(current = self.head,prev = None)    



llist = LinkedList()
llist.appending("A")
llist.appending("B")
llist.appending("C")
llist.appending("D")

print("Original List")
llist.print_list()


print("reversing by recursion: ")
llist.recursive_reverse()
llist.print_list()

print("reverse the list via iteration: ")
llist.reverse_iteratiion()
#see in the results swapping happens
llist.print_list()        