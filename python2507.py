# def f(arg1,arg2,arg3=4,arg4=8):
#     print(arg1,arg2,arg3,arg4)
# f(3,2)
# f(10,20,30,40)
# f(25,50,arg4=100)
# f(arg4=2,arg1=3,arg2=4) 



# def f(arg1,arg2,arg3=4,arg4=8):
#     print(arg1,arg2,arg3,arg4)
# f()
# f(arg3=10,arg4=20,30,40)
# f(4,5,arg2=6)
# f(4,5,arg3=5,arg5=6) 



# a=100
# def  f1():
#     print(a)
# f1()
# def f2():
#     print(a)
# f2()



# def f1():
#     a=10
#     print(a)
# def f2():
#     print(a)
# f1()
# f2()



# a=10
# def f1():
#     a=20
#     print(a)
# def f2():
#     print(a)
# f1()
# f2()



# a=10
# def f1():
#     a=20
#     print(a)
# def f2():
#     a=30
#     print(a)
# f1()
# f2()



# a=10
# def f1():
#     global a
#     a=20
#     print(a)
# def f2():
#     print(a)
# f1()
# f2()



# a=777
# def f1():
#     print(a)
#     global a
#     a=999
#     print(a)
# f1() 



# a=777
# def f1():
#     global a  
#     print(a)
#     a=999
#     print(a)
# f1() 



# a=888
# def f():
#     a=999
#     print(a)
# f() 



# a=888
# def f():
#     a=999
#     print(a)
#     print(globals().get('a'))
#     print(globals()['a'])
# f() 



# def fact(n):
#     result=1
#     while n>=1:
#         result=result*n
#         n=n-1
#     return result
# print(fact(3))



# def fact(n):
#     if n==0:
#         result=1
#     else:
#         result=n*fact(n-1)
#     return result
# print(fact(6))



# def fact(n):
#     if n==0:
#         result=1
#     else:
#         result=n*fact(n-1)
#     return result
# for i in range(1,11):
#     print("the fact of" , i , "is:",fact(i))



# def fact(n):
#     print("exexution of fact function for n:",n)
#     if n == 0:
#         result=1
#     else:
#         result=n*fact(n-1)
#     print("returning fact ({}) is :{}".format(n,result))    
#     return result
# print(fact(6))



# count=0
# def fact(n):
#     global count
#     count=count+1
#     print("execution of fact function for n:",n)
#     if n == 0:
#         result=1
#     else:
#         result=n*fact(n-1)
#     return result
# print(fact(1000 ))
# print("the no of time fact function executed:",count)



# def  square(n):
#     n=n*n
#     return n
# print(square(3))



# s=lambda n: n*n
# for i in range (1,11):
#     print(i)
#     print(s(i))



# s=lambda a,b: a+b
# print(s(10,20))
# print(s(100,200))



s= lambda a,b : a>b 