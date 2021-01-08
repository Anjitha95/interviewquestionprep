
def secondlargest(list_ex):
	list_ex.sort()
	return list_ex[-2]




list_ex =[]

num = int(input("Enter number of elements in list: "))
 
for i in range(1, num + 1):
    val = int(input("Enter elements: "))
    list_ex.append(val)

number = secondlargest(list_ex)
print(number)