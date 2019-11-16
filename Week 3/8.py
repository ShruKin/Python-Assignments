print("Kinjal Raykarmakar\nSec: CSE2H\tRoll: 29\n")

s = input("Enter a string: ")

d = 0
l = 0
for i in s:
    if i.isdigit():
        d+=1
    elif i.isalpha():
        l+=1

print(f'No. of digits = {d} and No. of letters = {l}')