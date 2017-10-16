class Dog(object):
	def __init__(self,name,color):
		self.name = name
		self.color = color
	def eat(self):
		print ('%s is running'%self.name)
class Corgi(Dog):
	def setNewName(self,name):
		self.name = name
	def action(self):
		print('%s 遇到其他狗又躺下了'%self.name)
pepper = Corgi('胡椒','黄白')
print('我的名字是%s，我是%s色的'%(pepper.name,pepper.color))
pepper.action()