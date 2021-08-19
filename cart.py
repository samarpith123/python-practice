cart=[500,200,500000,10000]
for item in cart:
    if(item>=500000):
      print("item is skipped")
      continue
      print("processed item:",item)