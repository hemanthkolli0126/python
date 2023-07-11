# s="ABBABBABS"
# print(s.count("B"))
# print(s.count("BB"))
# print(s.count("Z"))
# print(s.count("B",4,9))



# s="BBBB"
# print(s.count("B"))
# print(s.count("BB"))
# print(s.count("BBB"))



# s="ABCABCABCA"
# i=s.find('ABC')
# print(i)
# i=s.find('ABC',3,10)
# print(i)
# i=s.find('ABC',6,10)
# print(i)
# i=s.find('ABC',9,10)
# print(i)
# i=s.find('ABC',3,len(s))
# print(i)



# s="ABCABCABCA"
# subs=input('enter the substring to search:')
# i=s.find(subs)
# if i == -1:
#     print("substring not found")
# while i != -1:
#     print('{} present at index:{}'.format(subs,i))
#     i=s.find(subs,i+len(subs),len(s))
# print("the number of occurrences:",s.count(subs))   




# s="ABCABCABCA"
# subs=input('enter the substring to search:')
# i=s.find(subs)
# if i == -1:
#     print("substring not found")
# c=0
# while i != -1:
#     c=c+1
#     print('{} present at index:{}'.format(subs,i))
#     i=s.find(subs,i+len(subs),len(s))
# print("the number of occurrences:",c)   



# s="ABCDEFGH"
# i=s.replace("A","X")
# print(i)



# s="hemanth kolli"
# i=s.replace(" ","")
# print(i)
# print("the no of spaces:",s.count(" "))
# print(len(s)-len(i))



# s="learning python is very easy"
# i=s.replace("python","java")
# print(i)



# s="ABABABA"
# s1=s.replace("A","B")
# print(s)
# print(s1)



# s="ABABABA"
# print("before replacement id of s:",id(s))
# s=s.replace("A","B")
# print(s)
# print("after replacement id of s:",id(s))



# s="hemanth kolli"
# l=s.split()
# print(l)
# for x in l:
#     print(x)



# d="11-07-2023"
# l=d.split("-")
# print(l)
# for x in l:
#     print(x)



# d="abchabchabchabchabc"
# l=d.split("h")
# print(l)
# for x in l:
#     print(x)



# l=["hemanth","kolli"]
# s="  :-  ".join(l)
# print(s)



# l=['10','7','2023']
# s="-".join(l)
# print(s)



# s='Learning Python is very easy'
# i=s.upper()
# print(i)



# s='Learning Python is very easy'
# i=s.lower()
# print(i)



# s='Learning Python is very easy'
# i=s.swapcase()
# print(i)



# s='Learning Python is very easy'
# i=s.title()
# print(i)



# s='Learning Python is very easy'
# i=s.capitalize()
# print(i)



# x="this" ,"is", "a" ,"string"
# s=("-").join(x)
# print(s)



# s=input("enter the first string:")
# s1=input("enter the second string:")
# if s.lower() == s1.lower():
#     print("both are equal")
# else:
#     print("both are not equal")
    
    
    
# s=input("enter the first string:").lower()
# s1=input("enter the second string:").lower()
# if s == s1:
#     print("both are equal")
# else:
#     print("both are not equal")



# username=input("enter the username:")
# password=input("enter the password:")
# if username.lower() == "hemanth" and password == "AnushA":
#     print("valid user")
# else:
#     print("invalid user")



# s=input("enter the string:")
# output=s[0].upper()+s[1:len(s)-1]+s[-2].upper()
# print(output)



s="learning python is very easy"
print(s.startswith("learning") and s.endswith("easy"))
