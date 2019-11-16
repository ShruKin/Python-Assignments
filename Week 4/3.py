print("Kinjal Raykarmakar\nSec: CSE2H\tRoll: 29\n")

def isperfect(num):
    sum = 0
    for i in range(1, num):
        if(num % i == 0):
            sum += i

    if sum == num:
        return True
    else:
        return False


n = int(input("Enter a number: "))

if isperfect(n):
    print(f"{n} is a perfect number")
else:
    print(f"{n} is not a perfect number")