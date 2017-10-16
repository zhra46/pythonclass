class Phone(object):
	def __init__(self,num,ca):
		self.num = num
		self.ca = ca
	def call(self,num):
		print('%s is calling %s'%(self.num,num))
class Computor(object):
	def __init__(self,cpu,mem):
		self.cpu = cpu
		self.mem = mem
	def playGame(self,game):
		print('playing %s'%game)
	def playMusic(self,music):
		print('playing %s'%music)
class Smartphone(Phone,Computor):
	def __init__(self,num,ca,cpu,mem):
		Computor.__init__(self,cpu,mem)
		Phone.__init__(self,num,ca)

iphone = Smartphone('10101010','chinatelecom','i8','100g')
print(dir(iphone))
