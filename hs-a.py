class car:
   def carmethod(self):
      print("this is car class method")

class sample:
   def __init__(self,name):
     self.name=name
  

class sample2(sample):
    def __init__(self,name,objectreciver):
      super().__init__(name)
      self.carobj=objectreciver

    def display(self):
      print("this is child class method")
      print(self.name)
      print(self.carobj)
      self.carobj.carmethod()
      
carobject=car()
object=sample2('for learning',carobject)
object.display()
