print("Kinjal Raykarmakar\nSec: CSE2H\tRoll: 29\n")

import math

print("Enter numbers (space seperated)")
num = list(map(int, input().split()))

for i in num:
    print(math.factorial(i), end=', ')