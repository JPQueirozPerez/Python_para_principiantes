horas = input ('Introduzca las horas: ')
try:
   horas = int(horas)
except: horas = -1
if horas < 0 :
   print ('Error, por favor introduce un número')
else:
   precio = input ('Introduzca el precio/hora: ')
   try:
     precio = int (precio)
   except: precio = -1
   if precio < 0 :
     print ('Error, por favor introduce un número')
   else:
     if horas>40:
       h_extra = horas-40
       p_extra = precio*1.5
     total = (horas-h_extra) * precio + h_extra * p_extra
     print ('El total a pagar es:', total)

