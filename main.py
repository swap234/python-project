

#with open("python.txt",'r') as f:
 # print(f.read())
#f.close()

with open("Javascript.txt",'w') as f:
    f.write("Javascript is also awesome ")
f.write("Javascript is my fav lang")
print(f.read(6))
f.close()