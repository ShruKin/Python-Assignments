print("Kinjal Raykarmakar\nSec: CSE2H\tRoll: 29\n")

print("The absolute value of -8:", abs(-8))

print()

alltrue = [True, True, True]
allfalse = [False, False, False]
onetrue = [True, False, False]
onefalse = [False, True, True]
empty = []
print(all(alltrue), any(alltrue))
print(all(allfalse), any(allfalse))
print(all(onetrue), any(onetrue))
print(all(onefalse), any(onefalse))
print(all(empty), any(empty))

print()

a = ascii("Würzburg")
print(a)

print()

print("The binary equivalent of 16:", bin(16))

print()

print(f"Casting 10 to boolean:", bool(10))

print()

print("Unicode of 38 is", chr(38))

print()

print("Complex number:", complex('1+2j'))
print("Complex number:", complex(2,3))

print()

print("I {} python".format("Love"))

print()

import math

print("Ceil of 3.4:", math.ceil(3.4))

print()

print("Factorial of 8:", math.factorial(8))

print()

print("GCD of 13 and 34:", math.gcd(13, 34))

print()

print("3*(2^3) is:", math.ldexp(3, 3))

print()

import textwrap
text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Vitae ultricies leo integer malesuada nunc vel risus commodo. Facilisis gravida neque convallis a. Elit duis tristique sollicitudin nibh sit amet commodo nulla facilisi. Id interdum velit laoreet id donec ultrices tincidunt arcu non. Justo eget magna fermentum iaculis eu non diam. Urna et pharetra pharetra massa massa ultricies mi quis hendrerit. Rutrum quisque non tellus orci ac auctor augue mauris augue. Iaculis nunc sed augue lacus viverra vitae congue. Augue lacus viverra vitae congue eu consequat. "
wrapper = textwrap.TextWrapper(width=50) 
word_list = wrapper.wrap(text) 
print(word_list)

print()

wrapper = textwrap.TextWrapper(width=50) 
string = wrapper.fill(text) 
print(string)

print()

shortened = textwrap.shorten(text=text, width=100) 
print(shortened)

print()

import statistics
import random
data = list(random.randint(1, 100) for _ in range(10))
print("Data:", data)

print()

print("Mean:", statistics.mean(data))

print()

print("Standard Deviation:", statistics.stdev(data))

print()

print("Grouped Median:", statistics.median_grouped(data))