print("Kinjal Raykarmakar\nSec: CSE2H\tRoll: 29\n")

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
 
 
def insert(root, node):
    if root is None:
        root = node
    else:
        if root.val < node.val:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)
 
 
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=", ")
        inorder(root.right)
 
 
r = Node(22)
insert(r, Node(44))
insert(r, Node(56))
insert(r, Node(12))
insert(r, Node(3))
insert(r, Node(6))
insert(r, Node(78))
insert(r, Node(49))
insert(r, Node(50))
 
inorder(r)