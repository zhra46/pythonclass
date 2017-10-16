li=[3,2,5,1,6,4]

#获取列表中的最大值
max=li[0]
for i in range(1,len(li)):
	if max < li[i]:
		max = li[i]

print("max=%d"%max)