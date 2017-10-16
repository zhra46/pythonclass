#2、请写出一段 Python 代码实现分组一个 list 里面的元素,比如 [1,2,3,...100]变成 [[1,2,3],  [4,5,6]....]
orglist=list(range(1,101))
templist=[]
result=[]
for i in orglist:
	templist.append(i)
	if len(templist)>=3:
		result.append(templist[:])#若直接装入templist，result中储存的元素是templist的引用，将随着循环执行不断变化，最终变成100
		templist.clear()
result.append(templist)
#循环执行至最后，将不满三项的最后的templist装入result中
print(result) 

