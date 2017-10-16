#开户 存款 取款 查询余额 转账
import os
def cl():
	os.system('clear')
def disMenu1():
	print ('*'*30)
	print ('ATM系统'.center(30))
	print ('','1.开户',sep=' '*12)
	print ('','2.登录账户',sep=' '*12)
	print ('','3.查看所有账户信息',sep=' '*12)
def disMenu2():
	print ('*'*30)
	print ('ATM系统'.center(30))
	print ('','1.存款',sep=' '*12)
	print ('','2.取款',sep=' '*12)
	print ('','3.查询余额',sep=' '*12)
	print ('','4.转账',sep=' '*12)
	print ('','5.退出',sep=' '*12)
class Account():
	def __init__(self,cardnumber,password):
		self.cardnumber = cardnumber
		self.balance = 0
		self.password=password
	def save(self,num):
		self.balance += num
	def showBalance(self):
		print('您的账号为:%s'%self.cardnumber)
		print('您当前的余额为%s'%self.balance)
	def withdraw(self):
		self.showBalance()
		num = int(input('请输入您要取出的金额'))
		while num>self.balance:
			print('您的余额不足,请您重新输入')
			num = int(input('请输入您要取出的金额'))
		self.balance-=num
	def transfer(self,acc,num):
		if num<self.balance:
			self.balance-=num
			acc.balance+=num
		else:
			print('您的余额不足')


accdct={}
while True:
	cl()
	disMenu1()
	op=input('请输入操作序号')
	if op == '1':
		cl()
		num = input('请输入开户账号')
		vflag = 0
		while vflag == 0:
			pas = input('请输入密码')
			pas1 = input('请确认密码')
			if pas == pas1:
				vflag = 1
			else:
				print ('请重新输入')

		acc = Account(num,pas)
		accdct[acc.cardnumber]=acc
	if op == '2':
		cl()
		cnum= input('请输入账号')
		while not (cnum in accdct):
			cnum = input('输入错误请重新输入')

		acc = accdct[cnum]
		pasv = 0
		while pasv == 0:
			pas = input('请输入密码')
			if pas == acc.password:
				pasv =1
			else:
				print('密码错误，请重新输入')
		while True:
				cl()
				disMenu2()
				op = input('请输入操作序号')
				if op =='1':
					cl()
					num = int(input('请输入要存入的金额'))
					acc.save(num)
				if op =='2':
					cl()
					acc.withdraw()
				if op =='3':
					cl()
					acc.showBalance()
					n=input('输入0 退出')
					
				if op =='4':
					cl()
					cnum = input('请输入要转账的账户')
					num = int(input('请输入要转账的金额'))
					acc2 = accdct[cnum]
					acc.transfer(acc2,num)
				if op =='5':
					cl()
					op = 0
					break
	if op == '3':
		cl()
		for v in accdct.values():
			v.showBalance()
