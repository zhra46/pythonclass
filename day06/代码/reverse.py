li=[3,2,5,1,6,4]

for i in range(0,int(len(li)/2)):
	li[i],li[len(li)-i-1] = li[len(li)-i-1],li[i]

print(li)