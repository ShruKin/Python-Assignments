print("Kinjal Raykarmakar\nSec: CSE2H\tRoll: 29\n")

class Queue:
    def __init__(self):
        self.data = []

    def enqueue(self, d):
        self.data.append(d)

    def dequeue(self):
        return self.data.pop(0)

    def display(self):
        print(self.data)

s = Queue()

s.enqueue(1)
s.enqueue(2)
s.enqueue(3)
s.enqueue(4)
s.enqueue(5)

s.display()

s.dequeue()
s.dequeue()

s.display()
