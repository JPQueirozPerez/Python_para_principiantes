handle = open('mbox-short.txt')
counts = dict()
email = list()
for line in handle:
  if line.startswith('From '):
     words = line.split()
     email = email + words[1:2]
for word in email:
  counts[word] = counts.get(word,0)+1
bigcount = None
bigword = None
for word,count in counts.items():
  if bigcount is None or count > bigcount:
    bigword = word
    bigcount = count
print('Emisor con más mensajes:', bigword, 'con', bigcount, 'mensajes')
