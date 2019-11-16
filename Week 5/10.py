print("Kinjal Raykarmakar\nSec: CSE2H\tRoll: 29\n")

def DiagonalSums(mat, n):
    prin, sec = 0, 0

    for i in range(0, n):
        for j in range(0, n):
            if i == j:
                prin += mat[i][j]

            if (i + j) == (n - 1):
                sec += mat[i][j]

    return (prin, sec)

def print_mat(mat):
    for i in mat:
        for j in i:
            print(j, end=' ')
        print()

tot_n = int(input("Enter n: "))
print("Enter the values: ")

mat = []
n = int(tot_n ** 0.5)
for i in range(n):
    temp = []
    for j in range(n):
        temp.append(int(input()))
    mat.append(temp)

print_mat(mat)

prin, sec = DiagonalSums(mat, n)

if prin == sec:
    print("Sum of Primary Diagonal is equal to Secondary Diagonal")
elif prin > sec:
    print("Sum of Primary Diagonal is more")
else:
    print("Sum of Secondary Diagonal is more")
