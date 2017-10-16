#coding=utf-8
money = 1
seat = 4
if money>=2:
	print('上车')
	if seat >0:
		print('有空位可以坐下')
	else:
		print('只能站着')
else:
	print('没钱了去充值')