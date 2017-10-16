import os,shutil
def myTree(path,tabcount=0):
	dirlist = os.listdir(path)
	dirlist.sort()
	for i in dirlist:
		fname=os.path.join(path,i)
		print ('  '*tabcount+i)
		if os.path.isdir(fname) == True:
			myTree(fname,tabcount+1)
myTree('/Users/tiger/pythonclass')#
