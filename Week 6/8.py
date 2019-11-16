print("Kinjal Raykarmakar\nSec: CSE2H\tRoll: 29\n")

my_enumerate = lambda x :[(t, x[t]) for t in range(len(x))]

li = ['a', 'e', 'i', 'o', 'u']
print(list(my_enumerate(li)))
