stack_size=5
stack=[None]*stack_size
top=-1

def isEmpty():
    if top==-1: return True
    else: return False

def isFull():
    return top==stack_size-1

def push(item):
    global top
    if not isFull():
        top=top+1
        stack[top]=item
        print(stack)
    else:
        print("stack is Full")

def pop():
    global top
    if not isEmpty():
        item=stack[top]
        top=top-1
        return item
    else:
        print("stack is Empty")
        return None
    
def peek():
    if not isEmpty():
        return stack[top]
    else:
        print("stack is Empty")
        return None
push(1)
push(2)
push(3)
push(4)
push(5)
pop()
push(6)
pop()
push(7)