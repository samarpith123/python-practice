class test:
  def __init__(self):
    self.name="arpith"
    self.color="red"
    print(self.color,self.name)
    print("-----")
  def read(self):
     self.write=45
     print(self.write)
     
c=test()
c.height=65
c.weight=72
print(c.__dict__)



