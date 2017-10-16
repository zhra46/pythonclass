for i in range(9):
	out=''
	for j in range (i+1):
		out+=str(j+1)+'*'+str(i+1)+'='+str((i+1)*(j+1)) +'   '
	print (out)