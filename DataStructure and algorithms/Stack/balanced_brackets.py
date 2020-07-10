#!/usr/bin/env python3

from stack import Stack

def is_balanced(inp_str):
    
    s = Stack()
    index = 0
    is_balanced = True

    while index<len(inp_str) and is_balanced:
        str_ele = inp_str[index]

        if str_ele in "({[":
            s.push(str_ele)
        else:
            if s.is_empty():
                is_balanced = False   #opening bracket finished and stack is empty       

            else:
                top = s.pop()
                if not is_match(top,str_ele):
                    is_balanced = False    
        index+=1

    if s.is_empty() and is_balanced:
        return True
    else:
        return False

def is_match(p1,p2):
    if p1=="(" and p2 == ")":
        return True
    elif p1 == "{" and p2 == "}":
        return True
    elif p1 == "[" and p2 == "]":
        return True
    else:
        return False            


print("String : (((({})))) Balanced or not?")
print(is_balanced("(((({}))))"))

print("String : [][]]] Balanced or not?")
print(is_balanced("[][]]]"))

print("String : [][] Balanced or not?")
print(is_balanced("[][]"))        