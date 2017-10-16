class Book(object):
	def __init__(self,title,auther,price):
		self.title = title
		self.auther = auther
		self.price = price
	def printinfo(self):
		print("title:%s\tauther:%s\tprice%s\t"%(self.title,self.auther,self.price))
book1 = Book('python','zhangsan',999)
book1.printinfo()
