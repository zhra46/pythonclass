def fun(*args):
	for arg in args:
		print(arg)

# fun(1,2,3)
# fun(4,5,6,7,8,9)
li=[4,6,7,8]
# fun(*li)
def fun2(**kwargs):
	for k,v in kwargs.items():
		print("%s:%s"%(k,v))

d1={"one":1,"two":2}
# fun2(name="lishi",age="20",socre=89)
# fun2(**d1)

def fun3(*args,**kwargs):
	for arg in args:
		print(arg)
	for k,v in kwargs.items():
		print("%s:%s"%(k,v))

fun3(*li,**d1)