message="how are you?"
def greet():
 print(message)
greet()

mult=lambda x,y:x*y
print(mult(5,7))
#sorted method:
points2D=[(2,3),(15,1),(5,-1),(10,4)]
points2D_sorted=lambda(x:x[0]+x[1])
print(points2D)
print(points2D_sorted)
#maping method:
a=[1,2,3,4,5]
b=map(lambda x:x*4,a)
print(b)
print(list(b))