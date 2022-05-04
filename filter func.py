import functools

a=[1,2,3,4,5]
b=filter(lambda x:x%2==0,a)
print(list(b))
c=[x for x in a if x%2==0]
print(c)
#reduce
from functools import reduce
a=[1,2,3,4,5]
product_a= reduce(lambda x,y:x*y,a)
print(product_a)