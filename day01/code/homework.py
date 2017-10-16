#coding=utf-8
#1 输入半径求周长及面积的作业
r = int(input('pls enter r'))
c = 2*3.14*r
s = 3.14 * r * r 
print ('周长为%d'%c)
print('面积为%d'%s)
#2 判断奇偶作业
n = int(input('pls enter a num'))
if n%2 == 0:
	print ('输入的数%d为偶数'%n)
else:
	print ('输入的数%d为奇数'%n)
#3 输出乘法表
n = input('enter 1 to output multitable')
if n == '1':
	for i in range(9):
		print ('')
		for j in range (i+1):
			print (str(j+1)+'*'+str(i+1)+'='+str((i+1)*(j+1)), end = '  ')
			
		
else:
	quit()