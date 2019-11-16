print("Kinjal Raykarmakar\nSec: CSE2H\tRoll: 29\n")

class Stack:
    def __init__(self):
        self.data = []

    def push(self, d):
        self.data.append(d)

    def pop(self):
        return self.data.pop()
    
    def peek(self):
        return self.data[-1]

    def display(self):
        print(list(reversed(self.data)))

s = Stack()

s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)

s.display()

s.pop()
s.pop()

s.display()

print(s.peek())