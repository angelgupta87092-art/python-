set_1 = {1,2,3,6,5,9}
 
for i in set_1:
    print(i)

if 6 in set_1 : 
    print(" true ")
else : 
    print ("false ")
mylist = list(set_1)
print(mylist[4])

set_1.add(29)
print(set_1)


set_1.update ({78,89})


print(set_1)

set_1.remove(29)
print(set_1)

myset={1,2,3,4}
myset.clear()
print(myset)

set1={1,2,3,4,6,8}
set2={4,3,5}
unionset=set1 | set2
unionset2=set1.union(set2)
print(unionset)
ints=set1.intersection(set2)
print(ints)

difference = set1 - set2
print(difference)# jo first me h second me nhi h 

symdifference = set1 ^ set2
print(symdifference)# common wala ko chor ke sara elemnet deta h 





