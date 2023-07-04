# x=int(input("enter the number:"))
# while x<=10:
#     print(x)
#     x+=1


# x=int(input("enter the number:"))
# sum=0
# i=1
# while i <=x:
#     sum=sum+i
#     i+=1
# print("the sum of first",x,"numbers is:",sum)
    
 
 
             #  differnet Indentation


# x=int(input("enter the number:"))
# sum=0
# i=1
# while i <=x:
#     sum=sum+i
#     i+=1
#     print("the sum of first",x,"numbers is:",sum)



# name=""
# while name!="hemanth":
#     name=input("enter the name ")
# print("hello hemanth good morning")



# x=input("enter the name:")
# if x == "hemanth":
#     print("welcome hemanth")
# elif x != "hemanth":
#     print("enter the name again")




# name=""
# password=""
# while (name!="hemanth")  and  (password!="kolli"):
#     name=input("enter the name: ")
#     password=input("enter the password: ")
# print("thanks for the correct details")



# i=0
# while True:
#     i=i+1
#     print("hello",i)



# i=0
# while False:
#     i=i+1
#     print("hello",i)



# for i in range (4):
#     for j in range(4):
#         print("i={} and j={}".format(i,j))



# x=int(input("enter the row:"))
# for i in range (1,x+1):
#     for j in range(1,i+1):
#         print("*",end="")
#     print()




# x=int(input("enter the row:"))
# for i in range (1,x+1):
#     for j in range(i):
#         print("*",end="")
#     print()



# x=int(input("enter the no:"))
# for i in range(x):
#     print("*"* x )



# x=int(input("enter the no:"))
# for i in range(x):
#     for j in range(x):
#         print("x",end=" ")
#     print()    



# x=int(input("enter the no of rows:"))
# for i in range(1,x+1):
#     print("*"*i)



# for i in range(6):
#     for j in range(i):
#         print("* "*i )
#     print()\
    
    

# x=int(input("enter the number:"))
# for i in range(1,x+1):
#     for j in range(1,i+1):
#         print(j , end="")
#     print()   



# i=0
# while True:
#     print("hello")
#     i+=1
#     if i == 5:
#         break




# for i in range(10):
#     if i == 7:
#         print("process is enough break")
#         break
#     print(i)    



# l=eval(input("enter the list:"))
# for i in l:
#     if i>500:
#         print("sorry we cant process this order")
#         break
#     print("processing",i)



# for i in range(10):
#     if i % 2 == 0:
#         continue
#     print(i)



# cart=[10,20,30,600,60,70,90]
# for item in cart:
#     if item>500:
#         print("sorry we cannot process this item:", item)
#         break
#     print("processing item :", item)



# cart=[10,20,30,600,60,70,90]
# for item in cart:
#     if item>500:
#         print("sorry we cannot process this item:", item)
#         continue
#     print("processing item :", item)
    
    

# numbers=[10,20,0,5,0,30]
# for n in numbers:
#     if n == 0:
#         print("not divisable")
#         continue
#     print("100/{}={}".format(n,100/n))
   


# cart=[10,20,30,60,70,90]
# for item in cart:
#     if item>500:
#         print("sorry we cannot process this item:", item)
#         break
#     print("processing item :", item)
# else:
#     print("congrats all items are processed")



cart=[10,20,30,600,70,90]
for item in cart:
    if item>500:
        print("sorry we cannot process this item:", item)
        break
    print("processing item :", item)
else:
    print("congrats all items are processed")