print("Kinjal Raykarmakar\nSec: CSE2H\tRoll: 29\n")
    
num = int(input("Enter a number: "))

if (num % 2 != 0) or (num % 2 == 0 and num in range(6, 21)):
    print("Weird")
elif ((num % 2 == 0) and (num in range(2, 6))) or ((num % 2 == 0) and (num > 20)):
    print("Not Weired")