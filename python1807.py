# d={100:'hemanth',200:'navven',300:'kolli'}
# print(d[100])
# print(d[300])
# print(d[700])



# d={100:'hemanth',200:'navven',300:'kolli'}
# key=eval(input("enter key to find the value:"))
# if key in d:
#     print('the value is:',d[key])
# else:
#     print("key not found")



# d={100:'hemanth',200:'navven',300:'kolli'}
# d[400]="shiva"
# print(d)
# d[100]="sunny"  
# print(d)



# d={100:'hemanth',200:'navven',300:'kolli'}
# del d[200],d[100]
# print(d)



# n=int(input("enter no of students:"))
# d={}
# for i in range(n):
#     name=input("enter the name of the student:")
#     marks=int(input("enter the marks:"))
#     d[name]=marks
# print('*' * 30)
# print('name','\t\t','marks')
# print("*" * 30)
# for name in d:
#     print(name,'\t\t',d[name])



# d1={100:'a',200:'b'}
# d2={300:'c',400:'d'}
# d3=d1 * 3
# d3=d1 + d2 
# print(d3)



# d1={100:'a',200:'b'}
# d2={300:'c',400:'d'}
# print(d1 == d2)
# d3={400:'d',300:'c'}
# print(d2 == d3)



# d1={100:'a',200:'b'}
# d2={300:'c',400:'d'}
# print(d1<d2)
# print(d1>d2)



# d1={100:'a',200:'b'}
# print( 100 in d1)
# print(300 in d1)
# print( 'a' in d1)



# d={100:'hemanth',200:'navven',300:'kolli'}
# print(len(d))



# d={100:'hemanth',200:'navven',300:'kolli'}
# print(d.get(100))
# print(d.get(700))



# d={100:'hemanth',200:'navven',300:'kolli'}
# print(d.get(100,'hemu'))
# print(d.get(700,'guest'))



# d1={100:'a',200:'b'}
# d2={300:'c',400:'d'}
# d1.update(d2)
# print(d1)



# d1={100:'a',200:'b'}
# d2={300:'c',400:'d',100:'hemu'}
# d1.update(d2)
# print(d1)



# d={100: 'a', 200: 'b', 300: 'c', 400: 'd'}
# k=d.keys()
# print(k)
# for key in d.keys():
#     print(key)



# d={100: 'a', 200: 'b', 300: 'c', 400: 'd'}
# v=d.values()
# print(v)
# for value in d.values():
#     print(value)



# d={100: 'a', 200: 'b', 300: 'c', 400: 'd'}
# i=d.items()
# print(i)
# print(type(i))
# for item in d.items():
#     print(item)
# for k,v in d.items():
#     print(k,'....',v)



# d={100: 'a', 200: 'b', 300: 'c', 400: 'd'}
# key=int(input("enter the key to get value:"))
# if key in d:
#     print("the corresponding value:",d.get(key))
# else:
#     print("the specified key is not available")



# d={100: 'a', 200: 'b', 300: 'c', 400: 'd'}
# value=input("enter the value to find key:")
# available=False
# for k,v in d.items():
#     if v == value:
#         print('the key is :',k)
#         available=True
# if available==False:
#     print("the value is not there in the dict")



# d={100: 'a', 200: 'b', 300: 'c', 400: 'd'}
# print(d.pop(100))
# print(d)
# print(d.pop(700))



# d={100: 'a', 200: 'b', 300: 'c', 400: 'd'}
# print(d.pop(100,'zz'))
# print(d)
# print(d.pop(700,"f"))
# print(d)



# d={100: 'a', 200: 'b', 300: 'c', 400: 'd'}
# print(d.popitem())
# print(d.popitem())
# print(d.popitem())
# print(d.popitem())
# print(d)
# print(d.popitem())



# d={100: 'a', 200: 'b', 300: 'c', 400: 'd'}
# d.clear()
# print(d)



# d={100: 'a', 200: 'b', 300: 'c', 400: 'd'}
# print(d.setdefault(500,'e'))
# print(d)
# print(d.setdefault(100,'g'))
# print(d)



d1={100: 'a', 200: 'b', 300: 'c', 400: 'd'}
d2=d1.copy()
print(d2)
d1[500]='e'
print(d1)
print(d2)