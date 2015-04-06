words = []
fname = raw_input("Enter file name: ")
try:
	fh = open(fname)
except:
	print "Cannot open file."
for line in fh:
    line = line.rstrip()
    wordsInLine = line.split(' ')
    for word in wordsInLine:
        if word not in words:
        	words.append(word)
        
words.sort()
print words