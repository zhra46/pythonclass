class Dog(object):
	def __init__(self,name):
		self.__name = name
		self.name = name
	def printName1(self):
		print(self.__name)
	def printName(self):
		print(self.name)
class Corgi(Dog):
	def setNewName(self,name):
		self.name = name
	def test(self):
#		print (self.__name)
		self.printName()
p = Corgi('hujiao')
p.setNewName('h')
p.test()
#print(dir(p))