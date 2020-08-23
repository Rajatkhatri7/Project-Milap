def createStack():
    stack = []
    return stack


#when stack is empty
def isEmpty(stack):
    return len(stack)==0

#add item to stack
def push(stack,item):
    stack.append(item)
    print(str(item)+" pushed to stack")

def pop(stack):
    if not isEmpty(stack):
        return stack.pop() 

def peek(stack):
    if not isEmpty(stack):
        return stack[len(stack)-1]        


stack = createStack() 
print(stack)
push(stack, str(10))
print(stack) 
push(stack, str(20))
print(stack) 
push(stack, str(30))
print(stack) 
print(pop(stack) + " popped from stack")

print(stack)