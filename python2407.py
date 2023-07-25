# a=20
# b=10
# print("the sum:",a+b)
# print("the difference:",a-b)
# print("the product:",a*b)



# a=200
# b=100
# print("the sum:",a+b)
# print("the difference:",a-b)
# print("the product:",a*b)



# a=2000
# b=1000
# print("the sum:",a+b)
# print("the difference:",a-b)
# print("the product:",a*b)



# x=int(input("enter the first no:"))
# y=int(input("enter the second no:"))
# print("the sum:",x+y)
# print("the difference:",x-y)
# print("the product:",x*y)



# def calculate(a,b):
#     print("the sum:",a+b)
#     print("the difference:",a-b)
#     print("the product:",a*b)
# calculate(20,10)
# calculate(200,100)
# calculate(2000,1000)



# def wish():
#     print("hello friend good evening")
# wish()
# wish()
# wish()



# def wish(name):
#     print("hello" , name , "good evening")
# wish("hemanth") 



# def sqrt(num):
#     sq=num*num
#     print('the square of {} is {}' .format(num,sq))
# sqrt(2)
# sqrt(3)
# sqrt(4)   



# def add(a,b):
#     sum=a+b
#     return sum 
# result=add(10,20)
# print("the sum:",result)
# print("the sum:",add(100,200))



# def f1():
#     print("hello")
# x=f1() 
# print('the return value:',x) 



# def fact(num):
#     result=1
#     while num >= 1:
#         result=result*num
#         num=num-1
#     return result
# for i in range(1,6):
#     print("the factorial of ",i,"is",fact(i))
# print("the factorial of 3 is :",fact(3))
# print("the factorial of 4 is :",fact(4))



# def sum_sub(a,b):
#     sum=a+b
#     sub=a-b
#     return sum,sub
# x,y=sum_sub(20,10)
# print("the sum:",x)
# print("the sub:",y)



# def cal(a,b):
#     sum=a+b
#     sub=a-b
#     multi=a*b
#     div=a/b
#     return sum,sub,multi,div
# t=cal(20,10)
# print(type(t))
# print(t)
# for x in t:
#     print(x)



# def f1(a,b):
#     print(a+b)
# f1(20,10 )



# def sub(a,b):
#     print(a-b)
# sub(200,100)
# sub(100,200)
# sub(100)



# def sub(a,b):
#     print(a-b)
# sub(200,100)
# sub(a=100,b=200)
# sub(a=100,b=200)
# sub(a=100)



# def sub(a,b):
#     print(a-b)
# sub(a=100,b=200)
# sub(100,200)
# sub(200,b=100)



# def wish(name='guest'):
#     print("hello",name,"good morning") 
# wish()
# wish("hemanth")



# def wish(name,msg):
#     pass



# def wish(name='hemanth',msg='good morning'):
#     pass



# def wish(name,msg='good morning'):
#     pass



# def f1(*n):
#     print('variable length argument function')
#     print(type(n))
#     print(n)
# f1()
# f1(10)
# f1(10,20,30,40)



# def sum(*n):
#     total=0
#     for x in n:
#         total=total+x
#     print("the sum:",total)
# sum()
# sum(10)
# sum(10,20)
# sum(10,20,30)
# sum(10,20,30,40)



# def f1(*n):
#     print(n)
# f1(10,20)
# f1((10,20,30),(40,50,60))



# def f1(x,*y):
#     print(x)
#     print(y)
# f1(10,20,30,40)
# f1(10)
# f1()



# def f1(*x,y):
#     print(x)
#     print(y)
# f1(10,20,30,40,y=60)


def f1(*x,*y):
    print(x)
    print(y)
f1(10,20,30,40,y=40,50,60)
