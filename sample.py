def fact(n):
    if (n <= 1):
        return 1
    else:
        return (n*fact(n-1))
    n=int(input("Enter a number: "))
    print("Factorial of the number is:")
    print(fact(n))

string= 'malayalam'
if (string==string[::-1]):
    print("string is palindrome")
else:
    print("string is not a palindrome")

import platform
print(dir(platform))

import math
print(math)

import random
print(random.randrange(1,10))
mylist=list("ABCDEFG")
print(random.choices(mylist, k=2))
print(random.sample(mylist, k=3))

import functools
help(print)
import math
print(math)

help(matplotlib)
