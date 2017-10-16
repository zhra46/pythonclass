class Animal(object):
	def move(self):
		pass
class Dog(Animal):
	def move(self):
		print('dog running')
class Bird(Animal):
	def move(self):
		print('bird flying')
class Fish(Animal):
	def move(self):
		print('fish swimming')

zoo = [Dog(),Fish(),Bird()]
def zoogame(zoo):
	for i in zoo:
		if isinstance(i,Animal):
			i.move()
zoogame(zoo)