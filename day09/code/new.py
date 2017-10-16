class User(object):
	def __init__(self,usrn,pswd):
		self.usrn = usrn
		self.pswd = pswd
	def __new__(cls,usrn,pswd):
		print('new() is called')
		return object.__new__(cls)
u = User('abc','abc')