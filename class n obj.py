class person:
    pass
class Person:
 def name(self):
  print("Function inside the class")

 def roll_no(self):
   print("Second function in the class")

obj=Person()
obj.name()
obj.roll_no()

class Parent:
    pass
class Parent:
    def house(self):
        print("It is asset")
    def car(self):
        print("It is liability")
class child():
    def bike(self):
        print("It is good")
obj=Parent()
obj.car()
obj.house()


class Student:
    pass

student1=Student()
student1.name="John"
student1.marks=78

print(student1.name)
print(student1.marks)