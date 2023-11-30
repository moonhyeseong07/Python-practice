class stack:
    def __init__(self,size=5):
        self.stack_size=size
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
    def pop(self):
        if self.isEmpty():
            print("empty")
            return
        pop_element=self.stack[self.top]
        self.top-=1
        return(pop_element)
    def peek(self):
        if self.isEmpty():
            print("empty")
            return
        return self.stack[self.top]
def priority(op):
    if op=='('or op==')': return 0
    elif op=='+'or op=='-': return 1
    elif op=='*'or op=='/': return 2
    else: return -1
def change(expr):
    s=stack(100)
    output=[]
    for term in expr:
        if term in '(':
            s.push('(')
        elif term in ')':
            while not s.isEmpty():
                op=s.pop()
                if op=='(':
                    break
                else:
                    output.append(op)
        elif term in "+-/*":
            while not s.isEmpty():
                op=s.peek()
                if priority(term)<=priority(op):
                    output.append(op)
                    s.pop()
                else: break
            s.push(term)
        else:
            output.append(term)
    while not s.isEmpty():
        output.append(s.pop())
    return output
a=input()
n=change(a)
for i in n:
    print(i,end='')