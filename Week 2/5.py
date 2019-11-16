print("Kinjal Raykarmakar\nSec: CSE2H\tRoll: 29\n")
    
cl = int(input("Enter Number of classes held: "))
atd = int(input("Enter Number of classes attended: "))

per = (atd / cl) * 100
print("Percentage of classes attended:", per)

if per > 75:
    print("The student is allowed to sit in the exam")
else:
    print("The student is not allowed to sit in the exam")