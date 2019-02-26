SIZE = 5
Q = [0]*SIZE
front, rear = 0, 0
def isFull():
    global front, rear
    return (rear+1) % len(Q) == front
def isEmpty():
    global front, rear
    return front == rear
def enQueue(item):
    global rear
    if isFull(): print("Queue Full")
    else:
        rear = (rear+1) % len(Q)
        Q[rear] = item
def deQueue():
    global front
    if isEmpty() : print("Queue Empty")
    else:
        front = (front+1)%len(Q)
        return Q[front]

enQueue(1)
enQueue(2)
enQueue(3)
enQueue(4)
enQueue(5)
print(isEmpty())
print(deQueue())
print(deQueue())
print(deQueue())
print(deQueue())
print(deQueue())
print(Q)