from re import *
from random import *
from string import *

n=int(input("Enter the length of your password: "))
print()

l=[i for i in ascii_letters+digits+punctuation]

while True:
    shuffle(l)
    p=sample(l,n)
    password="".join(p)
    if len(password) >= n and any(c.islower() for c in password) and any(c.isupper() for c in password) and any(c.isdigit() for c in password) and any(c in punctuation for c in password) :
        print("Your Password: {}\n".format(password))
        break
