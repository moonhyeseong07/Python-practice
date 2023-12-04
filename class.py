class CircularDeque:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.list = [None] * capacity
        self.front = -1
        self.rear = -1

    def isEmpty(self):
        return self.front == self.rear == -1

    def isFull(self):
        return (self.rear + 1) % self.capacity == self.front

    def Addfront(self, e):
        if self.isFull():
            print('Deque is full')
            return
        if self.isEmpty():
            self.front = self.rear = 0
        else:
            self.front = (self.front - 1 + self.capacity) % self.capacity
        self.list[self.front] = e
        print(self.list)

    def Deletefront(self):
        if self.isEmpty():
            print('Deque is empty')
            return
        deleted_element = self.list[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity
        print(deleted_element, end=' ')
        print(self.list)

    def Getfront(self):
        if self.isEmpty():
            print('Deque is empty')
        else:
            print(self.list[self.front])

    def Addrear(self, e):
        if self.isFull():
            print('Deque is full')
            return
        if self.isEmpty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.capacity
        self.list[self.rear] = e
        print(self.list)

    def Deleterear(self):
        if self.isEmpty():
            print('Deque is empty')
            return
        deleted_element = self.list[self.rear]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.rear = (self.rear - 1 + self.capacity) % self.capacity
        print(deleted_element, end=' ')
        print(self.list)

    def Getrear(self):
        if self.isEmpty():
            print('Deque is empty')
        else:
            print(self.list[self.rear])

# 테스트
a = CircularDeque()
a.Addfront(1)
a.Deletefront()
a.Addfront(2)
a.Addrear(3)
a.Deleterear()
a.Addrear(4)
a.Addrear(5)
a.Addrear(6)
a.Addrear(7)
a.Addrear(8)



'''class Deque:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.list = [None] * capacity
        self.front = -1
        self.rear = -1

    def isEmpty(self):
        return self.front == self.rear == -1

    def isFull(self):
        return (self.rear + 1) % self.capacity == self.front

    def Addfront(self, e):
        if self.isFull():
            print('Deque is full')
            return
        if self.isEmpty():
            self.front = self.rear = 0
        else:
            self.front = (self.front - 1 + self.capacity) % self.capacity
        self.list[self.front] = e
        print(self.list)

    def Deletefront(self):
        if self.isEmpty():
            print('Deque is empty')
            return
        deleted_element = self.list[self.front]
        if self.front == self.rear:  # 마지막 원소를 삭제하는 경우
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity
        print(deleted_element, end=' ')
        print(self.list)

    def Getfront(self):
        if self.isEmpty():
            print('Deque is empty')
        else:
            print(self.list[self.front])

    def Addrear(self, e):
        if self.isFull():
            print('Deque is full')
            return
        if self.isEmpty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.capacity
        self.list[self.rear] = e
        print(self.list)

    def Deleterear(self):
        if self.isEmpty():
            print('Deque is empty')
            return
        deleted_element = self.list[self.rear]
        if self.front == self.rear:  # 마지막 원소를 삭제하는 경우
            self.front = self.rear = -1
        else:
            self.rear = (self.rear - 1 + self.capacity) % self.capacity
        print(deleted_element, end=' ')
        print(self.list)

    def Getrear(self):
        if self.isEmpty():
            print('Deque is empty')
        else:
            print(self.list[self.rear])

a = Deque()
a.Addfront(1)
a.Deletefront()
a.Deletefront()'''