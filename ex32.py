the_count = [1,2,3,4,5]
fruits = ['apples', 'oranges', 'pears', 'apricoats']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# for loop for list

for number in the_count:
	print "The count is %d" % number
	
for fruit in fruits:
	print "A fruit of type %s" % fruit
	
for i in change:
	print "I got %r" % i
	
elements = []

for i in range(0, 6):
	print "Adding %d to the list." %i
	elements.append(i)
	
for i in elements:
	print "Element was: %d" % i