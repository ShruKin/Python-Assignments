print("Kinjal Raykarmakar\nSec: CSE2H\tRoll: 29\n")

def create_2d_list(row, col):
    return [[None for i in range(col)] for j in range(row)]

row_num = int(input("Input number of rows: "))
col_num = int(input("Input number of columns: "))

list_2d = create_2d_list(row_num, col_num)
print(list_2d)