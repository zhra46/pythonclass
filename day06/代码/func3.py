def divide(a,b):
	shang=a//b
	yushu=a%b
	return shang,yushu  #实际返回一个元组

sh,yu=divide(5,2)
print(sh,yu)

a=10
b=20
def swap(a,b):
	return b,a

def swap2(a,b):#交换的是局部变量，全局变量不受影响
	a,b=b,a

def swap3():#没有通用性
	global a
	global b
	a,b = b,a

a,b=swap(a,b)

print(a,b)
