def printStu(name,age=25):
	print("name=%s,age=%d"%(name,age))

def add(a=10,c=30,b=20):
	return a+b+c

printStu("zhangsan")

print(add())
print(add(10))
print(add(5,6))
print(add(4,5,6))