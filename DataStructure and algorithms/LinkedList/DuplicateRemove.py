
from singlyLL import Node,LinkedList

def remove_dup(llist_1):
    current = llist_1.head
    prev = None
    dup_values = {}
    

    while current:
        if current.data in dup_values:
            prev.next = current.next # removing duplicating
            current = None
        else:
            dup_values[current.data] = 1 # new entry in the dictionary
            prev = current

        current = prev.next



llist_1 = LinkedList()

llist_1.appending(1)
llist_1.appending(6)
llist_1.appending(1)
llist_1.appending(6)
llist_1.appending(15)
llist_1.appending(12)
llist_1.appending(10)
llist_1.appending(15)
print("list 1 : ",end=' ' )
llist_1.print_list()

remove_dup(llist_1)
print("modified list is: ", end=' ' )
llist_1.print_list()


