import sys
sName = sys.argv[1]
tName = sys.argv[2]
with open (sName,'r') as f:
	temp = f.read()
with open (tName,'w') as f:
	f.write(temp)
