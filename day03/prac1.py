#coding=utf-8
weight = float (input('weight'))
height = float (input('height'))
result = weight/(height**2)
print (result)
if weight <= 0 or height <=0 :
	print('输入错误')
elif result >=32:
	print ('dying fat')
elif result >=28:
	print('fat')
elif result >= 25:
	print('too heavy')
elif result >= 18.5:
	print('normal')
else:
	print('too light')