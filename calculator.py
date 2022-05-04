# calculator function
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mult(a,b):
    return a*b
def div(a,b):
    return a/b
print("please select operation")
select=int(input("Select operations from 1,2,3,4:"))

a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
if select==1:
    print(a,"+",b,"=", add(a,b))
elif select==2:
    print(a,"-",b,"=", sub(a,b))
elif select==3:
    print(a,"*",b,"=", mult(a,b))
elif select==4:
    print(a,"/",b,"=", div(a,b))
else:
    print("Invalid input")