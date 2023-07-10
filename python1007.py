# s=input("enter the string:")
# n=len(s)
# i=0
# print("in forward direction")
# while i<n:
#     print(s[i],end="")
#     i=i+1
# print()
# print("in backward direction")
# i=n-1
# while i>=0:
#     print(s[i],end="")
#     i=i-1
# print()
# print("in backward direction")
# i=-1
# while i >= n:
#     print(s[i],end="")
#     i=i-1



# s="hemanth"
# print("h" in s)
# print("z" in s)



# s=input("enter the main string:")
# subs=input("enter the sub string too search:")
# if subs in s:
#     print(subs, "is found in string")
# else:
#     print(subs, "is not found in string")



# s = input("enter the first string:")
# s1 = input("enter the second string:")
# if s == s1:
#     print("both strings are same")
# elif s >  s1:
#     print(" s is greater than s1")
# elif s < s1:
#     print("s is less than s1")
# else:
#     print("both strings are not same")



# l1=["a","b","c"]
# l2=["a","b","c"]
# l3=l2
# print(id(l1))
# print(id(l2))
# print(l1 is l2)
# print(l1 == l2)
# print(l2 is l3)



# city=input("enter the city name:")
# if city=="hyderabad":
#     print("hello hyderabadi")
# elif city=="chennai":
#     print("hello vanakkam")
# elif city=="banglore":
#     print("hello kannadiga")
# else:
#     print("enterd city is invalid")



# city = input("enter the city name:")
# scity = city.strip()
# if scity == "hyderabad":
#     print("hello hyderabadi")
# elif scity == "chennai":
#     print("hello vanakkam")
# elif scity == "banglore":
#     print("hello kannadiga")
# else:
#     print("enterd city is invalid")



# city=input("enter the city name:").strip()
# if city=="hyderabad":
#     print("hello hyderabadi")
# elif city=="chennai":
#     print("hello vanakkam")
# elif city=="banglore":
#     print("hello kannadiga")
# else:
#     print("enterd city is invalid")



# s='a b c d b a'
# print(s.find('c'))




# s='abcdba'
# print(s.find('b'))



# s='abcdba'
# print(s.rfind('b'))



# s='abcdba'
# print(s.index('b'))



# s='abcdba'
# print(s.rindex('b'))



# s="ABCDEFGHIJBK"
# print(s.find("B",3,8))
# print(s.find("B",3,11))
# print(s.find("F",3,7))



# mail=input("enter you mail id:")
# try:
#     i=mail.index("@")
#     print("mail id contains @ symbol which is mandatory")
# except ValueError:
#     print("mail id does not contain @ symbol")



s="ABCDEFGHIGKLMN"
print(s.index("B"))
print(s.index("F",2,20))
print(s.index("Z",2,20))


