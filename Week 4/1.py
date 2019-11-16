print("Kinjal Raykarmakar\nSec: CSE2H\tRoll: 29\n")

def c_to_f(val):
    return (val * (9/5)) + 32

def f_to_c(val):
    return (val - 32) * (5/9)

print("Enter temperature ending with c/f coressponding to Celsius/Fahrenheit respectively")
t = input("Temperature: ")

if t[-1] == 'c' or t[-1] == 'C':
    temp = float(t[:-1])
    print(f"Converted {temp} to Fahrenheit: {c_to_f(temp)}f")

elif t[-1] == 'f' or t[-1] == 'F':
    temp = float(t[:-1])
    print(f"Converted {temp} to Celsius: {f_to_c(temp)}c")

else:
    print("Invalid input!")