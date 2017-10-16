class Person(object):
	def __init__(self,name):
		self.name = name
	def work(self,axetype):
		print('%s is working'%self.name)
		axe = Factory.createAxe(axetype)
		axe.cut()
class Factory(object):
	@staticmethod
	def createAxe(axetype):
		if axetype == 'sa':
			return StoneAxe()
		if axetype == 'ia':
			return IronAxe()
		if axetype == 'ga':
			return GoldenAxe()
class Axe(object):
	def __init__(self):
		self.name = None
	def cut(self):
		print("he is using %s cutting tree"%self.name)

class GoldenAxe(Axe):
	def __init__(self):
		self.name = 'GoldenAxe'

class IronAxe(Axe):
	def __init__(self):
		self.name = 'IronAxe'

class StoneAxe(Axe):
	def __init__(self):
		self.name = 'StoneAxe'
p = Person('john')
p.work('ia')
