'''
读取文件
'''

filename=input('请输入文件：')

# 打开文件
fd = open(filename)

# 读取文件
while True:
    data= fd.read(5)
    # data=fd.readline()
    if not data:
        break
    print(data,end="")


# 迭代方式
for line in fd:
    print(line)




# 关闭文件
fd.close()
