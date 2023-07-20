# d=eval(input("enter the dict:"))
# sum=0
# for item in d.items():
#     sum=sum+item[1]
# print("the sum is :",sum)



# d=eval(input("enter the dict:"))
# print("the sum of values:",sum(d.values()))



# word=input("enter any string:")
# d={}
# for ch in word:
#     d[ch]= d.get(ch,0)+1
# for k,v in d.items():
#     print("the of time:",k ,"occured is :" ,v)     



# word=input("enter the string:")
# vowels={'a','e','i','o','u'}
# d={}
# for ch in word:
#     # if ch in vowels:
#     d[ch]=d.get(ch,0)+1
# for k,v in d.items():
#     print(k,"occured",v,"times")



# n=int(input("enter no of students:"))
# d={}
# for i in range(n):
#     name=input("enter student name:")
#     marks=int(input("enter the marks:"))
#     d[name]=marks
# print("student data insertion completed")
# print('*'* 30)
# print("name", '\t\t','marks')
# print('*' * 30)
# for k,v in d.items():
#     print(k,'\t\t',v)
# print("search operation started")
# while True:
#     name=input("enter student name to get marks")
#     marks=d.get(name,-1)
#     if marks==-1:
#         print("student not found")
#     else:
#         print("marks of ",name,'are',marks)
#     option=input("do you want to find another student marks (yes|no):")
#     if option.lower=='no':
#         break
# print("thanks for using the application")



# d={x:x*x for x in range(1, 11)}
# print(d)



# d={x:2**x for x in range(1, 11)}
# print(d)



# l1=[10,20]
# l2=[20,40]
# l3=l1+l2
# print(l3)
# l3=[*l1,*l2]
# print(l3)  



# t1=(10,20)
# t2=(20,40)
# t3=t1+t2
# print(t3)
# t3=(*t1,*t2)
# print(t3)  



s1={10,20}
s2={30,40,10}
# s3=s1+s2
# print(s3)
s3={*s1,*s2}
print(s3)  