li=[3,2,5,1,6,4]

#冒泡排序
for j in range(0,len(li)-1):  #冒泡的次数
	for i in range(0,len(li)-1-j):#冒泡的过程
		if li[i] > li[i+1]:
			li[i],li[i+1] = li[i+1],li[i]


print(li)