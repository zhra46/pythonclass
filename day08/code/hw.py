#学生管理系统
#菜单部分：
import os,pickle
class Student(object):
	def __init__(self,name,age,gender,qq,number):
		self.name = name
		self.age = age
		self.gender = gender
		self.qq = qq
		self.number = number
	def printInfo(self):
		print (self.number,self.name,self.age,self.gender,self.qq,sep='\t'*2)
class Ui(object):
	def printmenu(self):
		print ('='*50)
		t1= '学生管理系统'
		t1.center(50)
		print('输入1.添加学生'.center(50))
		print('输入2.查找学生'.center(50))
		print('输入3.修改学生'.center(50))
		print('输入4.删除学生'.center(50))
		print('输入5.查看所有学生'.center(50))
		print('输入6.退出'.center(50))
		print ('='*50)
	def detect(self,stus):
		n= input('请输入您要进行的操作(0显示菜单）\n')
		if n == '0':
			self.printmenu()
		if n == '6':
			quit()
		if n == '1':
			stus.addStu()
		if n =='2':
			stus.printInfo(input('请输入要查找的学生名称'))
		if n == '3':
			stus.modifyStu()
		if n =='4':
			stus.delStu(input('请输入要删除的学生姓名'))
		if n =='5':
			stus.printInfo()
	def __init__(self):
		self.printmenu()
		
		self.detect()

class Studentlist(object):
	def __init__(self):
		self.dict = {}
		self.length = len(self.dict)
	def save(self):
		f = open('stus.dat','wb')
		pickle.dump(self.dict,f)
		f.close()
	def load(self):
		f = open('stus.dat','rb')
		self.dict = pickle.load(f)
		f.close
		return stus
	def printInfo(self,name=0):
		if self.length==0:
			print('目前没有学生')
		# name = 0 就打印所有学生
		elif name == 0:    
			print('='*75)
			print('序号','姓名','年龄','性别','QQ',sep='\t'*2)
			for v in self.dict.values():
				v.printInfo()
			print('='*75)
		elif name in self.dict:
			print('='*75)
			print('序号','姓名','年龄','性别','QQ',sep='\t'*2)
			self.dict[name].printInfo()
			print('='*75)
		else:
			print('没有这个学生')
	def delStu(stus,name):
		if name in self.dict:
			self.dict.pop(name)
			print('删除学生%s成功'%name)
			self.save()
	def addStu(self):
			name=input('请输入学生姓名')
			age=input('请输入学生年龄')
			gender=input('请输入学生性别')
			qq=input('请输入学生qq号')
			number=str(stus.length+1)
			self.dict[name] = Student(name,age,gender,qq,number)
			self.save()
	def modifyStu(self):
			name=input('请输入要修改的学生名称')
			if name in self.dict:
				self.dict[name].age=input('请输入学生年龄')
				self.dict[name].gender=input('请输入学生性别')
				self.dict[name].qq=input('请输入学生qq号')
				self.save()
			else:
				print('没有这个学生')
stus = load()
print (stus)
printmenu()
while True:

	


