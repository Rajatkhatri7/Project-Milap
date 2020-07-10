#!/usr/bin/env python3

from stack import Stack

def int_to_bin(dec_num):
    s = Stack()

    while dec_num>0:
        num = dec_num%2
        s.push(num)
        dec_num = dec_num//2

    bin_num = ""
    while not s.is_empty():
        bin_num+=str(s.pop())
    return bin_num

print(int_to_bin(int(input("enter the no which u want convert to str: "))))
print(int_to_bin(int(input("enter the no which u want convert to str: "))))
print(int_to_bin(int(input("enter the no which u want convert to str: "))))