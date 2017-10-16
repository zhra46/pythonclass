def myP():
	print('-'*30)
def myP1(n=1):
	for i in range(n):
		myP()
def mySum(a,b,c):
	return a+b+c
def myAvr(a,b,c):
	return (a+b+c)/3
myP1(5)
print(myAvr(1,2,4))
