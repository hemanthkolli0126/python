# class student:
#     '''this is hemanth learning oops'''
#     # variables
#     # methods
# print(student.__doc__)
# # help(student)



# class student:
#     '''hemanth python class'''
#     def  __init__(self):
#         self.name='hemanth'
#         self.rolno=101
#         self.marks=90
#     def talk(self):
#         print('hello iam :',self.name)
#         print('my roll no:',self.rolno)
#         print('my marks are:',self.marks)
# s=student()
# print(s.name)
# print(s.rolno)
# print(s.marks)
# s.talk()



# class student:
#     def __init__(self,name,rollno,marks):
#         self.name=name
#         self.rollno=rollno
#         self.marks=marks
#     def talk(self):
#         print('hello iam :',self.name)
#         print('my roll no:',self.rollno)
#         print('my marks are:',self.marks)
# s1=student('hemanth',101,90)
# s2=student('mani',102,91)
# s1.talk()
# s2.talk()
# print(id(self))
# print(id(s1))



# class test:
#     def __init__(self):
#         print('address of the object:',id(self))
# t=test()
# print(id(t))



# class test:
#     def __init__(self):
#         print('constructer')
#     def m1(self,x):
#         print('x value is:',x)
# t=test()
# t.m1( 2)
# t.m1(4) 



# class student:
#     def __init__(delf,name,rollno,marks):
#         delf.name=name
#         delf.rollno=rollno
#         delf.marks=marks
#     def talk(kelf):
#         print('hello iam :',kelf.name)
#         print('my roll no:',kelf.rollno)
#         print('my marks are:',kelf.marks)
# s1=student('hemanth',101,90)
# s1.talk()



# class test:
#     def __init__(self):
#         print('constructor')
# t1=test() 
# t2=test() 
# t3=test()

  

# class student:
#     def __init__(self,name,rollno,marks):
#         print('creating instance variables')
#         self.name=name
#         self.rollno=rollno
#         self.marks=marks
# s1=student('hemanth',101,90)
# print(s1.name,s1.rollno,s1.marks)
# s2=student('manisha',102,91)
# print(s2.name,s2.rollno,s2.marks)



# class test:
#     def m1(self):
#         print("method")
# t=test()
# t.m1()



class test:
    def __init__(self):
        print("construtor execution")
t=test()
t.__init__()
t.__init__()
t.__init__()
t.__init__()