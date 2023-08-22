# class outer:
#     def __init__(self):
#         print("outer class object creation")
#     class inner:
#         def __init__(self):
#             print("inner class object creation")
#         def m1(self):
#             print("inner class method")
# o=outer()
# i=o.inner()
# i.m1()


# class person:
#     def __init__(self):
#         self.name='hemanth'
#         self.db=self.dob()
#     def display(self):
#         print('name:',self.name)
#     class dob:
#         def __init__(self):
#             self.dd=31
#             self.mm=1
#             self.yy=1999
#         def display(self):
#             print('dob={}/{}/{}'.format(self.dd,self.mm,self.yy))
# p=person()
# p.display()
# x=p.db
# x.display()


# class human:

#     def __init__(self):
#         self.name='hemanth'
#         self.head=self.head()
#         self.brain=self.brain()
#     def display(self):
#         print("hello..",self.name)

#     class head:
#         def talk(self):
#             print("talking")

#     class brain:
#         def think(self):
#             print("thinking")

# t=human()
# t.display()
# t.head.talk()
# t.brain.think()



class Language:
    __country = "america"

    def __init__(self, name):
        self.name = name

    def __show(self):
        print("country:", Language.__country)
        print("name:", self.__name)

    def display(self):
        self.__show()


lang = Language("english")
lang.display()
lang._Language__show()
print("access private name:",lang._Language__name)