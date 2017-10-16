def fact(n):
	if n ==1 :
		return 1
	else:
		return n*fact(n-1)

print (fact(10))

def feb(n):
	if n == 1:
		return 1
	if n == 2:
		return 1
	else:
		return feb(n-1)+feb(n-2)
li = []
# for i in range(1):
# 	li.append(feb(i+1))
print (feb(30))
