queue_size = 5
queue = [None] * queue_size
front = rear = -1

def is_empty():
    return front == rear == -1

def is_full():
    return (rear + 1) % queue_size == front

def enqueue(item):
    global front, rear
    if not is_full():
        if is_empty():
            front = 0
        rear = (rear + 1) % queue_size
        queue[rear] = item
        print(queue)
    else:
        print("Queue is Full")

def dequeue():
    global front, rear
    if not is_empty():
        item = queue[front]
        if front == rear:
            front = rear = -1
        else:
            front = (front + 1) % queue_size
        queue[front - 1] = None  
        print(queue)
        return item
    else:
        print("Queue is Empty")
        return None

def peek():
    if not is_empty():
        return queue[front]
    else:
        print("Queue is Empty")
        return None

enqueue(1)
enqueue(2)
enqueue(3)
enqueue(4)
enqueue(5)
dequeue()
dequeue()
dequeue()
dequeue()
