import math
print("Kinjal Raykarmakar\nSec: CSE2H\tRoll: 29\n")

n = int(input("Enter n: "))
nums = []

for _ in range(0, n, 2):
    row = []
    row.append(int(input()))
    row.append(int(input()))
    nums.append(row)

print(nums)

n = len(nums)
sxy = sx = sy = sxx = syy = 0
for i in nums:
    sx += i[0]
    sxx += i[0] ** 2
    sy += i[1]
    syy += i[1] ** 2

    for j in i:
        sxy += j

r = ((n * sxy) - (sx * sy)) / math.sqrt(((n * sxx) - (sx ** 2)) * ((n * syy) - (sy ** 2)))

print("%.2f" % r)
