import string
from random import *
allchar = string.ascii_letters + string.digits
invoice=[]
for i in range(0,9):
    j=choice(allchar)
    invoice.append(j)
joining="".join(invoice)
print(joining)

