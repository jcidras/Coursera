# Week 3 Assignment 2
inputScore = raw_input("Enter Score:")
try:
	fScore = float(inputScore)
except:
	print "Please enter a number"
	exit()
if fScore > 1.0 or fScore < 0.0:
    print "Score out of range"
else:
    if fScore >= 0.9:
        print "A"
    elif fScore >= 0.8:
        print "B"
    elif fScore >= 0.7:
        print "C"
    elif fScore >= 0.6:
        print "D"
    else:
        print "F"