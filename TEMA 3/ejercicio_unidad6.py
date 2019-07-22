data = 'X-DSPAM-Confidence: 0.8475'
space = data.find(' ')
num = data[space:]
value = float(num)
print(value)
