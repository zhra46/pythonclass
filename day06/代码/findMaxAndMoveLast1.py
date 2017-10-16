li=[3,2,5,1,6,4]

#获取列表中的最大值的下标
max=0
for i in range(1,len(li)):
	if li[max] < li[i]:
		max = i

print("max=%d"%max)

#交换位置
if max != len(li)-1:
	li[max],li[-1] = li[-1],li[max]

print(li)