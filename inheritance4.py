class car:
  def __init__(self,name,color):
    
    self.name=name
    self.color=color
  def carinfo(self):
    print(self.name,self.color)
class person:
  def __init__(self,name,age):
     self.name=name
     self.age=age

class employee(person):
     def __init__(self,name,age,salary,numb,car):
       super().__init__(name,age)
       self.salary=salary
       self.numb=numb
       self.car=car
     def display(self):
       print(self.name,self.age,self.salary,self.numb)
       self.car.carinfo()

c=car('hyundai',"red")
c=employee('abc',25,150000,35,c)

c.display()
