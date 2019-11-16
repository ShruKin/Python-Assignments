print("Kinjal Raykarmakar\nSec: CSE2H\tRoll: 29\n")

def s_list(l,size):
    return [l[i:i+size] for i in range(0, len(l), size)]

lis=[1,3,4,7,9,8,6,2]
size=int(input("Enter the size: "))
print(s_list(lis,size))
