print("Kinjal Raykarmakar\nSec: CSE2H\tRoll: 29\n")

import os
def extsort(files):
    return sorted(files,key=lambda x: os.path.splitext(x)[1])
print(extsort(['a.c','a.py','b.py','bar.txr','foo.txt','x.c']))
