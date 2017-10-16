import time
try:
	f = open('1.txt')
	try:
		while True:
			content = f.readline()
			if content == '':
				break
			print(content,end='')
			time.sleep(2)
	except BaseException:
		print('读取文件出现异常')
	else:
		print('读取文件成功')
	finally:
		f.close()
		print('文件成功关闭')
except IOError as result:
	print(result)