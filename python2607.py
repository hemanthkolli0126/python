# b= lambda a,b: a if a>b else b
# print(b(10,20))
# print(b(200,100))



# b=lambda a,b,c : a if a>b and a>c else b if b>c else c
# print(b(10,20,30))
# print(b(10,30,20))
# print(b(30,20,10))


# l=[1,2,3,4,5,6,7,8,9,10]
# def even(n):
#     if n%2 == 0:
#         return True
#     else:
#         return False
# l1=[ ]
# for n in l:
#     if even(n)==True:
#         l1.append(n)
# print(l1)
# l2=[ ]
# for n in l:
#     if even(n)==False:
#         l2.append(n)
# print(l2)



# l=[1,2,3,4,5,6,7,8,9,10]
# def even(n):
#     if n%2 == 0:
#         return True
#     else:
#         return False
# l1=list(filter(even,l))
# l2=(tuple(filter(even,l)))
# print(l1)
# print(l2)



# l=[1,2,3,4,5,6,7,8,9,10]
# l1=list(filter(lambda n: n%2==0,l))
# print(l1)



# l=[1,2,3,4,5,6,7,8,9,10]
# even=list(filter(lambda n: n%2==0,l))
# print(even)
# odd=list(filter(lambda n:n%2!=0,l))
# print(odd)
# l1=list(filter(lambda n:n%3==0 and n%2!=0,l))
# print(l1)



# hero=['pk','kalyan','kapoor','teja','vinay','vamsi']
# startwithk=list(filter(lambda name: name[0]=='k' ,hero))
# print(startwithk)



# hero=['pk','kalyan','kapoor','teja','vinay','vamsi']
# s=list(filter(lambda name: len(name)%5==0 ,hero))
# print(s)



# hero=['pk','kalyan','kapoor','teja','vinay','vamsi']
# s=list(filter(lambda name: len(name)%2!=0 ,hero))
# print(s)



# l=[1,2,3,4,5]
# def sq(n):
#     return n*n
# s=list(map(sq,l))
# print(s)



# l=[1,2,3,4,5]
# s=list(map(lambda n:n*n ,l))
# print(s)



# l=[1,2,3,4,5]
# l1=[5,10,15,20,25]
# l2=list(map(lambda x,y:x*y,l,l1))
# print(l2)



# l=[1,2,3,4,5,6,7,8,9,10]
# l1=[5,10,15,20,25]
# l2=list(map(lambda x,y:x*y,l,l1))
# print(l2)


# from functools import reduce
# l=[10,20,30,40,50]
# s=reduce(lambda x,y:x+y,l)
# print(s)



# from functools import reduce
# s=reduce(lambda x,y:x+y,range(1,101))
# print(s)



# import module
# print(module.add(10,20))



# import module as m
# print(m.x)
# print(m.add(10,20))



# from module import *
# print(x)
# print(y)
# print(add(10,20))
# print(product(10,20))



# from module import add as a , product as p
# print(a(10,20))
# print(p(10,20))



# import module
# import module2
# module.add(10,20)
# module2.add(10,20) 



#  from module import add as a1
# from module2 import add as a2
# a1(10,20)
# a2(10,20)



# from imp import reload
# import time
# import modulezyx
# modulezyx.add(10, 20)
# print("enter into sleeping state")
# time.sleep(30)
# print("just woke up... trying to use module again")
# reload( modulezyx )
# modulezyx.product(10,20)




import importlib
import time
import modulezyx
modulezyx.add(10, 20)
print("enter into sleeping state")
time.sleep(30)
print("just woke up... trying to use module again")
importlib.reload(modulezyx)
modulezyx.product(10,20)