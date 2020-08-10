from singlyLL import Node, LinkedList

def N_to_last(llist,n):

    p = llist.head
    q = llist.head


    count = 0
    while q:
        count+=1      # we have to make q point to n nodes beyond the head. 
        if(count>=n):
            break
        q = q.next


    if not q:
        print(str(n)+ " is greater than the number of nodes in the list")    

        return

    while p and q.next:
        p = p.next
        q = q.next
    return p.data
   



