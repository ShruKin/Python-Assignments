print("Kinjal Raykarmakar\nSec: CSE2H\tRoll: 29\n")

shallow = [[1, 2], [3, 4], [5, 6]]
flattened = []

print(f"Original list: {shallow}")

for i in shallow:
    for j in i:
        flattened.append(j)

print(f"Flattened list: {flattened}")