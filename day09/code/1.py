class Person(object):
	def __init__(self,name):
		self.__name = name
	def __str__(self):
		return ('name: %s'%self.__name)
	def setname(self,name):
		if len(name)>5:
			self.__name = name
		else:
			print('名字必须大于5个字符')
	def getname(self):
		return self.__name
p = Person('zhangsan')
print(p)
p.setname('13')
p.setname('lisisi')
print(p)