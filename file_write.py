"""写操作"""

f=open('file.txt','wb')

#  写操作   有中文必须.encode()
f.write("hello 你好".encode())

list_=['今天\n','2020年\n']
f.writelines(list_)

f.close()
