# class Employee:
#     def __init__(self):
#         print('Employee created')
#     def __del__(self):
#         print("Destructor called")
  
# def Create_obj():
#     print('Making Object...')
#     obj = Employee()
#     print('function end...')
#     return obj
  
# print('Calling Create_obj() function...')
# obj = Create_obj()
# print('Program End...')




# class Person(object):
#     def __init__(self, name, idnumber):
#         self.name = name
#         self.idnumber = idnumber
 
#     def display(self):
#         print(self.name)
#         print(self.idnumber)
         
#     def details(self):
#         print("My name is {}".format(self.name))
#         print("IdNumber: {}".format(self.idnumber))
# class Employee(Person):
#     def __init__(self, name, idnumber, salary, post):
#         self.salary = salary
#         self.post = post
#         Person.__init__(self, name, idnumber)
         
#     def details(self):
#         print("My name is {}".format(self.name))
#         print("IdNumber: {}".format(self.idnumber))
#         print("Post: {}".format(self.post))
 
# a = Employee('Rahul', 886012, 200000, "Intern")
# a.display()
# a.details()



# class Cal1:  
#     def Sum(self,a,b):  
#         return a+b;  
# class Cal2:  
#     def Multiplication(self,a,b):  
#         return a*b;  
# class Der(Cal1,Cal2):  
#     def Divide(self,a,b):  
#         return a/b;  
# d = Der()  
# print(d.Sum(20,20))  
# print(d.Multiplication(20,20))  
# print(d.Divide(20,20)) 



# class Car:
#     def __init__(self, color, mileage):
#         self.color = color
#         self.mileage = mileage
# blue_car = Car(color="blue", mileage=20_000)
# red_car = Car(color="red", mileage=30_000)
# for car in (blue_car, red_car):
#     print(f"The {car.color} car has {car.mileage:,} miles")



# class employee:
#     def __init__(self,eno,ename,esal):
#         self.eno=eno
#         self.ename=ename
#         self.esal=esal
#     def display(self):
#         print("employee number:",self.eno)
#         print("employee name:",self.ename)
#         print("employee salary:",self.esal)
# class test:
#     def modify(emp):
#         emp.esal=emp.esal+10000
#         emp.display()
# e=employee(126,'hemanth',10000)
# test.modify(e)



# class student:
#     def setName(self,name):
#         self.name=name
    
#     def getName(self):
#         return self.name
    
#     def setMarks(self,marks):
#         self.marks=marks
        
#     def getMarks(self):
#         return self.marks
    
# n=int(input('enter the no students:'))
# for i in range(n):
#     s=student()
#     name=input("enter name:")
#     s.setName(name)
#     marks=int(input("enter marks:"))
#     s.setMarks(marks)
    
# print("hi",s.getName())
# print("your marks are:",s.getMarks())
# print()



# class duck:
#     def talk(self):
#         print("quack.... quack....")
# class dog:
#     def talk(self):
#         print("bow.... bow....")
# class cat:
#     def talk(self):
#         print("meow.... meow....")
# class goat:
#     def talk(self):
#         print("myaah.... myaah....")
# def f1(obj):
#     obj.talk()
    
# i=[duck(),dog(),cat(),goat()]
# for obj in i:
#     f1(obj)



# class test:
#     count=0
#     def __init__(self):
#         test.count=test.count+1
#     @classmethod
#     def noofobj(cls):
#         print("the no of objects created for test class:",cls.count)
# t1=test()
# t2=test()
# t3=test()
# t5=test()
# test.noofobj()
# t4=test()



# import sys
# class customer:
#     ''' customer class with bank operations.. '''
#     bankname="hemanth"
#     def __init__(self,name,balance=0.0):
#         self.name=name
#         self.balance=balance
#     def deposit(self,amt):
#         self.balance=self.balance+amt
#         print("balance after deposit:",self.balance)
#     def withdraw(self,amt):
#         if amt>self.balance:
#             print('insufficient funds.. cannot perform this operation')
#             sys.ext()
#         self.balance=self.balance-amt
#         print("balance after withdraw:",self.balance)

# print('welcome to ' ,customer.bankname)
# name=input('enter your name:')
# c=customer(name)
# while True:
#     print('d-deposit\nw-withdraw\ne-exit')
#     option=input('choose your option:')
#     if option=='d' or option=='D':
#         amt=float(input('enter amount:'))
#         c.deposit(amt)
#     elif option=='w' or option=='W':
#         amt=float(input('enter amount:'))
#         c.withdraw(amt)
#     elif option=='e' or option=='E':
#         print("thanks for banking")
#         sys.exit()
#     else:
#         print('invalid option .. plz choose valid option')



class hemanthmath:
    @staticmethod
    def add(x,y):
        print('the sum :',x+y)
        
    @staticmethod
    def product(x,y):
        print('the product:',x*y)
    
    @staticmethod
    def average(x,y):
        print('the average:',(x+y)/2)
        
hemanthmath.add(10,20)
hemanthmath.product(10,20)
hemanthmath.average(10,20)
hemanthmath.add(20,20)
hemanthmath.product(20,20)
hemanthmath.average(20,20)