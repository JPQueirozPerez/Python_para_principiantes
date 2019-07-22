fhand = open('romeo.txt')
romeo = list(fhand)
wordList = list()
for line in romeo:
    words = line.split()
    wordList = list(set(wordList))
    wordList = wordList + words
wordList.sort(key=str.lower)
print(wordList)