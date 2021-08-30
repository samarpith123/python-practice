class new:
     def __init__(self):
       self.name="smartphone"
       
mobile=new()
mobile.rate=50000
mobile.brand="oppo"
print(mobile.__dict__)
del mobile.rate
print(mobile.__dict__)