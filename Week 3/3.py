print("Kinjal Raykarmakar\nSec: CSE2H\tRoll: 29\n")

row = int(input("Enter the number of rows: "))

for i in range(1, row+1):
    for j in range(i):
        print("*", end=" ")
    print()

for i in range(row+1, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()