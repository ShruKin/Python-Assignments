print("Kinjal Raykarmakar\nSec: CSE2H\tRoll: 29\n")

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
 
 
root = Node(1)
root.left = Node(2)
root.right = Node(3)
 
root.left.left = Node(4)