#请写出一段 Python 代码实现删除一个 list 里面的重复元素
import random
def reMoveSame(list):
	list1=[]
	for i in list:
		if not (i  in list1):
			list1.append(i)
	return list1
		
def testListGen(n):
	rtlist=[]
	for i in range(n):
		rtlist.append(random.randint(0,20))
	return rtlist

a=testListGen(100)
print('生成的列表为：')
print(a)
print('去掉重复元素的列表为')
b=reMoveSame(a)
print(b)

