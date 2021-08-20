a=[[5,6],[2,4]]

def sum(f):
     result=0
     for i in f:
          for k in i:
             result=result+k
     print(result)
sum(a)