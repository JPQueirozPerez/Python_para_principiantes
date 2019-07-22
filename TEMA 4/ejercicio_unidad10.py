fhand = open('mbox-short.txt')
counts = {}
for line in fhand:
  if line.startswith('From '):
     colon = line.find(':')
     hour = line[colon-2:colon]
     counts[hour] = counts.get(hour, 0) + 1
lst = []
for key, val in counts.items():
   newtup = (key, val)
   lst.append(newtup)
lst = sorted(lst)
for key, val in lst:
  print(key, val)
