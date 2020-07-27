#!/usr/bin/env python3

from singlyLL import Node,LinkedList

def merge_sorted(llist_1,llist2):

    p = llist_1.head
    q = llist2.head
    s = None

    if not p:
        return q
    if not q:
        return p


    if p and q: #when p and q are not none

        if p.data<=q.data:
            s = p
            p = s.next


        else:
            s = q
            q = s.next
        new_head  = s

    while p and q:
      if p.data <= q.data:
          s.next = p 
          s = p 
          p = s.next
      else:
          s.next = q
          s = q
          q = s.next
    if not p:
        s.next = q 
    if not q:
        s.next = p 
    return new_head

llist_1 = LinkedList()
llist_2 = LinkedList()

llist_1.appending(1)
llist_1.appending(5)
llist_1.appending(7)
llist_1.appending(9)
llist_1.appending(10)

print("list 1 : ",end=' ' )
llist_1.print_list()

llist_2.appending(2)
llist_2.appending(3)
llist_2.appending(4)
llist_2.appending(6)
llist_2.appending(8)

print("list 2: ", end=' ')
llist_2.print_list()



print("sorted list: ",end=' ')
merge_sorted(llist_1,llist_2)
llist_1.print_list()