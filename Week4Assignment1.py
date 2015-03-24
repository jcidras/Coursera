# Week 4 Assignment 1
def computepay(hours,rate,overtimeRate):
    if hours > 40:
        return ((((hours - 40) * rate) * overtimeRate) + (40 * rate))
    else:
    	return hours * rate

sHours= raw_input("Enter Hours:")
sRate = raw_input("Enter Rate:")
sOvertimeRate = raw_input("Overtime Rate:")

try:
	fHours = float(sHours)
	fRate = float(sRate)
	fOvertimeRate = float(sOvertimeRate)
except:
	print "Please enter numbers"
	exit()

fPay = computepay(fHours,fRate,fOvertimeRate)
print fPay