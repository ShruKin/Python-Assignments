print("Kinjal Raykarmakar\nSec: CSE2H\tRoll: 29\n")

numlist = []
n = int(input("Enter number of elements: "))

print("Enter numbers to list: ")

for _ in range(n):
    numlist.append(int(input()))

num = int(''.join(map(str, numlist)))

print(f"Output: {num}")