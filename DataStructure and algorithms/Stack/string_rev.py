#!/usr/bin/env python3
from stack import Stack

def str_rev(stack,inp_str):
    for word in inp_str:
        stack.push(word)
    rev_str = ""
    while not stack.is_empty():
        rev_str+=stack.pop()    

    return rev_str


stack = Stack()
inp_str = input("Enter your str: ")
print(str_rev(stack,inp_str))        