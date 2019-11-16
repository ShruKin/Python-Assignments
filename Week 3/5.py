print("Kinjal Raykarmakar\nSec: CSE2H\tRoll: 29\n")

fibo = [0, 1]

f = 0
while True:
    f = fibo[-1] + fibo[-2]
    if f > 50:
        break
    fibo.append(f)
print(fibo)