print("Kinjal Raykarmakar\nSec: CSE2H\tRoll: 29\n")

vowels = ['a', 'e', 'i', 'o', 'u']
alphabets = list(map(chr, range(ord('a'), ord('z')+1)))

consonants = list(filter(lambda x: x not in vowels, alphabets))
print(consonants)