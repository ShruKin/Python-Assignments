print("Kinjal Raykarmakar\nSec: CSE2H\tRoll: 29\n")

for i in range(1, 51):
    if i%15 == 0:
        print("FizzBuzz", end=", ")
    elif i%3 == 0:
        print("Fizz", end=", ")
    elif i%5 == 0:
        print("Buzz", end=", ")
    else:
        print(i, end=", ")