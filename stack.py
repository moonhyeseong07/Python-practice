class stack:
    def __init__(self):
        self.stack_size = 5  # 스택의 크기를 나타내는 변수
        self.stack = [0] * 5  # 스택을 저장하는 리스트, 모든 요소를 0으로 초기화
        self.top = -1  # 스택의 가장 위를 가리키는 변수

    def isEmpty(self):
        return self.top == -1  # 스택이 비어있는지 확인하는 함수

    def isFull(self):
        return self.top + 1 == self.stack_size  # 스택이 가득 차 있는지 확인하는 함수

    def push(self, e):
        if self.isFull():
            print("full")  # 스택이 가득 차 있는 경우 full 출력
            return
        self.top += 1
        self.stack[self.top] = e
        print(self.stack)  # 스택의 현재 상태 출력

    def pop(self):
        if self.isEmpty():
            print("empty")  # 스택이 비어있는 경우 empty 출력
            return
        pop_element = self.stack[self.top]
        self.top -= 1
        print(self.stack)  # 스택의 현재 상태 출력
        return pop_element

    def peek(self):
        if self.isEmpty(self):
            print("empty")  # 스택이 비어있는 경우 empty 출력
            return
        return stack[self.top]  # 스택의 가장 위에 있는 원소 반환

    def top_index(self):  # 탑 인덱스 출력 함수
        return [self.top]  # 탑의 인덱스 값을 리턴

    def all_pop(self):  # 값 전부 삭제 함수
        while self.top != -1:  # top이 -1이 아닐동안 반복
            self.pop(self.stack)  # 스택을 팝
            self.top -= 1  # 스택 탑 빼주기

    def stack_print(self):  # 스택 출력
        print(*self.stack)  # 스택 출력문


stack_a = stack()
stack_a.push(1)
stack_a.push(2)
stack_a.push(2)
stack_a.push(2)
stack_a.push(2)
stack_a.stack_print()
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