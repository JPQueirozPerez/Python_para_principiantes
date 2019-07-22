fhand = open('mbox-short.txt')
mbox = list(fhand)
count = 0
for line in mbox:
  if line.startswith('From '):
    line = line.rstrip()
    colon = line.find(':')
    email = line[4:colon-13]
    count = count + 1
    print(email)
print('Personas: ',count)
