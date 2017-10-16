def moveRight(li):
	temp = li[-1]
	for i in range(len(li)-1):  
		li[len(li)-1-i]=li[len(li)-2-i]
	li[0]=temp
def moveRightn(li,n=1):
	for i in range(n):
		moveRight(li)

li=[1,2,3,4,5]
moveRightn(li,3)
print(li)
