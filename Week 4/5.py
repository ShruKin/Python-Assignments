print("Kinjal Raykarmakar\nSec: CSE2H\tRoll: 29\n")

def foo():
    i = 1
    f = 1.4
    c = 'P'
    s = "Python"
    b = True

print("The function 'foo' has {} local variables".format(foo.__code__.co_nlocals))