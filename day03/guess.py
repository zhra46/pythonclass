answer = 33
n= int(input('请输入一个1-100之间的整数'))
while True:
	if not (n>0 and n<101):
		print('输入错误')

	if n == answer:
		print('恭喜你答对了')
		break
	elif n>answer:
		n = int(input ('大了，再猜'))
	elif n<answer:
		n = int(input ('小了，再猜'))