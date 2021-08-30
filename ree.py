class sample:
   schoolname='ghss'
   def __init__(self,name,rollno):
       self.name=name
       self.rollno=rollno    
   def demo(self):
       print(self.name)
       print(self.rollno)
   def classmethod(cls):
       print(cls.schoolname)

s=sample('arjun',1)
s1=sample('sharath',2)
s3=sample('vijisha',3)
s.classmethod()