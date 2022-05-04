#reduce
from functools import reduce
a=[1,2,3,4,5]
product_a= reduce(lambda x,y:x*y,a)
print(product_a)
#factorial
#from functools import reduce
#n=int(input("Enter a number(factorial): "))
#factorialFn=lambda x,y:x*y
#print(reduce(factorialFn,[i for i in range(1,n+1)]))
#sum
#from functools import reduce
#def sum(x,y):
 #   return x+y
#list=(2,4,5,6,7,8)
#print(reduce(sum,list))
#sum
from functools import reduce
list=(3,5,6,7,9)
print(reduce(lambda x,y:x+y,list))

from functools import reduce

vals = [0,1,2,3,4,5,6,7,8,9]
map_obj = map(lambda x: x+1,vals)
map_obj = filter(lambda x: x%2 == 1,map_obj)
map_obj = reduce(lambda x,y: x+y,map_obj,0)
print(map_obj)

l=[1,2,3,4,5]
[x+1 for x in l]