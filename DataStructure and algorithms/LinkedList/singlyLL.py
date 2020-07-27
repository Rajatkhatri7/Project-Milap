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


    def lengthOfList(self): #normal implementation
        count = 0
        ptr = self.head
        while ptr:
            count+=1
            ptr = ptr.next
        return count

    def lenByRecursion(self,node): # len by recursion
        if node is None:
            return 0
        return 1+self.lenByRecursion(node.next)


    def print_list(self):
        ptr = self.head
        while ptr:
            
            print(ptr.data,end=" -> ")
            ptr = ptr.next
        print("None")


    def swap_nodes(self,key1,key2):

    

        if key1==key2:
            return

    #traversing to find the key
        prev1  = None
        curr1 = self.head
        while curr1 and curr1.data!=key1:
            prev1 = curr1
            curr1 = curr1.next

        prev2 = None
        curr2 = self.head
        while curr2 and curr2.data!=key2:
            prev2 = curr2
            curr2 = curr2.next

        if not curr1 or not curr2: # case when one of the two node are not present
            return


    # if key is at starting node
        if prev1:
            prev1.next = curr2
        else:
            self.head = curr2            


        if prev2:
            prev2.next = curr1
        else:
            self.head = curr1        

        curr1.next , curr2.next = curr2.next , curr1.next





# llist = LinkedList()
# llist.appending("A")
# llist.appending("B")
# llist.appending("C")
# llist.appending("D")

# print("Original List")
# llist.print_list()






# llist.swap_nodes("B", "C")
# print("Swapping nodes B and C that are not head nodes")
# llist.print_list()

# llist.swap_nodes("A", "B")
# print("Swapping nodes A and B where key_1 is head node")
# llist.print_list()

# llist.swap_nodes("D", "B")
# print("Swapping nodes D and B where key_2 is head node")
# llist.print_list()

# llist.swap_nodes("C", "C")
# print("Swapping nodes C and C where both keys are same")
# llist.print_list()