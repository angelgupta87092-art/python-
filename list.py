mylist= [10,78,'m']
print(mylist)

mylist.append(56)
print(mylist)

mylist.insert(2,900)
print(mylist)

mylist.pop(4)
print(mylist)

mylist.remove(78)
print(mylist)

newlist=[10,20,30,40]
print(newlist)

#newlist.reverse()
#print(newlist)

newlist.append(3)
newlist.append(34)
print(newlist)
newlist.sort()
print(newlist)

newlist.sort(reverse=True)
print(newlist)

#list problem 

def sum():
    lst=[]
    user=int(input("enter the no. of element="))
    for i in range(user):
        choice= int(input(f"enter element{i}"))
        lst.append(choice)

    total = 0
    for i in range (len(lst)):
        total= total +lst[i]
    
sum()