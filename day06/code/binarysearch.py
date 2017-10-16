def binsrch(li,value):
	high = len(li)-1
	low = 0
	flag = False
	while flag == False:
		mid = (high+low)//2
		if li [mid]==value:
			return mid
		elif li [mid] > value:
			high = mid-1
		elif li [mid] < value:
			low = mid+1
li=[1,2,3,4,5,6]
print(binsrch(li,6))