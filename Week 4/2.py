print("Kinjal Raykarmakar\nSec: CSE2H\tRoll: 29\n")

def count_upp_low(string):
    u, l = 0, 0

    for i in string:
        if i.isupper():
            u += 1
        elif i.islower():
            l += 1

    return (u, l)

s = input("Enter a string: ")
upper, lower = count_upp_low(s)

print(f"There are {upper} upper case and {lower} lower case characters")