def order(num):
	n = 0
	while num != 0:
		n += 1
		num = num // 10
	return n


def power(p, num):
	print(p)
	if p == 0:
		return 1
	else:
		return pow(num, p)
	

def isamstrong(num):
	n = order(num)
	temp = num
	#print(temp)
	sum1 = 0

	while temp != 0:
		r = temp % 10
		print(r)
		sum1 = sum1 + power(n, r)
		print(sum1)
		temp = temp // 10
	if sum1 == num:
		print("This is amstrong number")
	else:
		print("This is not an amstrong number")

val = input("Enter the number:")
isamstrong(int(val))
  