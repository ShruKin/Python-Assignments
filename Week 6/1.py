print("Kinjal Raykarmakar\nSec: CSE2H\tRoll: 29\n")

tup = [('item1', '12.20'), ('item2','15.10' ), ('item3', '24.50') ] 
tup.sort(key = lambda x: float(x[1]), reverse = True)
print(tup)   
