class market:
  def __init__(self,name,color):
    self.name=name
    self.color=color
  def marketinfo(self):
    print(self.name)
    print(self.color)
 
class urban(market):
   def __init__(self,name,color,looks,height):
    super().__init__(name,color)
    self.looks=looks
    self.height=height
   def work(self):
       print(self.name)
       print(self.color) 
       print(self.looks)
       print(self.height) 

 
x=urban('tomato','red','lush',175)
x.marketinfo()
x.work() 