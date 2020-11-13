#Write a program that prints the numbers from 1 to 100 and 
#for multiples of ‘3’ print “Fizz” instead of the number and for the multiples of ‘5’ print “Buzz”. 

# Define FizzBuzz function
def FizzBuzz(val):
	# loop through the range of FizzBuzz to print
	for fizz in range(1, val):

		# For both 3 and 5 divisible
		if fizz% 15 == 0:
			print("FizzBuzz")
			continue

		# for only 3 divisibility
		elif fizz% 3 == 0:
			print("Fizz")
			continue

		# for only 5 divisibility
		elif fizz% 5 == 0:
			print("Buzz")
			continue

		print(fizz)

# Defining main function 
def main(): 
    val = input("Enter the number of range of fizzBuzz you want to print:")
    FizzBuzz(int(val))
  
  
# Using the special variable  
# __name__ 
if __name__=="__main__": 
    main() 