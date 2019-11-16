print("Kinjal Raykarmakar\nSec: CSE2H\tRoll: 29\n")

password = input("Enter a password: ")

spc = ['$', '#', '@']
d = list(filter(lambda n: n.isdigit(), password))
u = list(filter(lambda n: n.isupper(), password))
l = list(filter(lambda n: n.islower(), password))
s = list(filter(lambda n: n in spc, password))

if len(password)>6 and len(password)<16 and len(d)>=1 and len(u)>=1 and len(l)>=1 and len(s)>=1:
    print("Password accepted!")
else:
    print("Password rejected! Try agian!")