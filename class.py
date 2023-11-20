class Deque:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.list = [None] * capacity
        self.front = -1
        self.rear = 5  

    def isEmpty(self):
        return self.rear == self.capacity or self.front == -1

    def isFull(self):
        return self.rear - 1 == self.front

    def Addfront(self, e):
        if self.isFull():
            print('full')
            return
        self.front += 1
        self.list[self.front] = e
        print(self.list)

    def Deletefront(self):
        if self.isEmpty():
            print('empty')
            return
        print(self.list[self.front], end=' ')
        self.front -= 1
        print(self.front)

    def Getfront(self):
        print(self.list[self.front])

    def Addrear(self, e):
        if self.isFull():
            print('full')
            return
        self.rear = (self.rear - 1) % self.capacity
        self.list[self.rear] = e
        print(*self.list)

    def Deleterear(self):
        if self.isEmpty():
            print('empty')
            return
        print(self.list[self.rear], end=' ')
        self.rear = (self.rear + 1) % self.capacity
        print(self.rear)

    def Getrear(self):
        print(self.list[self.rear])

a = Deque()
a.Addfront(1)
a.Addrear(2)
a.Addfront(3)
a.Addfront(4)
a.Addrear(5)
a.Addfront(1)
a.Addrear(3)
a.Deletefront()
a.Deletefront()
a.Deleterear()
a.Deleterear()
a.Deleterear()
a.Deletefront()
