# Week 7 Assignment 2
def returnAverage (spam, count):
    return (spam / count)

fname = raw_input("Enter file name: ")
try:
	fh = open(fname)    
except:
    print "Unable to open file:", fname
    exit()
fspam = 0.0
icount = 0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:") : 
        fspam = fspam + float(line[20:26])
        icount = icount + 1

print "Average spam confidence:", returnAverage(fspam,icount)