print("Kinjal Raykarmakar\nSec: CSE2H\tRoll: 29\n")

lines = []
print("Enter a sequence line: ")
while True:
    line = input()
    if not line:
        break
    else:
        lines.append(line)

for i in lines:
    print(i.lower())