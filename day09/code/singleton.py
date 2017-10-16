class User(object):
	__instance = None
	def __init__(self,a,b):
		self.usrn = None
		self.pswd = None
	def __new__(cls,a,b):
		if not cls.__instance:
			cls.__instance = object.__new__(cls)
		return cls.__instance
	def setUsrn(self,usrn):
		self.usrn = usrn
	def setPswd(self,pswd):
		self.pswd = pswd
	def __str__(self):
		return ('usrn : %s pswd: %s'%(self.usrn,self.pswd))

a = User(1,2)
b = User(1,2)
print(id(a),id(b))

a.setUsrn('abc')
a.setPswd('pswd')
print(b)