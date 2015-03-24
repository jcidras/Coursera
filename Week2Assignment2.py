# Week 2 Assignment 2
fHours = raw_input("Enter Hours")
fRate = raw_input("Enter Rate")
try:
	fPay = (float(fHours) * float(fRate))
except:
	print "Please enter numbers"
	exit()
print fPay