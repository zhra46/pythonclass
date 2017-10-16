def bubble(*list):
	for j in range(len(list)-1):
		flag = False
		for i in range(len(list)-1-j):
			if list[i] > list[i+1]:
				flag = True
				list[i],list[i+1]=list[i+1],list[i]
		if flag == False:
			break
	print (list)
list =[8,2,52,3,44,1,32]
bubble(list)
print (list)
