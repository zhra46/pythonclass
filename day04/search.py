url='https://www.hao123.com?name=usr1&password=123123'
i1=url.find('?name=')
i2=url.find('&password=')
user=url[i1+len('?name='):i2]
password=url[i2+len('&password='):]
print('原始网址是%s'%url)
print('用户名：%s'%user)
print('密码：%s'%password)