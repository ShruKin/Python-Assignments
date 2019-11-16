print("Kinjal Raykarmakar\nSec: CSE2H\tRoll: 29\n")

def compare(list1, list2):
    for i in list1:
        if i in list2:
            return True


l1 = l2 = []
n1 = int(input("Enter list1 length: "))
n2 = int(input("Enter list2 length: "))

print("Enter list1: ")
for _ in range(n1):
    l1.append(int(input()))

print("Enter list2: ")
for _ in range(n2):
    l2.append(int(input()))

if compare(l1, l2):
    print("Common element present")
else:
    print("No common element present")
