smallest = None
largest = -1
value = None
while value != 'fin':
   value = input ()
   try:
     value = int(value)
   except:
       continue
   if value > largest:
       largest = value
       continue
   if smallest is None:
       smallest = value
   elif value < smallest:
       smallest = value
       continue
print ('Mayor valor:', largest, 'Menor valor:', smallest)
