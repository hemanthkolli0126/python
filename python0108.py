# class movie:
#     "this class is developed by hemanth"
#     def __init__(self,title,hero,heroine):
#         self.title=title
#         self.hero=hero
#         self.heroine=heroine
        
#     def info(self):
#         print('Movie name:',self.title)
#         print('Hero name:',self.hero)
#         print('Heroine name:',self.heroine)
# list_of_movies=[]
# while True:
#     title=input("enter movie name:")
#     hero=input("enter hero name:")
#     heroine=input("enter heroine name:")
#     m=movie(title,hero,heroine)
#     list_of_movies.append(m)
#     print("move information added")
#     option=input("do you want to add another movie[Yes|No]:")
#     if option.lower()=='no':
#         break
    
# print("all movies informatiom...")
# for movie in list_of_movies:
#     movie.info()
#     print()



# class test:
#     def test(self):
#         print("method")
# t=test()
# t.test()



# class student:
#     def __init__(self,name,rollno):
#         self.name=name
#         self.rollno=rollno 
# # instance variables



# class student:
#     school_name='techno school'
#     def __init__(self,name,rollno):
#         self.name=name
#         self.rollno=rollno 
# # static variables 



# class student:
#     school_name='techno school'
#     def __init__(self,name,rollno):
#         self.name=name
#         self.rollno=rollno 
#     def info(self):
#         x=10
#         # local variable
#         for i in range(x):
#             print(i)   



# class student:
#     school_name='durgasoft'
#     def __init__(self,name,rollno):
#         self.name=name
#         self.rollno=rollno
#     def getstudentinfo(self):
#         # x=10
#         print('student name:',self.name)
#         print('student rollno:',self.rollno)
#         # print('school name:',student.school_name)
#         # print('school strength:',x)
#     @classmethod
#     def getschoolname(cls):
#         print("school name:",cls.school_name)
# t=student('hemanth',100)
# t.getstudentinfo()
# t.getschoolname()



# class test:
#     @classmethod
#     def m1(cls):
#         print(id(cls))
# print(id(test))
# t=test()
# t.m1()



# class student:
#     school_name='durgasoft'
#     def __init__(self,name,rollno):
#         self.name=name
#         self.rollno=rollno
#     def getstudentinfo(self):
#         # x=10
#         print('student name:',self.name)
#         print('student rollno:',self.rollno)
#     @classmethod
#     def getschoolinfo(cls):
#         print("schoolname is:",cls.school_name)
# t=student('hemanth',100)
# t.getstudentinfo()
# t.getschoolinfo()



class add:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def adding(self):
        a=int(input('enter the number:'))
        b=int(input('enter the number:'))
        sum=a+b
        print("the sum of two no is:",sum)
t=add(10,20)
t.adding()