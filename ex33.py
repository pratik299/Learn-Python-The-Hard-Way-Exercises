i = 0
numbers = []

def practice_loop(limit):
	i = 0
	while i < limit:
		print "At the top i is %d" % i
		numbers.append(i)
	
		i += 1
		print "Numbers now: ", numbers
	
		print "At the bottom i is %d" % i

practice_loop(4)
	
print "The numbers: "

for num in numbers:
	print num