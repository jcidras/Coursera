# Week 5 Assignment 1
largest = None
smallest = None
numbers = []
while True:
    num = raw_input("Enter a number: ")
    try:
        if num == "done": break
        else:
             numbers.append(int(num))
    except:
        print "Invalid input"
        
for num in numbers:
    if largest is None or largest < num:
        largest = num

	if smallest is None or smallest > num:
		smallest = num

print "Maximum is", largest
print "Minimum is", smallest