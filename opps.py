class Student:
    name = " angel"

s1 = Student()
print(s1.name)


class Student2:
    
    def __init__(self,name):#this is a constructor
        self.name=name 
        print("this is a program")#this message will print if the class is called

s1 = Student2("ashii")
print(s1.name)
    
#question 

class Student3:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def get_avg(self):
        sum=0
        for i in self.marks:
            sum += i
        print(f"hii {self.name}ur avg marks is",sum/3)
            
            

s3= Student3("angell",[40,89,68])
print(s3.name,s3.marks)
s3.get_avg()

#question 
class Account:

    def __init__(self,balance ,acc_no):
        self.balance=balance
        self.acc_no=acc_no

    def debit(self,amount):
        self.balance -= amount
        print(amount,"debited from ur account")
        print("total balance = ",self.get_balance())

    def credit (self,amount):
        self.balance += amount
        print(amount,"credited to ur account")
        print("total balance=",self.get_balance())

    def get_balance(self):
        return self.balance
    
acc1=Account(56000,"ifsc8080")
print(acc1.balance)
acc1.credit(1600)
acc1.debit(7000)

#del keyword-- used for deleting object or object property 
del acc1.balance#deleting object's properties
#print(acc1.balance)

del acc1#deleting entire object


class circle:
    def __init__(self,radius):
        self.radius = radius
    
    def drawcircle(self):
        print("circle drawed")

    def area(self):
        return 3.14 * self.radius**2
    def perimeter (self):
        return 3.14*self.radius*2

c1 = circle(14)
print(c1)
print(c1.area())
print(c1.perimeter())


class employee:
    def __init__(self,role,dept,salary):
        self.role=role
        self.dept=dept
        self.salary=salary

    def show(self):
        print("role=",self.role)
        print("dept=",self.dept)
        print("salary=",self.salary)

class engineer(employee):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__("engineer","it",89000)
    
emp1=employee("accoutant","it",50000)
emp1.show()
e1=engineer("angel",21)
print(e1.name)
print(e1.age)
print(e1.role)


class order:
    def __init__(self,item,price):
        self.item=item
        self.price=price

    def __gt__(self,order2):
        return self.price>order2.price

order1=order("momos",30)
order2=order("jalebi",10)
print(order1>order2)