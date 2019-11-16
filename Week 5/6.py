print("Kinjal Raykarmakar\nSec: CSE2H\tRoll: 29\n")

def checkPrime(n):
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):

            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1

    for p in range(2, n):
        if prime[p]:
            print(p, end=" ")

n = int(input("Enter limit: "))

print("Prime numbers: ")
checkPrime(n)
print("\n")