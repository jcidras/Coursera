fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
words = []
count = 0
try:
	fh = open(fname)
except:
	print "Cannot open file"
for line in fh:
	if line.startswith('From '):
		line = line.rstrip()
		wordsInLine = line.split(' ')
		words.append(wordsInLine[1])
		count = count + 1

for word in words:
    print word
   
print "There were", count, "lines in the file with From as the first word"