print("Kinjal Raykarmakar\nSec: CSE2H\tRoll: 29\n")

filename=input("Enter file name: ")
for line in reversed(list(open(filename))):
    print(line.rstrip())
