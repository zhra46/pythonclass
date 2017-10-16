class LongError(Exception):
	def __init__(self,len,atleast):
		self.len = len
		self.atleast = atleast
	def __str__(self):
		return 'wrong length'
def test():
	while True:
		content = input()
		if len(content)< 3:
			raise LongError(len(content),3)
		else:
			print (content)
try:
	test()
except Exception as e:
	print (e)