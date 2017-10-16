#学生管理系统
#菜单部分：
import os
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
	if len (stus)==0:
		print('目前没有学生')
	elif name == 0:
		print('='*75)
		print('序号','姓名\t','年龄','性别','QQ',sep='\t'*2)
		for k in stus.keys():
			print(stus[k]['number'],k,stus[k]['age'],stus[k]['gender'],stus[k]['qq'],sep='\t'*2)
		print('='*75)
	elif name in stus:
		print('='*75)
		print('序号','姓名','年龄','性别','QQ',sep='\t'*2)
		print(stus[name]['number'],name,stus[name]['age'],stus[name]['gender'],stus[name]['qq'],sep='\t'*2)
		print('='*75)
	else:
		print('没有这个学生')
def delStu(stus,name):
	if name in stus:
		del stus[name]
		print('删除成功')
def addStu(stus):
		stu = {'name':1,'age':2,'gender':3,'qq':4,'number':5}
		stu['name']=input('请输入学生姓名')
		while stu['name'] in stus:
			print('检测到重名，请输入姓名加序号加以区别')
			stu['name']=input('请输入学生姓名')
		stu['age']=input('请输入学生年龄')
		stu['gender']=input('请输入学生性别')
		stu['qq']=input('请输入学生qq号')
		stu['number']=len(stus)+1
		stus[stu['name']]=stu
def modifyStu(stus):
		name=input('请输入要修改的学生名称')
		if name in stus:
			stus[name]['age']=input('请输入学生年龄')
			stus[name]['gender']=input('请输入学生性别')
			stus[name]['qq']=input('请输入学生qq号')
		else:
			print('没有这个学生')
stus = {}
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


