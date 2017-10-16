li=[1,2,3,5,4]

#冒泡排序
j=0
for j in range(0,len(li)-1):  #冒泡的次数
	flag = False  #用来记录在冒泡的过程中是否产生了交换，如果没有交换产生，就代表列表已经有序
	for i in range(0,len(li)-1-j):#冒泡的过程
		if li[i] > li[i+1]:
			flag = True   #产生了交换
			li[i],li[i+1] = li[i+1],li[i]
	#判断是否有交换产生，如果没有，列表已经有序，退出循环
	if flag == False:
		break
print(j)
print(li)