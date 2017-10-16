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
class Studentlist(object):
	def __init__(self):
		self.dict = {}
		self.length = len(self.dict)
	def addStu(self,Student):
		self.dict[Student.name]=Student
		self.length = len(self.dict)
	def delStu(self,name):
		self.dict.pop(name)
		self.length = len(self.dict)
	def findStu(self,name):
		if name in self.dict:
			return self.dict[name]
		else:
			print('wrong name')
	def printInfo(self):
		for v in self.dict.values():
			v.printinfo()
def save(stus):
	f = open('stus.dat','wb')
	pickle.dump(stus,f)
	f.close()
def load():
	f = open('stus.dat','rb')
	stus = pickle.load(f)
	f.close
	return stus
def printmenu():
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
def printinfo(stus,name=0):
	if stus.length==0:
		print('目前没有学生')
	elif name == 0:
		print('='*75)
		print('序号','姓名','年龄','性别','QQ',sep='\t'*2)
		for v in stus.dict.values():
			v.printInfo()
		print('='*75)
	elif name in stus.dict:
		print('='*75)
		print('序号','姓名','年龄','性别','QQ',sep='\t'*2)
		stus.dict[name].printInfo()
		print('='*75)
	else:
		print('没有这个学生')
def delStu(stus,name):
	if name in stus.dict:
		stus.delStu(name)
		print('删除成功')
		save(stus)
def addStu(stus):
		
		name=input('请输入学生姓名')
		age=input('请输入学生年龄')
		gender=input('请输入学生性别')
		qq=input('请输入学生qq号')
		number=str(stus.length+1)
		stu = Student(name,age,gender,qq,number)
		stus.addStu(stu)
		save(stus)
def modifyStu(stus):
		name=input('请输入要修改的学生名称')
		if name in stus.dict:
			stus.dict[name].age=input('请输入学生年龄')
			stus.dict[name].gender=input('请输入学生性别')
			stus.dict[name].qq=input('请输入学生qq号')
			save(stus)
		else:
			print('没有这个学生')
stus = load()
print (stus)
printmenu()
while True:

	n= input('请输入您要进行的操作(0显示菜单）\n')
	if n == '0':
		printmenu()
	if n == '6':
		quit()
	if n == '1':
		addStu(stus)

	if n =='2':
		printinfo(stus,input('请输入要查找的学生名称'))
	if n == '3':
		modifyStu(stus)
	if n =='4':
		name = input('请输入要删除的学生姓名')
		delStu(stus,name)

	if n =='5':
		printinfo(stus)


