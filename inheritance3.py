class person:
   def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
   def eatanddrink(self):
        print('eat food')

class employee(person):
    def __init__(self,name,age,place,no,salary):
        super().__init__(name,age,place)
        self.no=no
        self.salary=salary
    def employeeinfo(self):
          print(self.name)
          print(self.age)
          print(self.no)
          print(self.salary)
          print(self.place)
obj=employee('raju',25,'calicut',1,2000000)
obj.eatanddrink()
obj.employeeinfo()