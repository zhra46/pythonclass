class Dictclass(object):
	def __init__(self,dict):
		self.dict = dict
	def get_dict(self,key):
		if not key in self.dict:
			print('wrong key')
		else:
			return self.dict[key]
	def get_key(self):
		return list(self.dict)
	def update_dict(self,dict1):
		self.dict.update(dict1)
		return list(self.dict.values())

	def __repr__(self):
		return 'this is __rept__' 

d = {1:2,3:4}
d1 = {5:6,7:8}
dc = Dictclass(d)
print(dc.get_dict(1))
print(dc.get_key())
print(dc.update_dict(d1))
print(repr(dc))

