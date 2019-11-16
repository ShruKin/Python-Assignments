print("Kinjal Raykarmakar\nSec: CSE2H\tRoll: 29\n")

s = input("Enter a sentence: ").split()

nums = []
for i in s:
    if i.isdigit():
        nums.append(i)

print(nums)

