class person:
   def __init__(self,name,age):
        self.name=name
        self.age=age
   def eatanddrink(self):
        print('eat food')

class employee(person):
    def __init__(self,name,age,no,salary):
        super().__init__(name,age)
        self.no=no
        self.salary=salary
    def employeeinfo(self):
          print(self.name)
          print(self.age)
          print(self.no)
          print(self.salary)

obj=employee('raju',25,1,2000000)
obj.eatanddrink()
obj.employeeinfo()
