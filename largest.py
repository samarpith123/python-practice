a=int(input("Enter 3 numbers to compare"))
b=int(input())
c=int(input())

op=input("smallest/largest?")


def larg(a,b,c):
   if(a>b) and (a>c):
      largest = a
   elif(b>a) and (b>c):
      largest = b
   else:
      largest = c
   print("largest is: ",largest)

def small(a,b,c):
    if(a<b) and (a<c):
       smallest = a
    elif(b<a) and (b<c):
       smallest = b
    else:
       smallest = c
    print("smallest is: ",smallest)

if(op=='smallest'):
  small(a,b,c)
elif(op=='largest'):
  larg(a,b,c)
