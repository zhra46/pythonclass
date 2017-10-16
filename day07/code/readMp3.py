f = open ('test.mp3','rb')
f.seek(-128,2)
b=f.read()
print(b)