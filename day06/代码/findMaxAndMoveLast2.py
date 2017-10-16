li=[3,2,5,1,6,4]

#一边找最大值，一边向后换

for i in range(0,len(li)-1):
	if li[i] > li[i+1]:
		li[i],li[i+1] = li[i+1],li[i]


print(li)

