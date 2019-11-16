print("Kinjal Raykarmakar\nSec: CSE2H\tRoll: 29\n")

def binomialCoeff(n, k): 
    res = 1
    if (k > n - k): 
        k = n - k 
    for i in range(0 , k): 
        res = res * (n - i) 
        res = res // (i + 1) 
      
    return res 

def printPascal(n): 
    for row in range(0, n): 
        print(" " * (n-row-1), end = "")
        for i in range(0, row + 1): 
            print(binomialCoeff(row, i), "", end = "") 
        print() 

printPascal(5)