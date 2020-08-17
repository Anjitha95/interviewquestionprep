# count the number of flipped bits

# define a funtion to count the flipped bits
def countbits(number):
	"""Counts the number of 
	bits that are flipped."""
	count = 0
	while number:
		count += 1
		number &= (number-1)
	return count

# function to flip the number
def flippednumber(num1, num2):
	""""XOR of nums only flip the bits of numbers that are different """
	return countbits(num1^num2)

# let us assume that the following numbers are the input 
num1 = 7
num2 = 10
print(flippednumber(num1,num2))
