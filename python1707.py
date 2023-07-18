# s={}
# print(type(s))


# s={10,20,30,40}
# print(type(s))


# s=set()
# s.add(10)
# s.add("a")
# s.add("z")
# s.add(20)
# s.add(10)
# print(s)
# s.remove("z")
# print(s)
# print(type(s))


# l=[10,20,30,40]
# s=set(l)
# print(s)
# print(type(s))


# s=set(range(0,20))
# print(s)


# s=set('apple')
# print(s )


# s=eval(input("enter set of values:"))
# print(s)


# s1={10,20,30,40}
# s2={50,60,70,80}
# s3=s1.union(s2)
# print(s3)


# s1={10,20,30,40}
# s2={20,10,40,30}
# print(s1==s2)
# print(s1!=s2)


# s1={10,20,30}
# s2={20,10,5,6,7}
# print(s1>s2)
# print(s1<s2)
# print(s1<=s2)
# print(s1>=s2)


# s1={10,20,30}
# print(10 in s1)
# print(50 in s1)
# print(10 not in s1)
# print(50 not in s1)


# s1={10,20,30}
# print(len(s1))
# s1.add(100)
# print(s1)


# s1={10,20,30,40,50}
# s2={60,70,80,90,100}
# s1.update(s2)
# print(s1)
# s1.update(range(1,6),"hemanth")
# print(s1)


# s={10,20,30,40}
# s.update(10,20,50)
# print(s)



# s=set()
# s.update(range(1,10,2),range(0,10,2))
# print(s)



# s={10,20,30,40}
# s.remove(10)
# print(s)
# s.remove(50)
# print(s )



# s={10,20,30,40}
# s.discard(30)
# print(s)
# s.discard(50)
# print(s)



# s={10,20,30,40}
# print(s.pop())
# print(s.pop())
# print(s.pop())
# print(s.pop())
# print(s)
# print(s.pop())
# print(s)



# s={10,20,30,40}
# print(s)
# s.clear()
# print(s)



# s1={10,20,30,40,50}
# s2={60,70,80,90,100}
# s3=s1.union(s2)
# print(s3)



# s1={10,20,30,40,50}
# s2={40,50,60,70,80}
# s3=s1.union(s2)
# print(s3)
 
 
 
# s1={10,20,30,40,50}
# s2={40,50,60,70,80}
# s3=s1|s2
# print(s3)



# s1={10,20,30,40,50}
# s2={40,50,60,70,80}
# s3=s1.intersection(s2)
# print(s3)



# s1={10,20,30,40,50}
# s2={40,50,60,70,80}
# s3=s1&s2
# print(s3)



# s1={10,20,30,40,50}
# s2={40,50,60,70,80}
# s3=s1.difference(s2)
# print(s3)



# s1={10,20,30,40,50}
# s2={40,50,60,70,80}
# s3=s2.difference(s1)
# print(s3)



# s1={10,20,30,40,50}
# s2={40,50,60,70,80}
# s3=s2-s1
# print(s3)



# s1={10,20,30,40,50}
# s2={40,50,60,70,80}
# s3=s2.symmetric_difference(s1)
# print(s3)



# s1={10,20,30,40,50}
# s2={40,50,60,70,80}
# s3=s2^s1
# print(s3)



# s1={10,20,30,40,50}
# s2=s1
# s1.pop()
# print(s1)
# print(id(s1))
# print(s2)
# print(id(s1))



# s1={10,20,30,40,50}
# s2=s1.copy()
# s1.pop()
# print(s1)
# print(id(s1))
# print(s2)
# print(id(s2))



# s={x*x for x in range(1,6)}
# print(s)
# print(type(s))



# s={2**x for x in range(1,6)}
# print(s)
# print(type(s))



# l=[1,1,1,2,2,3,4,4,4,5,5,6,6]
# s=set(l)
# print(s)
# l1=list(s)
# print(l1)



# l=[10,10,20,30,10,20,30]
# l1=[]
# for x in l:
#     if x not in l1:
#         l1.append(x)
# print(l1)



# word=input("enter the word:")
# s=set(word)
# v={'a','e','i','o','u'}
# result= s.intersection(v)
# print(result)





# d={100:'hemanth',200:'kolli',300:'hemu'}
# print(d[100])



# d={100:"hemanth","a":300,200:"ravi","b":400,100:"kolli"}
# print(d)



# l=[(100,"a"),(200,"b"),(300,'c')]
# d=dict(l)
# print(d)



# l=([100,"a"],[200,"b"],[300,'c']) 
# d=dict(l)
# print(d)



d=eval(input("enter the dictionary:"))
print(d)
print(type(d))











 
