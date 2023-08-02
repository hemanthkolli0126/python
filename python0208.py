# class test :
#     def __init__(self):
#         self.a=10
#         self.b=20
# t=test()
# print(t.__dict__)



# class test:
#     def __init__(self):
#         self.a=10
#         self.b=20
#     def m1(self):
#         self.c=30
#         self.d=40
# t=test()
# t.m1()
# print(t.__dict__)



# class test:
#     def __init__(self):
#         self.a=10
#         self.b=20
#     def m1(self):
#         self.c=30
# t=test()
# t.m1()
# t.d=40
# print(t.__dict__)



# class test:
#     def __init__(self):
#         self.a=10
#         self.b=20
#     def m1(self):
#         self.c=30
# t1=test()
# t1.m1()
# t1.d=40
# t2=test()
# print(t1.__dict__)
# print(t2.__dict__)




# class test:
#     def __init__(self):
#         self.a=10
#         self.b=20
#     def display(self):
#         print(self.a)
#         print(self.b)
# t=test()
# t.display()
# print(t.a)
# print(t.b)



# class test:
#     def __init__(self):
#         self.a=10
#         self.b=20
#     def display(self):
#         print(self.a)
#         print(self.b)
# t=test()
# t.display()
# del t.a
# t.display()



# class test:
#     def __init__(self):
#         self.a=10
#         self.b=20
#         self.c=30
#         self.d=40
#     def m1(self):
#         del self.c
# t=test()
# t.m1()
# del t.a
# print(t.__dict__)
# t.__init__()



# class test:
#     def __init__(self):
#         self.a=10
#         self.b=20
# t1=test()
# t1.a=888
# t1.b=999
# t2=test()
# print("t1:",t1.a,t1.b)
# print("t2:",t2.a,t2.b)



# class student:
#     school_name="sri chaitanya techno school"
#     def __init__(self,name,rollno):
#         self.name=name
#         self.rollno=rollno
#     def talk(self):
#         print("name:",self.name)
#         print("rollno:",self.rollno)
#         print("schoolname:",student.school_name)
# t=student("hemanth",126)
# t.talk()



# class test:
#     a=10 
# t=test()
# print(test.__dict__)



# class test:
#     a=10
#     def __init__(self):
#         test.b=20
#     def m1(self): 
#         test.c=30
# t=test()
# t.m1()
# print(test.__dict__)



# class test:
#     a=10
#     def __init__(self):
#         print(self.a)
#         print(test.a)
# t=test()



class test:
    a=10
    def __init__(self):
        print(self.a)
        print(test.a)
    def m1(delf):
        print(delf.a)
        print(test.a)
    @classmethod
    def m2(cls):
        print(cls.a)
        print(test.a)
    @staticmethod
    def m3():
        print(test.a)
t=test()
t.m1()
test.m2()
test.m3()
print(t.a)
print(test.a)


