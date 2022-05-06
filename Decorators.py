#Decorators=>pass functions as arguments
def func1(name):
    return f"{name},Hi"
def func2(name):
    return f"{name},How are you?"
def func3(func4):
    return func4('Hello all')
print(func3(func1))
print(func3(func2))

def inc(x):
    return x+1
def operate(func,x):
    return func(x)
print(operate(inc,5))

#Nested Functions:
def func():
    print("first function")
def func1():
    print("First Person")
def func2():
    print("Second Person")
func1()
func2()
func()

#Decorators:
def printer():
    print("Welcome")
def display_info(func):
    def wrapper():
        print("Executing",func,__name__,"function")
        func()
        print("Finished execution")
    return wrapper()
decorated_func=display_info(printer)
decorated_func()