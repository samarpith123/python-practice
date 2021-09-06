class food:
  def method1(self):
   print("pizza")


class person:
 def __init__(self,name,place):
   self.name=name
   self.place=place

class employee(person):
 def __init__(self,name,place,salary,foodinfo):
   super().__init__(name,place)
   self.salary=salary
   self.food1=foodinfo
 def display(self):
  print(self.name)
  print(self.place)
  print(self.salary)
  self.food1.method1()
object1=food() 
object=employee('arpith','calicut',15000,object1)
object.display()