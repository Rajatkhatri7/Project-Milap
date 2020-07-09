#!/usr/bin/env python3



class Stack():
    
    def  __init__(self):
        self.items = []

    def is_empty(self): #chk if stack is empty or not
        return self.items == []

    def peek(self):
        if not self.is_empty():
            return self.items[-1]    

    def push(self,item):
        self.items.append(item)    

    def pop(self):
        return self.items.pop()

    def get_stack(self):
        return self.items


stck1 = Stack()

stck1.push("a")
stck1.push("b")
stck1.push("c")

print(f' Initial stack elements are : {stck1.get_stack()}')

stck1.pop()
print(f"Elements of stack after poping the elements: {stck1.get_stack()}")

print(f'Peeking to the stack : {stck1.peek()}')