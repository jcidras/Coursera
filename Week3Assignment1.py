# Week 3 Assignment 1
strHours = raw_input("Enter Hours:")
strHourlyPay = raw_input("Enter Pay:")
fOvertimePay = 1.50
try:
	fHours = float(strHours)
	fHourlyPay = float(strHourlyPay)
except:
	print "Please enter numbers"
	exit()
#Test for overtime
if fHours > 40:
    fOvertime = fHours - 40
    fHourlyPayTotal = fHourlyPay * 40
    fOvertimePayTotal = ((fHourlyPay * fOvertime) * fOvertimePay)
    print fHourlyPayTotal + fOvertimePayTotal
else:
     print fHourlyPay * fHours