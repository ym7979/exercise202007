"""文件偏移量"""

file=input('文件：')
f=open(file,'w+')
f.write("hello kitty")
print("文件偏移量：",f.tell())

f.seek(3,0)# 从开头位置 偏移3个字节
data=f.read()
f.close()

import os
# 获取一个目录中的文件列表
print(os.path.getsize('./dict.txt'))
