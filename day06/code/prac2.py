import random
list = [2,55,4,12,36,1,28]
max=list[0]
for i in list:
	if i > max:
		max = i
list[-1],list[list.index(max)]=list[list.index(max)],list[-1]
print (list)
list1 = [4,55,2,12,36,1,28]
max = list1[0]
idx = 0
for i in range(len(list1)):
	if list1[i]> max:
		max = list1[i]
		idx = i 
		list1[-1],list1[idx] = list1[idx],list1[-1]

print (list1)
for j in range(len(list)-1):
	flag =  False
	for i in range(len(list)-1-j):
		if list1[i]  >  list1[i+1]:
			flag =  True
			list1[i]  ,  list1[i+1]  =  list1[i+1], list1[i]
	if flag ==  False:
		break
print (j)
print(list1)


