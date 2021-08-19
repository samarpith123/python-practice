a=int(input("enter a number"))
b=int(input("enter second number"))
def result(v1,v2):
   add=v1+v2
   sub=v1-v2
   return add,sub

c=result(a,b)
print(type(c))
print(c)

def sayhello():
   print("hello")
d=sayhello()
print(d)
print(type(d))
