num=10
def add(a,b):
	return a+b

class Person(object):
	def __init__(self,name,age):
		self.name=name
		self.age=age
	def __str__(self):
		return "name:%s,age:%s"%(self.name,self.age)

