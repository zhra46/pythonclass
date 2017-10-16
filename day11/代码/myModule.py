num=10
def add(a,b):
	return a+b

class Person(object):
	def __init__(self,name,age):
		self.name=name
		self.age=age
	def __str__(self):
		return "name:%s,age:%s"%(self.name,self.age)
# __all__=["add","Person"]

if __name__ == "__main__":
	p = Person("zs",20)
	print(p)
	print(__name__)