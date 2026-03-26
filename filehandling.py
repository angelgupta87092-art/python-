f= open("list.py","r")
data= f.read()
print(data)
print(type(data))
f.close()

f2= open("list.py","r")
data=f2.read(3)
print(data)
f2.close()

f3= open("list.py","r")
data=f3.readlines(3)
print(data)
f3.close()


# with open("new.py", "r") as f4:
#     data=f4.read()
#     print(data)

#import os
#os.remove("new.py")#for removing file 

with open("demo.txt","w") as fl:
    fl.write("hey everyone.\n i am angel")
    

with open ("demo.txt","r") as fs:
    data=fs.read()
    print(data)

ftell= open("demo.txt","r")
print(ftell.tell())
data=ftell.read(3)
print(data)
print(ftell.tell())
data=ftell.read()
print(data)
print(ftell.tell())

ftell.seek(5)
data=ftell.read()
print(data)

