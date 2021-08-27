list_of_movies=[]
class movies:
 
   def __init__(self,moviename,jounar):
     self.moviename=moviename
     self.jounar=jounar
 
   def info(self):
    print(self.moviename)
    print(self.jounar)

while True:
  title=input("enter movie name")
  recieve=input("enter jounar")
  x=movies(title,recieve)
  list_of_movies.append(x)
  print("movie added")
  option=input("do u want to add more y/n")
  if(option=="n"):
    break
print("all movies information")
for b in list_of_movies:
  b.info()
  print("----")
  print(b.moviename)
  
