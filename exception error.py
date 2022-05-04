numerator=10
denominator=0
print(numerator/denominator)

my_list=[1,2,3]
i=int(input("Enter index: "))
print(my_list[i])
except ZeroDivisionError:
   print("denominator cannot be zero")
except IndexError:
  print("Index is wrong")
  print("Program ends")