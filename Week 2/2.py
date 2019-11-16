print("Kinjal Raykarmakar\nSec: CSE2H\tRoll: 29\n")
    
unit = 100
print("Cost of one unit is:", unit)

qty = int(input("Enter quantity: "))

cost = qty * unit
if cost > 1000:
    cost = 0.9 * cost

print("Cost:", cost)