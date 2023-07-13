# l=[]
# l.append(10)
# l.append(20)
# l.append(30)
# print(l)
# l.append(40)
# print(l)



# l=[]
# for x in range(1,101):
#     if x % 10 == 0:
#         l.append(x)
# print(l)



# l=[10,20,30,40,]
# l.insert(0,200)
# print(l)



# l=[10,20,30,40,]
# l.insert(100,2)
# print(l)




# l=[10,20,30,40,]
# l.insert(-100,2)
# print(l)



# l1=[10,20,30,40,]
# l2=[50,60,70,80,]
# l1.extend(l2)
# print(l1)
# l2.extend(l1)
# print(l2)



# l1=[10,20,30]
# l2=[50,60]
# l1.append(l2)
# print(l1)
# print(len(l1))



# l1=[10,20,30]
# l2=[50,60]
# l1.extend(l2)
# print(l1)
# print(len(l1))



# l1=[10,20,30]
# l1.append('ABC')
# print(l1)
# print(len(l1))



# l1=[10,20,30]
# l1.extend('ABC')
# print(l1)
# print(len(l1))



# l1=[10,10,20,30]
# l1.remove(10)
# print(l1)



# l1=[10,10,20,30]
# l1.remove(40)
# print(l1)



# l=[1,2,3,4,5,6,]
# print('before removal:',l)
# x=int(input("enter the element to remove:"))
# if x in l :
#     l.remove(x)
#     print("after removal:",l)
# else:
#     print(x,"not present in list")



# l=[1,1,1,1,2,2,2,3,3]
# x=int(input("enter the element to remove:"))
# while True:
#     if x in l:
#         l.remove(x)
#     else:
#         break
# print("after removal:",l)



# l=[10,20,30]
# print(l.pop())
# print(l)



# l=[10,20,30]
# print(l.pop())
# print(l)
# print(l.pop())
# print(l)
# print(l.pop())
# print(l)
# print(l.pop())
# print(l)\
    
    
    
# l=[10,20,30,40,50]
# l.pop(0)
# print(l)



# l=[10,20,30,40,50]
# l.pop(-1)
# print(l)



# l=[10,20,30,40,50]
# l.clear()
# print(l)



# l=[10,20,30,40,50]
# l.reverse()
# print(l)


# l=[10,20,30,40,50]
# print("before reversal:",l)
# l.reverse()
# print("after reversal:",l)



# l=[10,20,30,40]
# r=reversed(l)
# l1=list(r)
# print(l1)
    


# s="hemanth"
# r=reversed(s)
# print(r)
# for x in r :
#     print(x)



# l=[3,5,2,8]
# print("before sorting:",l)
# l.sort()
# print("after sorting:",l)



# l=['z','a','v','b']
# print("before sorting:",l)
# l.sort()
# print("after sorting:",l)



# l=["banana","apple","cat"]
# l.sort()
# print(l)



# l=[20,5,15,10,5]
# l.sort(reverse=True)
# print(l)



# l=["mango","apple","banana"]
# l.sort(reverse=True)
# print(l)



# l=[40,20,'b','a']
# l.sort()
# print()



# l1=[10,20,30,40]
# l2=l1
# l1[1]=777
# print(l1)
# print(l2)
# print(id(l1))
# print(id(l2))
# print(l1 is l2)



# l1=[10,20,30,40]
# l2=l1[::]
# print(id(l1))
# print(id(l2))
# print(l1 is l2)
# print(l1 is not l2)



# l1=[10,20,30,40]
# l2=l1[::]
# l1[1]=9999
# print("l1:",l1)
# print("l2:",l2)



# l1=[10,20,30,40]
# l2=l1.copy()
# print(l1)
# print(l2)
# print(id(l1))
# print(id(l2))



# l=[10,20,[30,40]]
# print(l[0])
# print(l[1])
# print(l[2])
# print(l[2][0])
# print(l[2][1])



# l=[[10,20,30],[40,50,60],[70,80,90]]
# print(l)
# print("elements row wise:")
# for x in l:
#     print(x)
# print("elements in matrix style")
# for x in l:
#     for y in x:
#         print(y,end=" ")
#     print()



# l=[1,2,3,4,5,6,7,8,9,10]



# l=[]
# for i in range (1,11):
#     l.append(i)
# print(l)



# l=[x for x in range(1,11)]
# print(l)



# l=[x*x for x in range(1,11)]
# print(l)


# l=[2**x for x in range(1,6)]
# print(l)



# l=[x  for x in range(1,101) if x % 10 == 0]
# print(l)



# l1=[10,20,30,40]
# l2=[30,40,50,60]
# l3=[x for x in l1 if x not in l2]
# print(l3)



l1=[10,20,30,40]
l2=[30,40,50,60]
l3=[x for x in l1 if x in l2]
print(l3)

















