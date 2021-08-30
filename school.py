class student:
   school='Kv'
   def __init__(self,name,rollno):
     self.name=name
     self.rollno=rollno

   def studentinfo(self):
      print(self.name)
      print(self.rollno)
   
   def schoolname(cls):
      print(cls.school)

x=student('arpith',25)
x.studentinfo()
x.schoolname()
   