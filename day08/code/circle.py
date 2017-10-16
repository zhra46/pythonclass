class Circle(object):
	Pi=3.14
	@classmethod
	def setPi(gls,n):
		gls.Pi = n
	def __init__(self,r,x,y):
		self.r = r
		self.x = x
		self.y = y
	def area(self):
		return self.r^2*3.14
	def draw(self):
		print('以（%d,%d)为圆心画了一个半径为%.2f的圆'%(self.x,self.y,self.r))
c1 = Circle(4,33,33)
print(c1.Pi)
Circle.setPi(3.1415)
print(c1.Pi)
print(Circle.Pi)