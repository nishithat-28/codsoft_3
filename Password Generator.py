from random import *
from string import *

n=int(input("Enter the length of your password: "))
print()
s=ascii_letters+digits+punctuation
l=[i for i in s]
shuffle(l)
p=sample(l,n)
password="".join(p)

print("Your Password: {}\n".format(password))
