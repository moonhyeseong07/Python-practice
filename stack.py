class stack:
    def __init__(self):
        self.stack_size=5
        self.stack=[0]*5
        self.top=-1
    def isEmpty(self):
        return self.top==-1
    def isFull(self):
        return self.top+1==self.stack_size
    def push(self,e):
        if self.isFull():
            print("full")
            return
        self.top+=1
        self.stack[self.top]=e
        print(self.stack)
    def pop(self):
        if self.isEmpty():
            print("empty")
            return
        pop_element=self.stack[self.top]
        self.top-=1
        print(self.stack)
        return(pop_element)
    def peek(self):
        if self.isEmpty(self):
            print("empty")
            return
        return stack[self.top]
    def top_index(self):#탑 인덱스 출력 함수
        return[self.top]#탑의 인덱스 값을 리턴

stack_a=stack()
stack_a.push(1)
stack_a.push(2)
stack_a.push(2)
stack_a.push(2)
stack_a.push(2)
print(stack_a.pop())
print(stack_a.pop())
print(stack_a.pop())
print(stack_a.pop())
print(stack_a.pop())
print(stack_a.pop())
print(stack_a.pop())
print(stack_a.top)
print(stack_a.pop())
print(stack_a.top)
'''
max_stack=5
stack=[0]*max_stack
def init_stack():
    global top
    top=-1
def isEmpty_stack():
    return top==-1
def isFull_stack():
    return top+1==max_stack
def push_stack(e):
    global top,stack
    if isFull_stack():
        print("full")
        return
    top+=1
    stack[top]=e
    print(stack)
def pop_stack():
    global top
    if isEmpty_stack():
        print("empty")
        return
    pop_element=stack[top]
    top-=1
    print(stack)
    return pop_element
def peek_stack():
    if isEmpty_stack():
        print("empty")
        return
    return stack[top]
init_stack()
push_stack(1)
push_stack(2)
push_stack(3)
push_stack(4)
push_stack(5)
push_stack(6)
print(pop_stack(),top)

'''