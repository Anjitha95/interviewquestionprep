""" Solution 1: Naive Method"""
"""
def triplesum(a, sum):
	for i in range(0,len(a)):
		for j in range(i+1, len(a)):
			for k in range(j+1, len(a)):
				if a[i] +a[j] +a[k] == sum:
					print("The triplet is:",  a[i], ", ", a[j], ", ", a[k] )
					return True
	return False	

"""

""" Solution 2: Using two pointers"""
"""
def triplesum(a, sum, a_size):
	a.sort()

	for i in range(0, a_size-2):
		l = i+1
		r = a_size-1

		while l < r:

			if a[i] +a[l] +a[r] == sum:
				print("The triplet is:",  a[i], ", ", a[l], ", ", a[r] )
				return True
			elif a[i] +a[l] +a[r] < sum:
				l += 1
			else:
				r -= 1
	return False

"""
""" Solution 3: Hashing"""

def triplesum(a, sum, a_size):
	for i in range(0, a_size-1):
		s = set()
		current_sum = sum- a[i]

		for j in range(i+1, a_size):
			if current_sum -a[j] in s:
				print("The triplet is:",  a[i], ", ", a[j], ", ", current_sum -a[j] )
				return True
			s.add(a[j])
	return False



a = [ 1, 4, 45, 6, 10, 8]
sum = 22
a_size = len(a)
triplesum(a, sum, a_size)