for i in range(1,10):
	for j in range(1,i+1):
		if i*j<10:
			print('%d*%d=%d '%(i,j,i*j),end='  ')
		else:
			print('%d*%d=%d'%(i,j,i*j),end='  ')
	print ('')
