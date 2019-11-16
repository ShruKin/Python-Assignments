print('Name: Kinjal raykarmakar\nCSE2H\tRoll No.: 29\n')

f = open('amazon.csv', 'r')
f2 = open('text.txt', 'w')
f2.writelines(f.readlines())