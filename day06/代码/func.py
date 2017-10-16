#函数定义
def add(a,b):
	print("a=%d,b=%d"%(a,b))
	return a+b

def hello():
	print("hello world")
	return
	print("============")

#函数调用
rtn=hello()
print(rtn)
print(add(b=10,a=20))