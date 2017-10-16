#1、给定一个字符串aStr，返回使用空格或者'\t'分割后的倒数第二个子串
str='Python is an easy to learn, powerful programming language.'
list=str.split()
print('原始字符串为：\n "%s" '%str)
print('倒数第二个子字符串为：\n"%s"'%list[-2])
