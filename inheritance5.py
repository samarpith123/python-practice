class car:
    def __init__(self,name,colour):
     self.name=name
     self.colour=colour
    
    def carinfo(self):
     print(self.name,self.colour)
     
class person:
    def __init__(self,name,age):
     self.name=name
     self.age=age

class empl(person):
    def __init__(self,name,age,numb,salary,car):
     super().__init__(name,age)
     self.numb=numb
     self.salary=salary
     self.car=car
     
    def display(self):
     print(self.name)
     print(self.age)
     print(self.numb
self.car.carinfo()
   
carobject=car('bmw','darkblue') 
empobject=empl('jithin',25,2,250000,carobject)
empobject.display()
