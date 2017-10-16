import os,shutil
def myTree(path):
	dirlist = os.listdir(path)
#	print(dirlist)
	for i in dirlist:
		print (i)
		if os.path.isdir(path+'/'+i) == True:
			myTree(path+'/'+i)
myTree('/Users/tiger/pythonclass')