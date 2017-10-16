#写一个函数打印一条横线
def printALine():
	print("-------------")

#打印自定义行数的横线
def printLines(lines,width):
	for i in range(0,lines):
		print("-"*width)

#写一个函数求三个数的和
def add(a,b,c):
	return a+b+c
#写一个函数求三个数的平均值
def average(a,b,c):
	return (a+b+c)/3


printALine()
printLines(10,20)

print(add(10,20,30))
print(average(10,20,30))