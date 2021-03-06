class my_Queue:

    def __init__(self, size=100):
        self.size = size
        self.Q = [0] * size
        self.front, self.rear = -1, -1

    def enQueue(self, item):
        if self.Full(): print("Q is Full!")
        else:
            self.rear += 1
            self.Q[self.rear] = item

    def deQueue(self):
        if self.isEmpty(): print("Q is Empty!!")
        else:
            self.front += 1
            return self.Q[self.front]

    def Qpeek(self):
        if self.isEmpty(): print("Q is Empty!")
        else:
            return self.Q[self.front+1]

    def isEmpty(self):
        return self.front==self.rear

    def Full(self):
        return self.rear == self.size-1

myQ = my_Queue(100)
myQ.enQueue(1)
myQ.enQueue(2)
myQ.enQueue(3)
print(myQ.Qpeek())
print(myQ.deQueue())
print(myQ.deQueue())
print(myQ.deQueue())
print(myQ.deQueue())
