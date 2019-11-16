print("Kinjal Raykarmakar\nSec: CSE2H\tRoll: 29\n")

items = []

n = int(input("Enter number of elements: "))

for _ in range(n):
    items.append(int(input("Enter: ")))

print(f"Original list: {items}")

print(f"After removing duplicate elements: {list(set(items))}")