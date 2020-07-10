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

