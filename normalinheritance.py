class base:
    def basemethod(self,name,age):
          self.name=name
          self.age=age
          print(self.name,self.age)
 

class child(base):
      def childmethod(self,place):
          self.place=place
          print(self.place)


obj=child()
obj.basemethod('raju',25)
obj.childmethod('calicut')