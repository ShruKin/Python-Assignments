print("Kinjal Raykarmakar\nSec: CSE2H\tRoll: 29\n")

def mutate(s):
    words = set()
    alphabets = list(map(chr, range(ord('a'), ord('z')+1)))

    for i in range(len(s)):
        for a in alphabets:
            words.add(s[:i] + a + s[i:]) #   inserting character
    
    for i in range(len(s)):
        words.add(s[:i] + s[i+1:])   #   deleting character
        for a in alphabets:
            words.add(s[:i] + a + s[i+1:])   #   replacing character

    for i in range(len(s)-1):
        words.add(s[:i] + s[i+1] + s[i] + s[i+2:])

    return words

def nearly_equal(a, b):
    return a in mutate(b)
    
words = mutate('hello')

print(nearly_equal('python', 'perl'))
print(nearly_equal('perl', 'pearl'))
print(nearly_equal('python', 'jython'))
print(nearly_equal('man', 'woman'))
