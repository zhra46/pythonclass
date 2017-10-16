def test1():
	print('test1.1')
	print(num)
	print('test1.2')
def test2():
	print('test2.1')
	test1()
	print('test2.2')
def test3():
	print('test3.1')
	try:
		test2()
	except :
		print('捕获异常')
	finally:
		print('test3.2')
test3()