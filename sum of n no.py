n=int(input("Enter a number: "))
sum=0
while (n>0):
    sum=sum+n
    n=n-1
print("Sum of natural numbers is: ",sum)
#sum using recursion:
def recur_sum(n):
    if n<=1:
        return n
    else:
        return n+recur_sum(n-1)
num=10
if num<0:
    print("Enter a positive number")
else:
    print("sum of natural numbers", recur_sum(num))