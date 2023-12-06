class Queue:
    def __init__(self, size=5):
        self.size = size
        self.list = [None] * size
        self.front = -1
        self.rear = -1

    def isEmpty(self):
        return self.front == self.rear

    def isFull(self):
        return self.rear + 1 == self.size 

    def enqueue(self, e):
        self.e = e
        if self.isFull():
            print("Queue is Full")
        else:
            self.rear = self.rear + 1
            self.list[self.rear] = self.e

    def dequeue(self):
        if self.isEmpty():
            print("Queue is Empty")
        else:
            self.front = self.front + 1
        print(self.list[self.front])
        self.list[self.front] = None

q=Queue()
for i in range(6):
    q.enqueue(i)
    print(q.list)

for i in range(4):
    q.dequeue()
    print(q.list)

print(q.list)