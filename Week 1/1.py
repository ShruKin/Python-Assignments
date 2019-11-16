import math

print("Kinjal Raykarmakar\nSec: CSE2H\tRoll: 29\n")

N = int(input("Enter the kilometers per day(N): "))
M = int(input("Enter the total route length(M): "))

print("The car will take {} days".format(math.ceil(M/N)))