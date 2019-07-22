fname = input('Nombre de archivo: ')
try:
  fhand = open(fname)
except:
  print('El archivo no pudo abrirse:', fname)
  quit()
  
count = 0
sum = 0
for line in fhand:
  if line.startswith('X-DSPAM-Confidence:'):
    line = line.rstrip()
    count = count+1
    print(line)
    space = line.find(' ')
    num = line[space:]
    value = float(num)
    sum = sum + value

average = sum/count
print('El promedio es: ', average)
