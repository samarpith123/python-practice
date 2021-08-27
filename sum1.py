class sum:
 
  def __init__(self,result):
    self.result=result
    print(self.result)

a=int(input("enter starting number"))
b=int(input("enter last number"))
x=0
for v in range(a,b):
   x=x+v
print(x)
g=sum(x)

