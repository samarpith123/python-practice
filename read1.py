a=int(input("enter first number"))
b=int(input("enter second number"))
s=input("what type of operation u need +/- ")
def add(v1,v2):
   print("sum-",v1+v2)
def sub(v1,v2):
  print("differnce -",v1-v2)
if(s=='+'):
  add(a,b)
elif(s=='-'):
  sub(a,b)
else:
  print("not defined")


  
