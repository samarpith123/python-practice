class cricketbat:
     def __init__(self):
        self.name="newbalance"
        
c=cricketbat()
c.rate=15000
c.color="red"
print(c.__dict__)
del c.color
print(c.__dict__)
c.weight=89
del c.weight
print(c.__dict__)
