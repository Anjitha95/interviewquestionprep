"""A strobogrammatic number is a number that looks like the same when rotated.
180 degrees. Write a function to determine if a number is strobogrammatic. 
Input: 69  Output: True
Input: 828 Output: False"""

def isstrobagrammatic(num):

	lookup = {'0':'0', '1':'1','6':'9', '8':'8', '9':'6'}
	ans = ''
	for n in num:
		if n not in lookup:
			return False
		ans += lookup[n]
	return ans[::-1] == num



val = input("Enter the number:")
result = isstrobagrammatic(val)
print(result)
  