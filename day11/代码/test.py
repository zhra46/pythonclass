import sys
sys.path.append(r"C:\Users\admin\Desktop\python人工智能班2\day11\代码\sub")

import myModule

print(myModule.__all__)
print(myModule.add(10,20))
p = myModule.Person("John",24)
print(p)