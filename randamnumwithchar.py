import string
from random import *
min_char = 8
max_char = 12
allchar = string.ascii_letters + string.digits
invoicenumber=[]
for i in range(0,9):
    j=choice(allchar)
    invoicenumber.append(j)
print(invoicenumber)
password = "".join(choice(allchar) for x in range(randint(min_char, max_char)))
