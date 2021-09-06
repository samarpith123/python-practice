class mobile:
  def __init__(self,screen,processor):
   self.screen=screen
   self.processor
  def info(self):
   print(self.screen,self.processor)
class mobile1(mobile):
  def __init__(self,screen,processor,ram):
   super().__init__(screen,processor)
   self.ram=ram
class mobile2(mobile1):
  def __init__(self,screen,processor,ram,sound):
   super().__init__(screen,processor,ram)
   self.sound=sound
  def methodinfo(self):
    print(self.screen)
   
    print(self.ram)
    print(self.sound)
c=mobile2('lcd','trww','8gb','dolby')
c.methodinfo()
