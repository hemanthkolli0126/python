# from sys import argv
# print(argv)
# print(argv[0])
# print(argv[1:])
# print(argv[:])


# from sys import argv
# print("the number of command line arguments:",len(argv))
# print("the list of command line arguments:",argv)
# print("command line arguments one by one :")
# for x in argv:
#     print(x)
# print("slice operator result:",argv[1:8])


# from sys import argv
# args=argv[1:]
# sum=0
# for x in args:
#     n=int(x)
#     sum += n
# print("the sum:" ,sum)



# from sys import argv
# print(argv[1])


# from sys import argv
# print(argv[1]+argv[2])



# from sys import argv
# print(int(argv[1])+int(argv[2]))


# from sys import argv
# print(eval(argv[1])+eval(argv[2]))


# from sys import argv
# print(int(argv[1])+int(argv[2]))


# from sys import argv
# print(argv[7:100])


# print("hemanth")
# print()
# print("good evg")
# print("submit")



# print("hello \n hemanth")
# print("hello \t hemanth")


# print("hemanth"*4)



# print("hemanth"+"kolli")
# print("hemanth","kolli")



# a,b,c=10,20,30
# print("the values are:",a,b,c)


# a,b,c=10,20,30
# print(a,b,c)
# print(a,b,c,sep=",")
# print(a,b,c,sep=":")


# print("hello",end=' ')
# print("students",end=' ')
# print("python is",end=' ')
# print("very easy")


# print(10,20,30,40,sep=':',end='...')
# print(50,60,70,80,sep='-')


# l=[10,20,30,40]
# t=(10,20,30,40)
# s={10,20,30,40}
# print(l,end='...')
# print(t,end='...')
# print(s,end='...')
# print(l,t,s)



# a,b,c=10,20,30
# print("a value is %i" %a)
# print("a value is %i and b value is %i" %(a,b))


# name=("hemanth")
# l=[10,20,30,40]
# print("hello this is  %s the list is: %s"  %(name,l) )

# name="hemanth"
# salary=10000
# friend="vishnu"
# print("hello {0} your salary is {1} and your friend {2} is waiting".format(name,salary,friend))
# print("hello {} your salary is {} and your friend {} is waiting".format(name,salary,friend))
# print("hello {2} your salary is {1} and your friend {0} is waiting".format(name,salary,friend))
# print("hello {x} your salary is {y} and your friend {z} is waiting".format(x=name,y=salary,z=friend))


# x=int(input("enter the number:"))
# status= "positive" if  x>0 else "negative"
# print("status:",status)



# x=int(input("enter the number:"))
# status= "even" if (x%2 )==0 else "odd"
# print("given number is :",status)

# # ----------------------------------------------------

# x=int(input("enter the number:"))
# if (x%2 )==0:
#     print("given number is even")
# else:
#     print("given number is odd")
    
    
# n=int(input("no:"))
# if n is n%2 == 1 :
#     print("wired")
# elif  n%2 == 0 and 2<=n<=5:
#     print("Not wired")
# elif  n%2 == 0 and 6>=n<=20:
#     print("wired")
# else:
#     print("wired")   
    
    

n=int(input(""))
if  n%2 != 0 :
    print("wired")
elif  n%2 == 0 and 2<=n<=5:
    print("Not wired")
elif  n%2 == 0 and 6<=n<=20:
    print("wired")
elif n%2 == 0 and n>20:
    print("wired")     
