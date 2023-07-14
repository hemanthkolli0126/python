# t=(10,'hemanth',10,20)
# print(type(t))



# t=10,'hemanth',10,20,20.5
# print(type(t))
# print(t)
# print(t[0])
# print(t[-1])
# t[-1]=10
# print(t)



# n=(2)
# print(type(n))



# t=(10,)
# print(type(t))



# l=[10,20,30,40]
# t=tuple(l)
# print(t)
# print(type(t))



# t=tuple(range(1,11,2))
# print(t)



# t=tuple('hemanth')
# print(t)



# t=eval(input("enter tuple of values:"))
# print(t)
# print(type(t))



# t=(10,20,30,40,50,60)
# print(t[0])
# print(t[-1])
# print(t[100])



# t=(10,20,30,40,50,60,70,80)
# print(t[2:5])



# t1=(10,20,30)
# t2=(40,50,60)
# t3=t1+t2
# print(t3)
# print(t1)
# print(t2)




# t1=(10,20,30)
# t2=(40,50,60)
# t3=t1+t2
# print(t3)
# t3=t1+10
# t3=t1+[10,20]



# t1=(10,20,30)
# t2=t1 * 3
# print(t2)



# t1=(10,20)
# t2=(20,40)
# t3=t1+t2
# t4=t3*3
# print(t4)



# t1=["Dog","Cat","Rat"]
# t2=t"Dog","Cat","Rat"]
# t3=["DOG","CAT","RAT"]
# t4=["Cat","Rat","Dog"]
# print(t1==t2)
# print(t1==t3)
# print(t1==t4)
# print(t1!=t4)




# t1=(10,20,30,40)
# t2=(50,60)
# print(t1<t2)
# print(t1<=t2)
# print(t1>t2)
# print(t1>=t2)



# t1=(10,20,30,40)
# t2=(10,5,60)
# print(t1<t2)
# print(t1<=t2)
# print(t1>t2)
# print(t1>=t2)



# t=(10,20,30)
# print( 10 in t)
# print(50 not in t)
# print(60 in t)



# t=(10,20,30)
# print(len(t))



# t=(10,20,30,10)
# print(t.count(10))



# t=(10,20,30)
# l=t.index(20)
# print(l)



# t=(10,20,30,40)
# r=reversed(t)
# t1=tuple(r)
# print(t)
# print(t1)



# t=(30,40,10,20,150)
# l=sorted(t)
# t1=tuple(l)
# print(t1)



# t=(30,40,10,20,150)
# l=sorted(t,reverse=True)
# t1=tuple(l)
# print(t1)



# t=(10,20,30,0,40,60)
# x=max(t)
# print(x)
# y=min(t)
# print(y)



# a=10
# b=20
# c=30
# d=40
# t=a,b,c,d
# print(t)
# print(type(t))
# l=[a,b,c,d]
# print(l)
# print(type(l))



# t=(10,20,30,40)
# a,b,c = t



# t=(10,20,30,40)
# a, *b = t
# print(a)
# print(b)



# t=(x*x for x in range(1,6))
# print(t)
# print(type(t))



# s={10,20,30,70,80}
# s.add(5)
# print(s)
# t=sorted(s)
# print(t)




# from collections.abc import Hashable

# l=[10,20,30,40]
# t=(10,20,30)
# print(isinstance(l,Hashable))
# print(isinstance(t,Hashable))
# print(hash(t))
# print(hash(l))



# s={10,20}
# l=[10,20,30]
# t=(10,20,30)
# s.add(t)
# print(s)
# s.add(l)
# print(s)



# d={}
# l=[10,20,30]
# t=(10,20,30)
# d[t]="A"
# print(d)
# d[l]="B"
# print("B")



# t=eval(input("enter the tuple  of number:"))
# sum = 0
# for x in t:
#     sum=sum+x
#     print("the sum:",sum)
# print("the average:",sum/len(t))



t=eval(input("enter the tuple  of number:"))
x=sum(t)
y=sum(t)/len(t)
print(x)
print(y)














