# Week 7 Assignment 1
fname = raw_input("Enter file name: ")
try:
    fHandle = open(fname)
except:
    print "file", fname, "could not be opened"
    
for lines in fHandle:
    print lines.rstrip().upper()