print("Kinjal Raykarmakar\nSec: CSE2H\tRoll: 29\n")
    
print("Enter three ages(space-seperated): ")
age = list(map(int, input().split()))

print("Oldest Age: {} and Yougest Age: {}".format(max(age), min(age)))